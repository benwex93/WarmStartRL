import copy
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Actor(nn.Module):
	def __init__(self, state_dim, action_dim, max_action):
		super(Actor, self).__init__()

		self.l1 = nn.Linear(state_dim, 256)
		self.l2 = nn.Linear(256, 256)
		self.l3 = nn.Linear(256, action_dim)
		
		self.max_action = max_action
		

	def forward(self, state):
		a = F.relu(self.l1(state))
		a = F.relu(self.l2(a))
		return self.max_action * torch.tanh(self.l3(a))

class Critic(nn.Module):
	def __init__(self, state_dim, action_dim, layer_width, dropout_rate):
		super(Critic, self).__init__()

		# Q1 architecture
		self.l1 = nn.Linear(state_dim + action_dim, 256)
		self.l2 = nn.Linear(256, 256)
		self.l3 = nn.Linear(256, 1)

		# Q2 architecture
		self.l4 = nn.Linear(state_dim + action_dim, 256)
		self.l5 = nn.Linear(256, 256)
		self.l6 = nn.Linear(256, 1)

	def forward(self, state, action):
		sa = torch.cat([state, action], 1)

		q1 = F.relu(self.l1(sa))
		q1 = F.relu(self.l2(q1))
		q1 = self.l3(q1)

		q2 = F.relu(self.l4(sa))
		q2 = F.relu(self.l5(q2))
		q2 = self.l6(q2)
		return q1, q2


	def Q1(self, state, action):
		sa = torch.cat([state, action], 1)

		q1 = F.relu(self.l1(sa))
		q1 = F.relu(self.l2(q1))
		q1 = self.l3(q1)
		return q1

class TD3C(object):
	def __init__(
		self,
		state_dim,
		action_dim,
		max_action,
		discount=0.99,
		tau=0.005,
		policy_noise=0.2,
		noise_clip=0.5,
		policy_freq=2,
		start_update_policy=0,
		dropout_rate=0.1,
		layer_width=256,
		alpha=0.5,
		actor_update_rule=None,
		const_dU = 1,
		learning_rate = 3e-4,
	):

		self.actor = Actor(state_dim, action_dim, max_action).to(device)
		self.actor_target = copy.deepcopy(self.actor)
		self.actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=learning_rate)

		self.critic = Critic(state_dim, action_dim, layer_width, dropout_rate).to(device)
		self.critic_target = copy.deepcopy(self.critic)
		self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=3e-4)

		self.start_update_policy = start_update_policy

		self.max_action = max_action
		self.discount = discount


		# self.tau = tau * (1.-dropout_rate)
		self.tau = tau		
		self.policy_noise = policy_noise
		self.noise_clip = noise_clip
		self.policy_freq = policy_freq

		self.total_it = 0

		self.N_copies_for_uncertainty = 100
		self.state_uncertainties = []
		self.gradient_info = []
		self.dropout_rate = dropout_rate
		self.layer_width = layer_width
		self.alpha = alpha
		self.actor_update_rule = actor_update_rule
		self.const_dU = const_dU
	def select_action(self, state):
		state = torch.FloatTensor(state.reshape(1, -1)).to(device)
		return self.actor(state).cpu().data.numpy().flatten()

	def q_uncertainty(self, state, action):

		with torch.no_grad():

			#copy state/action for multiple passes through critic to calculate uncertainty
			action_copies = action.repeat(self.N_copies_for_uncertainty, 1)

			s_copies = state.repeat(self.N_copies_for_uncertainty, 1)

			#turn on train mode so that dropout is enabled
			self.critic.train()
			Q_copies_dropout = self.critic.Q1(s_copies, action_copies)
			self.critic.eval()
			Q_copies_dropout = \
				Q_copies_dropout.view(self.N_copies_for_uncertainty, action.shape[0], -1)
			mu = Q_copies_dropout.mean(0, keepdim=True)
			#calculate variance
			# uncertainty_estimation = ((Q_copies_dropout - mu) ** 2).mean(0)

			uncertainty_estimation =  Q_copies_dropout.var(0, keepdim=True)
			#batch average uncertainty
			# sigma_avg = uncertainty_estimation.mean()
			#coefficient of variation (sigma/mu):
			#no need to do mean over batch
			uncertainty_estimation_score = (torch.sqrt(uncertainty_estimation) / torch.abs(mu))
			return uncertainty_estimation_score.flatten().cpu().numpy(), mu.flatten().cpu().numpy() 

	def train(self, replay_buffer, batch_size=100, main_timestep=0):
		self.total_it += 1

		# Sample replay buffer 
		state, action, next_state, reward, not_done = replay_buffer.sample(batch_size)

		#####################
		#Critic Update
		#####################
		self.critic.eval()
		with torch.no_grad():
			# Select action according to policy and add clipped noise
			noise = (
				torch.randn_like(action) * self.policy_noise
			).clamp(-self.noise_clip, self.noise_clip)
			
			next_action = (
				self.actor_target(next_state) + noise
			).clamp(-self.max_action, self.max_action)

			# Compute the target Q value
			target_Q1, target_Q2 = self.critic_target(next_state, next_action)
			target_Q = torch.min(target_Q1, target_Q2)
			target_Q = reward + not_done * self.discount * target_Q

		self.critic.train()
		# Get current Q estimates
		current_Q1, current_Q2 = self.critic(state, action)

		# Compute critic loss
		critic_loss = F.mse_loss(current_Q1, target_Q) + F.mse_loss(current_Q2, target_Q)

		# Optimize the critic
		self.critic_optimizer.zero_grad()
		critic_loss.backward()
		self.critic_optimizer.step()

		if self.total_it % 2 == 0:
			# Update the frozen target models
			for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
				target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)


		# Delayed policy updates
		if self.total_it > self.start_update_policy and \
			self.total_it % self.policy_freq == 0:


			#####################
			#Uncertainty Calculate
			#####################
			#Zero gradients are cleared before making any gradient operation so they don't accumulate
			self.actor.zero_grad()
			self.critic.zero_grad()
			self.actor_optimizer.zero_grad()
			self.critic_optimizer.zero_grad()

			pi_a = self.actor(state)
	
			#Need detached version of actions to calculate Q/U s.t. backprop via Q/U wont go into policy weights 
			#Need to turn on the requires_grad signal s.t. gradients will be calculated at the action input.
			pi_a_detached = pi_a.detach().clone().requires_grad_(True)

			#calculate the uncertainty and immediately backpropagate it to the action input to yield nabla_u
			bc_loss = F.mse_loss(pi_a_detached, action)

			bc_loss.backward()

			nabla_u = pi_a_detached.grad.clone().detach()

			#Clear policy action gradients
			pi_a_detached.grad = None
			self.critic.zero_grad()
			self.actor.zero_grad()
			self.critic_optimizer.zero_grad()
			self.actor_optimizer.zero_grad()


			q_avg = self.critic.Q1(state, pi_a_detached)
			q_avg.mean().backward()
			nabla_q = pi_a_detached.grad.clone().detach()

			with torch.no_grad():
				#average over batch
				cos_sim = F.cosine_similarity(nabla_u, nabla_q, dim=1).mean()
				norm_nabla_u = torch.norm(nabla_u, dim=1).mean()
				norm_nabla_q = torch.norm(nabla_q, dim=1).mean()
				self.gradient_info.append((main_timestep, \
						cos_sim.detach().cpu().item(), 
						norm_nabla_u.detach().cpu().item(),
						norm_nabla_q.detach().cpu().item()))

			# elif self.actor_update_rule == 'dQ_|_dU':
			# nabla_u = -nabla_u
			nabla_q = -nabla_q
			#now we have both nabla_u and nabla_q and we can turn to calculate the projection of q onto u
			dot_product = (nabla_q * nabla_u).sum(dim=1, keepdim=True)
			#increasing uncertainty, but we dont mind to decrease it)
			projection = (nabla_q * dot_product) / (nabla_q * nabla_q).sum(dim=1, keepdim=True)
			#the projection is required only when dot_product is positive (because care about avoiding 
			#first
			nabla_pi_constrained = nabla_u - projection * torch.logical_not(dot_product > 0)
			#second
			# nabla_pi_constrained = nabla_u - projection * (dot_product > 0)

			if self.total_it % 500 == 0:
				with torch.no_grad():
					norm_nabla_c = torch.norm(nabla_pi_constrained, dim=1).mean()
				print('norm_nabla_q: ', norm_nabla_q)
				print('norm_nabla_u: ', norm_nabla_u)
				print('norm_nabla_c: ', norm_nabla_c)
			# nabla_pi_constrained = -(nabla_q_constrained * pi_a).mean()
			# nabla_pi_constrained.backward()
			self.actor.zero_grad()
			self.critic.zero_grad()
			self.actor_optimizer.zero_grad()
			self.critic_optimizer.zero_grad()
			pi_a.backward(nabla_pi_constrained)
			
			self.actor_optimizer.step()

			for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
				target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)


	def save(self, filename):
		torch.save(self.critic.state_dict(), filename + "_critic")
		torch.save(self.critic_optimizer.state_dict(), filename + "_critic_optimizer")
		
		torch.save(self.actor.state_dict(), filename + "_actor")
		torch.save(self.actor_optimizer.state_dict(), filename + "_actor_optimizer")


	def load(self, filename):
		self.critic.load_state_dict(torch.load(filename + "_critic"))
		self.critic_optimizer.load_state_dict(torch.load(filename + "_critic_optimizer"))
		self.critic_target = copy.deepcopy(self.critic)

		self.actor.load_state_dict(torch.load(filename + "_actor"))
		self.actor_optimizer.load_state_dict(torch.load(filename + "_actor_optimizer"))
		self.actor_target = copy.deepcopy(self.actor)
				
	# def load_bc(self, filename):
		
	# 	self.actor.load_state_dict(torch.load(filename + "_actor"))
	# 	self.actor_target = copy.deepcopy(self.actor)

	def load_policy(self, filename):

		self.actor.load_state_dict(torch.load(filename + "_actor"))
		self.actor_target = copy.deepcopy(self.actor)
		