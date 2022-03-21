import numpy as np
import torch
import gym
import argparse
import os

import utils
import TD3
from envs import init_env
from env_experts import init_expert
from moviepy.editor import ImageSequenceClip
# ep_num_to_save = 0

def eval_policy(policy, env_name, seed, num_env_it, dl=None, eval_episodes=10, movie_name='sample'):


	eval_env = init_env(env_name)
	# eval_env = wrappers.Monitor(eval_env, os.getcwd(), force=True)
	avg_reward = 0.
	gif = []
	frames = 0
	# rate = 10
	rate = 0
	for episode_num in range(eval_episodes):
		state, done = eval_env.reset(), False
		episode_reward = 0
		while not done:
			action = policy.select_action(np.array(state))
			# if episode_num == 0:
			if episode_num >= 0:
				# frames+=1
				# if frames % rate == 0:
				arr = eval_env.render(mode='rgb_array')
				gif.append(arr)

			state, reward, done, _ = eval_env.step(action) 

			avg_reward += reward

			episode_reward += reward
		# if episode_num == 0:
		if episode_num ==9:
			# clip = ImageSequenceClip(gif, fps=5)
			clip = ImageSequenceClip(gif, fps=20)
			current_avg = avg_reward / (episode_num + 1)
			clip.write_videofile(os.path.join(os.getcwd(),'../videos/'+movie_name+' '+str(current_avg)+ '.mp4')) 
			return


	avg_reward /= eval_episodes
	if dl:
		tb_scalar_log = {'avg_10_episode_reward':avg_reward }
		dl.tb_scalar_logger(tb_scalar_log, num_env_it) 

	if env_name != 'FetchPickAndPlace-v1' and env_name != 'FetchPush-v1' and env_name != 'FetchSlide-v1':
		eval_env.env.close()

	print("---------------------------------------")
	print(f"Evaluation over {eval_episodes} episodes: {avg_reward:.3f}")
	print("---------------------------------------")
	return avg_reward
from random import randint
# def eval_policy(policy, env_name, seed, num_env_it, dl=None, eval_episodes=10):


# 	eval_env = init_env(env_name)
# 	# eval_env = wrappers.Monitor(eval_env, os.getcwd(), force=True)
# 	avg_reward = 0.
# 	gif = []
# 	frames = 0
# 	rate = 10
# 	value = randint(0, 10)
# 	for episode_num in range(eval_episodes):
# 		state, done = eval_env.reset(), False
# 		episode_reward = 0
# 		while not done:
# 			action = policy.select_action(np.array(state))
# 			if episode_num == value:
# 				# print(action)
# 				frames+=1
# 				if frames % rate == 0:
# 					arr = np.flip(eval_env.env.sim.render(600,600))
# 					# arr = eval_env.render(mode='rgb_array')
# 					gif.append(arr)
# 					pass

# 			state, reward, done, _ = eval_env.step(action) 

# 			avg_reward += reward

# 			episode_reward += reward
# 		if episode_num == value and len(gif) > 0:
# 			clip = ImageSequenceClip(gif, fps=5)
# 			clip.write_videofile(os.path.join(os.getcwd(),'sample.mp4')) 



# 	avg_reward /= eval_episodes
# 	if dl:
# 		tb_scalar_log = {'avg_10_episode_reward':avg_reward }
# 		dl.tb_scalar_logger(tb_scalar_log, num_env_it) 

# 	if env_name != 'FetchPickAndPlace-v1':
# 		eval_env.env.close()

# 	print("---------------------------------------")
# 	print(f"Evaluation over {eval_episodes} episodes: {avg_reward:.3f}")
# 	print("---------------------------------------")
# 	return avg_reward


def boolean_feature(feature, default, help):

    global parser
    featurename = feature.replace("-", "_")
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--%s' % feature, dest=featurename, action='store_true', help=help)
    feature_parser.add_argument('--no-%s' % feature, dest=featurename, action='store_false', help=help)
    parser.set_defaults(**{featurename: default})

parser = argparse.ArgumentParser()
if __name__ == "__main__":
	
	parser.add_argument("--policy", default="TD3")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	boolean_feature("log", True, 'to log to tensorboard')
	parser.add_argument("--seed", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds

	parser.add_argument("--max_timesteps", default=1e6, type=int)   # Max time steps to run environment
	parser.add_argument("--expert_model", default='')       # Frequency of delayed policy updates
	parser.add_argument("--movie_name", default='')       # Frequency of delayed policy updates
	args = parser.parse_args()

	# Set seeds before init_env (env seeds set in init_env)
	# env.seed(args.seed)
	# env.action_space.seed(args.seed)
	torch.manual_seed(args.seed)
	torch.cuda.manual_seed(args.seed)
	torch.backends.cudnn.deterministic = True
	torch.backends.cudnn.enabled=False
	torch.backends.cudnn.benchmark = False
	np.random.seed(args.seed)
	
	env = init_env(args.env)

	state_dim = env.observation_space.shape[0]

	action_dim = env.action_space.shape[0]
	max_action = float(env.action_space.high[0])



	kwargs = {
		"state_dim": state_dim,
		"action_dim": action_dim,
		"max_action": max_action,
	}

	if args.policy == "TD3":
		# Target policy smoothing is scaled wrt the action scale
		policy = TD3.TD3(**kwargs)

	policy.load_policy(f'{args.expert_model}')

	file_name = f"{args.policy}_{args.env}"
	for t in range(int(args.max_timesteps)):
		eval_policy(policy, args.env, args.seed, num_env_it=(t + 1), movie_name=args.movie_name)
		# if args.log:
		# 	np.save(f"./results/{file_name}", evaluations)

