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
	def __init__(self, state_dim, action_dim):
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


class TD3CCL_PQD(object):
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
		alpha = 1,
		start_percentile = 0.5
	):

		self.actor = Actor(state_dim, action_dim, max_action).to(device)
		self.actor_target = copy.deepcopy(self.actor)
		self.actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=3e-4)

		self.critic = Critic(state_dim, action_dim).to(device)
		self.critic_target = copy.deepcopy(self.critic)
		self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=3e-4)

		self.start_update_policy = start_update_policy

		self.max_action = max_action
		self.discount = discount
		self.tau = tau
		self.policy_noise = policy_noise
		self.noise_clip = noise_clip
		self.policy_freq = policy_freq

		self.total_it = 0
		self.original_alpha = alpha
		print('self.original_alpha: ', self.original_alpha)
		self.alpha = alpha
		self.start_percentile = start_percentile

	def select_action(self, state):
		state = torch.FloatTensor(state.reshape(1, -1)).to(device)
		return self.actor(state).cpu().data.numpy().flatten()


	def train(self, replay_buffer, batch_size=100, main_timestep=0):
		self.total_it += 1

		# Sample replay buffer 
		state, action, next_state, reward, not_done = replay_buffer.sample(batch_size)
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

		# Get current Q estimates
		current_Q1, current_Q2 = self.critic(state, action)

		# Compute critic loss
		critic_loss = F.mse_loss(current_Q1, target_Q) + F.mse_loss(current_Q2, target_Q)

		# Optimize the critic
		self.critic_optimizer.zero_grad()
		critic_loss.backward()
		self.critic_optimizer.step()

		if self.total_it % 500 == 0:
			with torch.no_grad():
				num_action_samples = 500

				actions_repeat = action.unsqueeze(1).repeat(1,num_action_samples,1) #(256,1,6)-> #(256,500,6)
				random_uniform = ((torch.rand(actions_repeat.shape) * 2) -1).to(device)
				noise_actions = actions_repeat+random_uniform
				noise_actions = noise_actions.flatten(start_dim=0,end_dim=1) #(128000,6)

				states_repeat = state.unsqueeze(1).repeat(1,num_action_samples,1)
				states_repeat = states_repeat.flatten(start_dim=0,end_dim=1) #(128000,17)
				
				q_noise_vals = self.critic.Q1(states_repeat, noise_actions)
				q_noise_vals = q_noise_vals.view(-1, num_action_samples)

				q_vals = self.critic.Q1(state, action)
				percentile = torch.nonzero(q_vals > q_noise_vals).shape[0] / (num_action_samples * batch_size)
				print('percentile: ', percentile)

				if percentile < self.start_percentile:
					self.alpha = self.original_alpha
				else:
					alpha_exponent = \
							np.interp(percentile,[self.start_percentile,1.0],[np.log10(self.original_alpha),0.0])
					self.alpha = np.power(10, alpha_exponent)
					print('alpha_exponent: ', alpha_exponent)

				print('self.alpha: ', self.alpha)

		# Delayed policy updates
		if self.total_it > self.start_update_policy and \
			self.total_it % self.policy_freq == 0:

			#####################
			#BC_|_TD3 Calculate
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

			nabla_bc = pi_a_detached.grad.clone().detach()

			#Clear policy action gradients
			pi_a_detached.grad = None
			self.critic.zero_grad()
			self.actor.zero_grad()
			self.critic_optimizer.zero_grad()
			self.actor_optimizer.zero_grad()


			q_avg = self.critic.Q1(state, pi_a_detached)
			q_avg.mean().backward()
			nabla_q = pi_a_detached.grad.clone().detach()


			# want to increase q
			nabla_q = -nabla_q
			#now we have both nabla_u and nabla_q and we can turn to calculate the projection of q onto u
			dot_product = (nabla_q * nabla_bc).sum(dim=1, keepdim=True)
			#increasing uncertainty, but we dont mind to decrease it)
			projection = (nabla_q * dot_product) / (nabla_q * nabla_q).sum(dim=1, keepdim=True)
			#the projection is required only when dot_product is positive
			nabla_bc_perp_q = nabla_bc - projection * torch.logical_not(dot_product > 0)
			# get gradient remainder
			nabla_bc_parallel_q = nabla_q - nabla_bc_perp_q


			self.actor.zero_grad()
			self.critic.zero_grad()
			self.actor_optimizer.zero_grad()
			self.critic_optimizer.zero_grad()

			actor_gradient = nabla_bc_perp_q + (self.alpha) * nabla_bc_parallel_q

			if self.total_it % 500 == 0:
				with torch.no_grad():
					norm_nabla_q = torch.norm(nabla_q, dim=1).mean()
					norm_nabla_bc = torch.norm(nabla_bc, dim=1).mean()
					norm_nabla_perp = torch.norm(nabla_bc_perp_q, dim=1).mean()
					norm_nabla_parallel = torch.norm(nabla_bc_parallel_q, dim=1).mean()
					norm_nabla_actor_gradient = torch.norm(actor_gradient, dim=1).mean()
				print('norm_nabla_q: ', norm_nabla_q)
				print('norm_nabla_bc: ', norm_nabla_bc)
				print('norm_nabla_perp: ', norm_nabla_perp)
				print('norm_nabla_parallel: ', norm_nabla_parallel)
				print('norm_nabla_actor_gradient: ', norm_nabla_actor_gradient)

			pi_a.backward(actor_gradient)
			
			self.actor_optimizer.step()

			for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
				target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)

		if self.total_it % self.policy_freq == 0:
			# Update the frozen target models
			for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
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
		
	def load_policy(self, filename):

		self.actor.load_state_dict(torch.load(filename + "_actor"))
		self.actor_target = copy.deepcopy(self.actor)
		