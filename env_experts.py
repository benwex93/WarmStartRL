from envs import DistanceWrapper, PickPlaceWrapper, init_env
import numpy as np
import gym

# from fetch_stack_expert import FetchStackExpert

#REQUIRES GYM==0.15.4!!!!
#DOESNT WORK with gym==0.17.2
def init_expert(env_name, expl_noise, policy_file=None):
	expert = None

	if env_name == 'FetchReach-v1':	
		expert = FetchReachExpert()

	elif env_name == 'FetchPickAndPlace-v1':
		expert_env = gym.make(env_name)
		expert_env = PickPlaceWrapper(expert_env)
		expert_env._max_episode_steps = 100
		expert = FetchPickPlaceExpert(expert_env)

	elif env_name == 'FetchSlide-v1':
		expert_env = gym.make(env_name)
		expert_env = PickPlaceWrapper(expert_env)
		expert_env._max_episode_steps = 100
		expert = FetchSlideExpert(expert_env)

	elif env_name == 'FetchPush-v1':
		expert_env = gym.make(env_name)
		expert_env = PickPlaceWrapper(expert_env)
		expert_env._max_episode_steps = 100
		expert = FetchPushExpert(expert_env)

	elif env_name in ['FetchStack4Stage3-v1', 'FetchStack4SparseStage3-v1']:
		expert_env = gym.make(env_name)
		# expert_env = PickPlaceWrapper(expert_env)
		# expert_env._max_episode_steps = 100
		expert = FetchStackExpert(expert_env)


	elif env_name == 'FetchSlide-v1':	
		pass

	elif env_name in ["HalfCheetah-v3", "Hopper-v3", "Walker2d-v3", "Ant-v3", "Humanoid-v3", "InvertedPendulum-v2", \
							"InvertedDoublePendulum-v2", "Reacher-v2", "LunarLanderContinuous-v2"]:
		env = init_env(env_name)
		expert = ClassicMujocoExpert(env, env_name, policy_file)
	expert.expl_noise = expl_noise
	return expert

class FetchReachExpert():
	def __init__(self):
		pass
	def select_action(self, state):

		# state = old_state.cpu().detach().numpy()
		gripperPos = state[:3]
		#GOAL DOES NOT CHANGE AFTER REWINDING STATE BUT GRIPPER POS DOES
		goal = state[10:13]


		episode_timesteps = 0 #count the total number of timesteps

		object_oriented_goal = (goal-gripperPos)

		# if np.linalg.norm(object_oriented_goal) >= 0.05 or episode_timesteps < self.env._max_episode_steps:
		# 	#env.render()

		action = [0, 0, 0, 0]
		object_oriented_goal = (goal-gripperPos)

		for i in range(len(object_oriented_goal)):
			action[i] = object_oriented_goal[i]*6

		return action

class FetchSlideExpert():
	def __init__(self, env):
		self.env = env
		self.env.reset()

		self.state_dim = self.env.observation_space['observation'].shape[0]
		self.action_dim = self.env.action_space.shape[0]
		self.max_action = float(env.action_space.high[0])

	def go_above_cube(self, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = object_rel_pos.copy()
		object_oriented_goal[2] += 0.12

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)

		while np.linalg.norm(object_oriented_goal) >= 0.005 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			object_oriented_goal = object_rel_pos.copy()
			object_oriented_goal[2] += 0.12

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy
	def go_to_side_of_cube(self, side, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = object_rel_pos.copy()

		if side == 'front':
			object_oriented_goal[0] += 0.07		
		elif side == 'back':
			object_oriented_goal[0] -= 0.07
		elif side == 'right':
			object_oriented_goal[1] += 0.07
		elif side == 'left':
			object_oriented_goal[1] -= 0.07

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)

		while np.linalg.norm(object_oriented_goal) >= 0.01 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			# print(np.linalg.norm(object_oriented_goal))
			object_oriented_goal = object_rel_pos.copy()
			if side == 'front':
				object_oriented_goal[0] += 0.07		
			elif side == 'back':
				object_oriented_goal[0] -= 0.07
			elif side == 'right':
				object_oriented_goal[1] += 0.07
			elif side == 'left':
				object_oriented_goal[1] -= 0.07

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy
	def push_side_of_cube(self, side, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = (goal - gripperPos).copy()
		# object_oriented_goal = (goal - objectPos).copy()

		if side == 'back' or side == 'front':
			object_oriented_goal[1] = 0	
		elif side == 'right' or side == 'left':
			object_oriented_goal[0] = 0
		object_oriented_goal[2] = 0

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)


		while np.linalg.norm(object_oriented_goal) >= 0.01 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]
			object_oriented_goal = (goal - gripperPos).copy()
			# object_oriented_goal = (goal - objectPos).copy()

			if side == 'back' or side == 'front':
				object_oriented_goal[1] = 0		
			elif side == 'right' or side == 'left':
				object_oriented_goal[0] = 0
			object_oriented_goal[2] = 0	

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy

	def play_episode(self):

		ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool = [],[],[],[],[]
		
		state = self.env.reset()
		self.timeStep = 0

		state = self.go_above_cube(state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)

		if not state:
			return None, None, None, None, None

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		if (goal-objectPos)[0] > 0.01: 
			state = self.go_to_side_of_cube('back', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			
			state = self.push_side_of_cube('back', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			

		ep_done_bool[-1] = 1
		return ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool

class FetchPushExpert():
	def __init__(self, env):
		self.env = env
		self.env.reset()

		self.state_dim = self.env.observation_space['observation'].shape[0]
		self.action_dim = self.env.action_space.shape[0]
		self.max_action = float(env.action_space.high[0])

	def go_above_cube(self, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = object_rel_pos.copy()
		object_oriented_goal[2] += 0.12

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)

		while np.linalg.norm(object_oriented_goal) >= 0.005 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			object_oriented_goal = object_rel_pos.copy()
			object_oriented_goal[2] += 0.12

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy
	def go_to_side_of_cube(self, side, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = object_rel_pos.copy()

		if side == 'front':
			object_oriented_goal[0] += 0.07		
		elif side == 'back':
			object_oriented_goal[0] -= 0.07
		elif side == 'right':
			object_oriented_goal[1] += 0.07
		elif side == 'left':
			object_oriented_goal[1] -= 0.07

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)

		while np.linalg.norm(object_oriented_goal) >= 0.005 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			object_oriented_goal = object_rel_pos.copy()
			if side == 'front':
				object_oriented_goal[0] += 0.07		
			elif side == 'back':
				object_oriented_goal[0] -= 0.07
			elif side == 'right':
				object_oriented_goal[1] += 0.07
			elif side == 'left':
				object_oriented_goal[1] -= 0.07

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy
	def push_side_of_cube(self, side, state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool):

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]

		object_oriented_goal = (goal - gripperPos).copy()
		# object_oriented_goal = (goal - objectPos).copy()

		if side == 'back' or side == 'front':
			object_oriented_goal[1] = 0	
		elif side == 'right' or side == 'left':
			object_oriented_goal[0] = 0
		object_oriented_goal[2] = 0

		next_state_copy = state.copy()
		state = np.append(state['observation'], goal)

		while np.linalg.norm(object_oriented_goal) >= 0.01 and self.timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]
			# print(np.linalg.norm(object_oriented_goal))
			object_oriented_goal = (goal - gripperPos).copy()
			# object_oriented_goal = (goal - objectPos).copy()

			if side == 'back' or side == 'front':
				object_oriented_goal[1] = 0		
			elif side == 'right' or side == 'left':
				object_oriented_goal[0] = 0
			object_oriented_goal[2] = 0	

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None

			done_bool = float(done) if self.timeStep < self.env._max_episode_steps else 0.0

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state_copy = next_state.copy()
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)

			state = next_state
			self.timeStep += 1

		return next_state_copy

	def play_episode(self):

		ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool = [],[],[],[],[]
		
		state = self.env.reset()
		self.timeStep = 0

		state = self.go_above_cube(state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)

		if not state:
			return None, None, None, None, None

		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		if (goal-objectPos)[0] > 0.01: 
			state = self.go_to_side_of_cube('back', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			
			state = self.push_side_of_cube('back', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			

		state = self.go_above_cube(state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		if (goal-objectPos)[0] < -0.01:
			state = self.go_to_side_of_cube('front', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
			state = self.push_side_of_cube('front', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			

		state = self.go_above_cube(state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		if (goal-objectPos)[1] > 0.01:
			state = self.go_to_side_of_cube('left', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
			state = self.push_side_of_cube('left', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			

		state = self.go_above_cube(state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
		goal = state['desired_goal']
		objectPos = state['observation'][3:6]
		if (goal-objectPos)[1] < -0.01:
			state = self.go_to_side_of_cube('right', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)
			state = self.push_side_of_cube('right', state, ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)			


		ep_done_bool[-1] = 1
		return ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool

class FetchPickPlaceExpert():
	def __init__(self, env):
		self.env = env
		self.env.reset()

		self.state_dim = self.env.observation_space['observation'].shape[0]
		self.action_dim = self.env.action_space.shape[0]
		self.max_action = float(env.action_space.high[0])
	def play_episode(self):

		state = self.env.reset()

		# goal = state['observation'][25:28]
		goal = state['desired_goal']

		#objectPosition
		objectPos = state['observation'][3:6]
		gripperPos = state['observation'][:3]
		object_rel_pos = state['observation'][6:9]


		object_oriented_goal = (goal-gripperPos)
		object_oriented_goal[2] += 0.03

		timeStep = 0

		ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool, ep_saved_state = \
																			[],[],[],[],[],[]
		

		state = np.append(state['observation'], goal)
		
		while np.linalg.norm(object_oriented_goal) >= 0.005 and timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			object_oriented_goal = object_rel_pos.copy()
			object_oriented_goal[2] += 0.03

			for i in range(len(object_oriented_goal)):
				action[i] = object_oriented_goal[i]*6

			action[len(action)-1] = 0.05

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			
			if info is False:
				print('bad episode')
				return None, None, None, None, None



			done_bool = float(done) if timeStep < self.env._max_episode_steps else 0.0

			timeStep += 1
			
			#saved_state = self.env.sim.get_state().flatten().copy()
			saved_state = None

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)
			ep_saved_state.append(saved_state)

			state = next_state


		while np.linalg.norm(object_rel_pos) >= 0.005 and timeStep <= self.env._max_episode_steps :
			# self.env.render()
			action = [0, 0, 0, 0]



			for i in range(len(object_rel_pos)):
				action[i] = object_rel_pos[i]*6

			action[len(action)-1] = -0.05

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)
			done_bool = float(done) if timeStep < self.env._max_episode_steps else 0.0

			timeStep += 1


			#saved_state = self.env.sim.get_state().flatten().copy()
			saved_state = None
			
			
			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]

			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)
			ep_saved_state.append(saved_state)

			state = next_state



		while np.linalg.norm(goal - objectPos) >= 0.01 and timeStep <= self.env._max_episode_steps :
			# self.env.render()
			action = [0, 0, 0, 0]



			for i in range(len(goal - objectPos)):
				action[i] = (goal - objectPos)[i]*6

			action[len(action)-1] = -0.05

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)

			done_bool = float(done) if timeStep < self.env._max_episode_steps else 0.0

			timeStep += 1

			#saved_state = self.env.sim.get_state().flatten().copy()
			saved_state = None

			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]

			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)
			ep_saved_state.append(saved_state)

			state = next_state


		while timeStep <= self.env._max_episode_steps:
			# self.env.render()
			action = [0, 0, 0, 0]

			action[len(action)-1] = -0.05

			action = (
				action
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			next_state, reward, done, info = self.env.step(action)

			reward = 1.0

			done_bool = float(done) if timeStep < self.env._max_episode_steps else 0.0

			timeStep += 1


			#saved_state = self.env.sim.get_state().flatten().copy()
			saved_state = None
			
			
			objectPos = next_state['observation'][3:6]
			gripperPos = next_state['observation'][:3]
			object_rel_pos = next_state['observation'][6:9]
			
			#set goal to correct one since loading state in mujoco only loads robot positions 
			next_state = np.append(next_state['observation'], goal)

			ep_state.append(state)
			ep_actions.append(action)
			ep_next_state.append(next_state)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)
			ep_saved_state.append(saved_state)

			state = next_state



			# if timeStep >= self.env._max_episode_steps: break
		# print(sum(ep_reward))
		saved_state = [None for _ in ep_state]
		ep_done_bool[-1] = 1
		return ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool
import TD3
class ClassicMujocoExpert():
	def __init__(self, env, env_name, policy_file):
		self.env = env
		self.env.reset()
		self.state_dim = self.env.observation_space.shape[0]
		self.action_dim = self.env.action_space.shape[0]
		self.max_action = float(env.action_space.high[0])
		# self.expl_noise = 

		kwargs = {
			"state_dim": self.state_dim,
			"action_dim": self.action_dim,
			"max_action": self.max_action,
			"discount": 0,
			"tau": 0,
		}

		if 'TD3' in policy_file:
			self.policy = TD3.TD3(**kwargs)
			self.policy.load(f"{policy_file}")

		else:
			print('no policy selected')
			exit(-1)
	def play_episode(self):

		state = self.env.reset()

		ep_state, ep_action, ep_next_state, ep_reward, ep_done_bool, ep_saved_state = \
															[],[],[],[],[],[]
		
		episode_timesteps = 0
		done=False


		# while not done:
		while not done and episode_timesteps < self.env._max_episode_steps:

			episode_timesteps += 1

			# action = self.policy.select_action(np.array(state))

			action = (
				self.policy.select_action(np.array(state))
				+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
			).clip(-self.max_action, self.max_action)

			# Perform action
			next_state, reward, done, _ = self.env.step(action) 
			done_bool = float(done) if episode_timesteps < self.env._max_episode_steps else 0

			ep_state.append(state)
			ep_action.append(action)
			ep_next_state.append(next_state)
			ep_saved_state.append(None)
			ep_reward.append(reward)
			ep_done_bool.append(done_bool)


			state = next_state

		# Store data in replay buffer
		print('expert reward:', sum(ep_reward))

		# new_discounted_return = csil_replay_buffer.get_episode_discounted_return(ep_reward, discount_factor)

		# print('old_discounted_return: ', old_discounted_return[0])
		# print('new_discounted_return: ', new_discounted_return[0])


		# corrected=False
		# if new_discounted_return[0] > old_discounted_return[0]:
		# 	csil_replay_buffer.add_episode( \
		# 	ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool, ep_saved_state, \
		# 	new_discounted_return)
		# 	corrected = True
		# return corrected
		ep_done_bool[-1] = 1
		return ep_state, ep_action, ep_next_state, ep_reward, ep_done_bool

