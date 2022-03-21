import gym
import numpy as np
import gym_fetch_stack
class DistanceWrapper(gym.Wrapper):
	def __init__(self, env, sparse):
		super().__init__(env)
		self.env = env
		self.sparse = sparse
	def step(self, action):
		next_state, reward, done, info = self.env.step(action)

		# modify ...
		achieved_goal = next_state['achieved_goal']
		goal = next_state['desired_goal']
		assert achieved_goal.shape == goal.shape
		# Compute distance between goal and the achieved goal.
		d = np.linalg.norm(achieved_goal - goal, axis=-1)

		# print(d)
		if self.sparse:
			reward = (d < 0.05).astype(np.float32)
		else:
			reward = -d

		return next_state, reward, done, info




import glfw
import gym
from types import MethodType
class PickPlaceWrapper(gym.Wrapper):
	def __init__(self, env):
		super().__init__(env)
		self.env = env
		self.env_timesteps = 1
		# self.env._max_episode_steps = 100

		self.distance_threshold = 0.08
	def step(self, action):

		next_state, reward, done, info = self.env.step(action)

		info = True
		# modify ...
		achieved_goal = next_state['achieved_goal']
		goal = next_state['desired_goal']
		assert achieved_goal.shape == goal.shape
		# Compute distance between goal and the achieved goal.
		d = np.linalg.norm(achieved_goal - goal, axis=-1)

		# print('env reward: ', reward)
		# print('caclutated distance: ', d)
		# if self.sparse:
		reward = -(d > self.distance_threshold).astype(np.float32)
		# print('caclutated reward: ', reward)
		# else:
		# 	reward = -d


		#makes sure not to start in done state and if does then exits so as to not bias
		if reward == 0 and self.env_timesteps == 1:
			reward = -1.0
			done = True
			info = False
		#+50 for no negatives
		elif self.env_timesteps < 100:
			done = False
		else:
			done = True
		self.env_timesteps+=1

		return next_state, reward + 1, done, info
	def close(self):
		if self.viewer is not None:
			glfw.destroy_window(self.viewer.window)
			self.viewer = None
	def reset(self):
		self.env_timesteps = 1
		return self.env.reset()

class SuccessWrapper(gym.Wrapper):
	def __init__(self, env):
		super().__init__(env)
		self.env = env
	def step(self, action):

		next_state, reward, done, info = self.env.step(action)

		#makes sure not to start in done state and if does then exits so as to not bias
		if reward == 0 and self.env_timesteps == 1:
			reward = -1.0
			done = True
			info = False
		# elif self.env_timesteps < 100:
		# 	done = False
		# else:
		# 	done = True
		self.env_timesteps+=1

		return next_state, reward + 1, done, info
	def close(self):
		if self.viewer is not None:
			glfw.destroy_window(self.viewer.window)
			self.viewer = None
	def reset(self):
		self.env_timesteps = 1
		return self.env.reset()

import cv2
cv2.ocl.setUseOpenCL(False)
import numpy as np
class Atari4FrameWrapper(gym.Wrapper):
	def __init__(self, env):
		super().__init__(env)
		self.env = env
		self.width = 84
		self.height = 84
		self.observation_space = gym.spaces.Box(low=0, high=255,
			shape=(1, 4, self.height, self.width), dtype=np.uint8)

	def observation(self, frame):
		frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
		frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
		return frame[:, :, None]

	def reset(self):

		frame = self.env.reset()
		frame = self.observation(frame)
		self.f1 = frame
		self.f2 = frame
		self.f3 = frame
		self.f4 = frame
		return np.stack((self.f1,self.f2,self.f3,self.f4), axis=0).transpose(3,0,1,2)

	def step(self, action):

		next_frame, reward, done, info = self.env.step(action)
		next_frame = self.observation(next_frame)

		self.f1 = self.f2
		self.f2 = self.f3
		self.f3 = self.f4
		self.f4 = next_frame
		next_state = np.stack((self.f1,self.f2,self.f3,self.f4), axis=0).transpose(3,0,1,2)
		return next_state, reward, done, info

from gym.utils import seeding
def init_env(env_name):
	env = gym.make(env_name)
	# import pdb
	# pdb.set_trace()
	#usually 4
	seed=4

	# #for fetch slide CCLPQD Final 40
	# seed=8

	env.seed(seed)
	env.np_random, seed = seeding.np_random(seed)
	env.action_space.seed(seed)


	if env_name == 'FetchReach-v1':

		env = DistanceWrapper(env, True)
		# env = DistanceWrapper(env, args.sparse)
		from gym.wrappers import FilterObservation, FlattenObservation
		env = FlattenObservation(FilterObservation(env, ['observation', 'desired_goal']))
		env._max_episode_steps = 100

	elif env_name == 'FetchPickAndPlace-v1' or env_name == 'FetchPush-v1' or env_name == 'FetchSlide-v1':
		
		env = PickPlaceWrapper(env)
		from gym.wrappers import FilterObservation, FlattenObservation
		env = FlattenObservation(FilterObservation(env, ['observation', 'desired_goal']))
		env._max_episode_steps = 100

	elif env_name in ['FetchStack4Stage3-v1', 'FetchStack4SparseStage3-v1']:
		
		env = SuccessWrapper(env)
		from gym.wrappers import FilterObservation, FlattenObservation
		env = FlattenObservation(FilterObservation(env, ['observation', 'desired_goal']))
		# env._max_episode_steps = 100

	elif env_name == 'MsPacmanNoFrameskip-v4':
		
		env = Atari4FrameWrapper(env)
		env._max_episode_steps = np.inf


	return env