

import numpy as np
import torch
import gym
import argparse
import os

import utils
import TD3
from envs import init_env
from gym.utils import seeding

import pickle
from datetime import datetime

def eval_policy(policy, env_name, seed, eval_episodes=10):
	# eval_env = gym.make(env_name)
	eval_env = init_env(env_name)

	eval_env.seed(seed + 100)
	eval_env.np_random, _ = seeding.np_random(seed + 100)
	eval_env.action_space.seed(seed + 100)


	avg_reward = 0.
	for _ in range(eval_episodes):
		state, done = eval_env.reset(), False
		while not done:
			action = policy.select_action(np.array(state))
			state, reward, done, _ = eval_env.step(action)
			avg_reward += reward

	avg_reward /= eval_episodes

	print("---------------------------------------")
	print(f"Evaluation over {eval_episodes} episodes: {avg_reward:.3f}")
	print("---------------------------------------")
	return avg_reward

def boolean_feature(feature, default, help):

    global parser
    featurename = feature.replace("-", "_")
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--%s' % feature, dest=featurename, action='store_true', help=help)
    feature_parser.add_argument('--no-%s' % feature, dest=featurename, action='store_false', help=help)
    parser.set_defaults(**{featurename: default})

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--policy", default="TD3")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	parser.add_argument("--seed", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds
	parser.add_argument("--eval_freq", default=5e3, type=int)       # How often (time steps) we evaluate
	parser.add_argument("--start_timesteps", default=25e3, type=int)# Time steps initial random policy is used
	parser.add_argument("--max_timesteps", default=1e6, type=int)   # Max time steps to run environment
	parser.add_argument("--expl_noise", default=0.1)                # Std of Gaussian exploration noise
	parser.add_argument("--batch_size", default=256, type=int)      # Batch size for both actor and critic
	parser.add_argument("--discount", default=0.99)                 # Discount factor
	parser.add_argument("--tau", default=0.005, type=float)                     # Target network update rate
	parser.add_argument("--policy_noise", default=0.2)              # Noise added to target policy during critic update
	parser.add_argument("--noise_clip", default=0.5)                # Range to clip target policy noise
	parser.add_argument("--policy_freq", default=2, type=int)       # Frequency of delayed policy updates
	parser.add_argument("--log", action="store_true")        		# Save model and optimizer parameters
	parser.add_argument("--model_dir", default="")           # Save model and optimizer parameters
	parser.add_argument("--results_dir", default="")           # Save model and optimizer parameters
	parser.add_argument("--save_model", action="store_true")        # Save model and optimizer parameters
	parser.add_argument("--save_model_checkpoint", action="store_true")        # Save model and optimizer parameters
	parser.add_argument("--desired_performance", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds
	parser.add_argument("--save_replay_buffer", action="store_true")        	# Save model and optimizer parameters

	args = parser.parse_args()

	file_name = f"{args.policy}_{args.env}_{args.seed}_{args.desired_performance}"
	print("---------------------------------------")
	print(f"Policy: {args.policy}, Env: {args.env}, Seed: {args.seed}")
	print("---------------------------------------")
        
	if not os.path.exists(str(args.model_dir)):
		os.makedirs(str(args.model_dir))
	# if not os.path.exists(str(args.results_dir)):
	# 	os.makedirs(str(args.results_dir))

	experiment_args = {
		"policy": args.policy,
		"env": args.env,
		"seed": args.seed,
		"eval_freq": args.eval_freq,
		"start_timesteps": args.start_timesteps,
		"max_timesteps": args.max_timesteps,
		"expl_noise": args.expl_noise,
		"batch_size": args.batch_size,
		"discount": args.discount,
		"tau": args.tau,
		"policy_noise": args.policy_noise,
		"noise_clip": args.noise_clip,
		"policy_freq": args.policy_freq,
		"tau": args.tau,
		"desired_performance": args.desired_performance,
		"save_replay_buffer": args.save_replay_buffer,
	}
	if args.log:
		results_dir = os.path.join(str(args.results_dir),file_name)
		if not os.path.exists(results_dir):
			os.makedirs(results_dir)

		f = open(os.path.join(results_dir,'params.txt'), "w")
		for k, v in experiment_args.items():
			f.write(k +': ' + str(v) + '\n')
		f.close()


	# Set seeds
	import random
	from random import randint
	random.seed(args.seed)

	# Set seeds before init_env (env seeds set in init_env)
	torch.manual_seed(args.seed)
	torch.cuda.manual_seed(args.seed)
	torch.backends.cudnn.deterministic = True
	torch.backends.cudnn.enabled=False
	torch.backends.cudnn.benchmark = False
	np.random.seed(args.seed)

	# eval_env = gym.make(args.env)
	env = init_env(args.env)

	env.seed(args.seed)
	env.np_random, _ = seeding.np_random(args.seed)
	env.action_space.seed(args.seed)

	state_dim = env.observation_space.shape[0]
	action_dim = env.action_space.shape[0] 
	max_action = float(env.action_space.high[0])

	kwargs = {
		"state_dim": state_dim,
		"action_dim": action_dim,
		"max_action": max_action,
		"discount": args.discount,
		"tau": args.tau,
	}

	if args.policy == "TD3":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3.TD3(**kwargs)

	replay_buffer = utils.ReplayBuffer(state_dim, action_dim)
	
	# Evaluate untrained policy
	evaluations = [(0,eval_policy(policy, args.env, args.seed))]

	state, done = env.reset(), False
	episode_reward = 0
	episode_timesteps = 0
	episode_num = 0

	state_uncertainties = []
	for t in range(int(args.max_timesteps)):
		
		episode_timesteps += 1

		# Select action randomly or according to policy
		if t < args.start_timesteps:
			action = env.action_space.sample()
		else:
			action = \
				(policy.select_action(np.array(state))	
				+ np.random.normal(0, max_action * args.expl_noise, size=action_dim)
			).clip(-max_action, max_action)

		# Perform action
		next_state, reward, done, _ = env.step(action) 
		done_bool = float(done) if episode_timesteps < env._max_episode_steps else 0

		# Store data in replay buffer
		replay_buffer.add(state, action, next_state, reward, done_bool)

		state = next_state
		episode_reward += reward

		# Train agent after collecting sufficient data
		if t >= args.start_timesteps:
			policy.train(replay_buffer, args.batch_size)

		if done:
			# +1 to account for 0 indexing. +0 on ep_timesteps since it will increment +1 even if done=True
			print(f"Total T: {t+1} Episode Num: {episode_num+1} Episode T: {episode_timesteps} Reward: {episode_reward:.3f}")
			# Reset environment
			state, done = env.reset(), False
			episode_reward = 0
			episode_timesteps = 0
			episode_num += 1 

		# Evaluate episode
		if (t + 1) % args.eval_freq == 0:
			avg_reward = eval_policy(policy, args.env, args.seed)
			evaluations.append((t,avg_reward))
			if args.log:
				np.save(f"{results_dir}/evaluations_{file_name}", evaluations)
			if args.save_model:
				policy.save(f"{args.model_dir}")
			if args.save_model_checkpoint and (t + 1) % 20000 == 0:
				policy.save_actor(f"{args.model_dir}{file_name}_{t}")
			if avg_reward >= args.desired_performance:
				print('reach desired performance')
				import pickle
				with open(f"{args.model_dir}{file_name}", 'wb') as file_pi:
					pickle.dump(replay_buffer, file_pi)

				exit(1)
	print('reach end without desired performance')
	import pickle
	with open(f"{args.model_dir}{file_name}", 'wb') as file_pi:
		pickle.dump(replay_buffer, file_pi)

	exit(1)
