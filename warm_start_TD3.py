

import numpy as np
import torch
import gym
import argparse
import os

import utils
import DDPG
import TD3
import TD3_fetch
import TD3_equalSA
import TD3C
import TD3CCL_BC
import TD3CCL_PQD
import TD3C2
import TD3_BC_Constraint
import TD3_BC_Constraint
import TD3_BC_Constraint_Scheduled
import TD3_BC_Uncertainty
import TD3_BC_Penalty
import TD3_BC_Pertubation
import TD3_gradient_clipping
import TD3_Gradient_Compare
import TD3_learning_rate
import TD3_learning_rate_scheduled
import TD3_warm_start
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

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--policy", default="TD3")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	parser.add_argument("--seed", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds
	parser.add_argument("--start_timesteps", default=25e3, type=int)# Time steps initial random policy is used
	parser.add_argument("--start_update_policy", default=0, type=int)# Time steps initial random policy is used
	parser.add_argument("--layer_width", default=256, type=int)		# Time steps initial random policy is used
	parser.add_argument("--eval_freq", default=5e3, type=int)       # How often (time steps) we evaluate
	parser.add_argument("--max_timesteps", default=1e6, type=int)   # Max time steps to run environment
	parser.add_argument("--expl_noise", default=0.1, type=float)                # Std of Gaussian exploration noise
	parser.add_argument("--batch_size", default=256, type=int)      # Batch size for both actor and critic
	parser.add_argument("--buffer_size", default=1000000, type=int)      # Batch size for both actor and critic
	parser.add_argument("--discount", default=0.99, type=float)                 # Discount factor
	parser.add_argument("--tau", default=0.005, type=float)                     # Target network update rate
	parser.add_argument("--dropout_rate", default=0.1, type=float)                     # Target network update rate
	parser.add_argument("--learning_rate", default=3e-4, type=float)                     # Target network update rate
	parser.add_argument("--gradient_clipping", default=3e-4, type=float)                     # Target network update rate
	parser.add_argument("--start_percentile", default=0.5, type=float)                     # Target network update rate
	parser.add_argument("--policy_noise", default=0.2)              # Noise added to target policy during critic update
	parser.add_argument("--noise_clip", default=0.5)                # Range to clip target policy noise
	parser.add_argument("--policy_freq", default=2, type=int)       # Frequency of delayed policy updates
	parser.add_argument("--log", action="store_true")        		# Save model and optimizer parameters
	parser.add_argument("--load_expert", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--load_expert_with_q", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--load_bc", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--load_buffer", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--load_buffer_loc", default="")        	# Save model and optimizer parameters
	parser.add_argument("--load_model_checkpoint", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--calculate_percentile", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--save_model", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--bc_model", default="")        	# Save model and optimizer parameters
	parser.add_argument("--expert_model", default="")        	# Save model and optimizer parameters
	parser.add_argument("--results_dir", default="")           # Save model and optimizer parameters
	parser.add_argument("--alpha", default=0.5, type=float)              # Noise added to target policy during critic update
	parser.add_argument("--steps_switch", default=50000, type=float)              # Noise added to target policy during critic update
	parser.add_argument("--actor_update_rule", default="")        	# Save model and optimizer parameters
	parser.add_argument("--save_steps", default=0, type=int)		# Time steps initial random policy is used
	args = parser.parse_args()

	file_name = f"{args.policy}_{args.env}_{args.seed}_{datetime.now()}"
	print("---------------------------------------")
	print(f"Policy: {args.policy}, Env: {args.env}, Seed: {args.seed}")
	print("---------------------------------------")
        
	if not os.path.exists(str(args.results_dir)):
                os.makedirs(str(args.results_dir))
	#if not os.path.exists("./results"):
	#	os.makedirs("./results")

	experiment_args = {
		"policy": args.policy,
		"env": args.env,
		"seed": args.seed,
		"start_timesteps": args.start_timesteps,
		"eval_freq": args.eval_freq,
		"max_timesteps": args.max_timesteps,
		"expl_noise": args.expl_noise,
		"batch_size": args.batch_size,
		"discount": args.discount,
		"tau": args.tau,
		"policy_noise": args.policy_noise,
		"noise_clip": args.noise_clip,
		"policy_freq": args.policy_freq,
		"start_update_policy": args.start_update_policy,
		"tau": args.tau,
		"dropout_rate": args.dropout_rate,
		"learning_rate": args.learning_rate,
		"gradient_clipping": args.gradient_clipping,
		"layer_width": args.layer_width,
		"actor_update_rule": args.actor_update_rule,
		"steps_switch": args.steps_switch,
		"load_bc": args.load_bc,
		"bc_model": args.bc_model,
		"load_expert": args.load_expert,
		"load_expert_with_q": args.load_expert_with_q,
		"expert_model": args.expert_model,
		"save_steps": args.save_steps,
		"alpha": args.alpha,
		"load_buffer": args.load_buffer,
	}
	if args.log:
		results_dir = os.path.join(str(args.results_dir),file_name+str(datetime.now()))
		if not os.path.exists(str(args.results_dir)):
			os.makedirs(str(args.results_dir))
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
		"start_update_policy": args.start_update_policy,
		"tau": args.tau,
	}

	if args.policy == "DDPG":
		# Target policy smoothing is scaled wrt the action scale
		policy = DDPG.DDPG(**kwargs)

	elif args.policy == "TD3":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["load_expert_with_q"] = args.load_expert_with_q
		policy = TD3.TD3(**kwargs)

	elif args.policy == "TD3_fetch":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["load_expert_with_q"] = args.load_expert_with_q
		policy = TD3_fetch.TD3_fetch(**kwargs)

	elif args.policy == "TD3_equalSA":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["load_expert_with_q"] = args.load_expert_with_q
		policy = TD3_equalSA.TD3_equalSA(**kwargs)

	elif args.policy == "TD3_gradient_clipping":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["gradient_clipping"] = args.gradient_clipping
		policy = TD3_gradient_clipping.TD3_gradient_clipping(**kwargs)

	elif args.policy == "TD3_Gradient_Compare":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["load_expert_with_q"] = args.load_expert_with_q
		policy = TD3_Gradient_Compare.TD3_Gradient_Compare(**kwargs)

	elif args.policy == "TD3_learning_rate":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["learning_rate"] = args.learning_rate
		policy = TD3_learning_rate.TD3_learning_rate(**kwargs)

	elif args.policy == "TD3_learning_rate_scheduled":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["learning_rate"] = args.learning_rate
		policy = TD3_learning_rate_scheduled.TD3_learning_rate_scheduled(**kwargs)

	elif args.policy == "TD3C":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["actor_update_rule"] = args.actor_update_rule
		kwargs["learning_rate"] = args.learning_rate
		policy = TD3C.TD3C(**kwargs)
	elif args.policy == "TD3C2":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3C2.TD3C2(**kwargs)
	elif args.policy == "TD3_BC_Constraint":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		policy = TD3_BC_Constraint.TD3_BC_Constraint(**kwargs)

	elif args.policy == "TD3_BC_Constraint_Scheduled":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		policy = TD3_BC_Constraint_Scheduled.TD3_BC_Constraint_Scheduled(**kwargs)

	elif args.policy == "TD3_BC_Uncertainty":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		kwargs["start_percentile"] = args.start_percentile
		policy = TD3_BC_Uncertainty.TD3_BC_Uncertainty(**kwargs)

	elif args.policy == "TD3CCL_PQD":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		kwargs["start_percentile"] = args.start_percentile
		policy = TD3CCL_PQD.TD3CCL_PQD(**kwargs)

	elif args.policy == "TD3CCL_BC":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		kwargs["start_percentile"] = args.start_percentile
		policy = TD3CCL_BC.TD3CCL_BC(**kwargs)

	elif args.policy == "TD3_BC_Pertubation":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		policy = TD3_BC_Pertubation.TD3_BC_Pertubation(**kwargs)

	elif args.policy == "TD3_BC_Penalty":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["alpha"] = args.alpha
		policy = TD3_BC_Penalty.TD3_BC_Penalty(**kwargs)	
	
	elif args.policy == "TD3_warm_start":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3_warm_start.TD3_warm_start(**kwargs)

	elif args.policy == "TD3UE_Dropout":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		kwargs["dropout_rate"] = args.dropout_rate
		kwargs["actor_update_rule"] = args.actor_update_rule
		kwargs["layer_width"] = args.layer_width
		kwargs["alpha"] = args.alpha
		policy = TD3UE_Dropout.TD3UE_Dropout(**kwargs)

	if args.load_bc:
		policy.load_policy(f'{args.bc_model}')		
	elif args.load_expert:
		policy.load_policy(f'{args.expert_model}')
	elif args.load_expert_with_q:
		policy.load(f'{args.expert_model}')
	elif args.load_model_checkpoint:
		policy.load_policy(f'{args.expert_model}_{args.save_steps}')

	replay_buffer = utils.ReplayBuffer(state_dim, action_dim, max_size=args.buffer_size)
	
	if args.load_buffer:
		import pickle
		with open(os.path.join(args.load_buffer_loc), 'rb') as filehandler: 
			replay_buffer = pickle.load(filehandler)
		print('loaded buffer')
	# Evaluate untrained policy

	evaluations = [(0,eval_policy(policy, args.env, args.seed))]

	if args.calculate_percentile:
		percentiles = []


	state, done = env.reset(), False
	episode_reward = 0
	episode_timesteps = 0
	episode_num = 0

	state_uncertainties = []
	for t in range(int(args.max_timesteps)):
		
		episode_timesteps += 1

		# Select action randomly or according to policy
		if not args.load_bc and not args.load_expert and not args.load_expert_with_q and t < args.start_timesteps:
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
			policy.train(replay_buffer, args.batch_size, t)

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
			evaluations.append((t,eval_policy(policy, args.env, args.seed)))

			if args.calculate_percentile:
				percentiles.append(policy.get_percentile(replay_buffer, args.batch_size))

			if args.log:
				np.save(f"{results_dir}/evaluations_{file_name}", evaluations)

				if args.calculate_percentile:
					np.save(f"{results_dir}/percentiles_{file_name}", percentiles)
				
				if args.save_model:
					policy.save(f"{results_dir}/model_{file_name}")
				# np.save(f"{results_dir}/state_uncertainties_{file_name}", policy.state_uncertainties)
				# np.save(f"{results_dir}/gradient_info_{file_name}", policy.gradient_info)

