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


class BC(object):
	def __init__(
		self,
		state_dim,
		action_dim,
		max_action,
		lr,
		discount=0.99,
		tau=0.005,
		policy_noise=0.2,
		noise_clip=0.5,
		policy_freq=2
	):

		self.actor = Actor(state_dim, action_dim, max_action).to(device)
		self.bc_actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=lr)

		self.max_action = max_action
		self.discount = discount
		self.tau = tau
		self.policy_noise = policy_noise
		self.noise_clip = noise_clip
		self.policy_freq = policy_freq

		self.total_it = 0


	def select_action(self, state):
		with torch.no_grad():
			state = torch.FloatTensor(state.reshape(1, -1)).to(device)
			action = self.actor(state).cpu().data.numpy().flatten()

			return action

	def train(self, expert_replay_buffer, batch_size=100):
		self.total_it += 1

		state, action, next_state, reward, not_done = \
													expert_replay_buffer.sample(batch_size)
		# # Compute BC losse
		bc_loss = (F.mse_loss(self.actor(state), action) * not_done).mean()


		# #Expert policy update
		# with torch.no_grad():
		# 	noise = (
		# 		torch.randn_like(action) * self.policy_noise
		# 	).clamp(-self.noise_clip, self.noise_clip)
		# 	action = (
		# 		action + csil_noise
		# 	).clamp(-self.max_action, self.max_action)

		# with torch.no_grad():
		# 	noise = (
		# 		torch.randn_like(next_action) * self.policy_noise
		# 	).clamp(-self.noise_clip, self.noise_clip)
		# 	next_action = (
		# 		next_action + noise
		# 	).clamp(-self.max_action, self.max_action)


		# # Compute BC losse
		# bc_loss = (F.mse_loss(self.actor(state), csil_action)  * not_done).mean() + \
		# 	(F.mse_loss(self.actor(next_state), csil_next_action)  * not_done).mean()
		
		if self.total_it % 500 == 0:
			print(bc_loss)
		
		# Optimize the actor 
		self.bc_actor_optimizer.zero_grad()
		bc_loss.backward()
		self.bc_actor_optimizer.step()

	def save(self, filename):
		torch.save(self.actor.state_dict(), filename + "_actor")

	def load(self, filename):
		self.critic.load_state_dict(torch.load(filename + "_critic"))
		self.critic_optimizer.load_state_dict(torch.load(filename + "_critic_optimizer"))
		self.critic_target = copy.deepcopy(self.critic)

		self.actor.load_state_dict(torch.load(filename + "_actor"))
		self.actor_optimizer.load_state_dict(torch.load(filename + "_actor_optimizer"))
		self.actor_target = copy.deepcopy(self.actor)
		