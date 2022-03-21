

import numpy as np
import torch
import gym
import argparse
import os
import copy

import utils
import TD3
import TD3C2
import TD3_warm_start
import TD3UE_QEnsemble

from gym.utils import seeding
import torch.nn.functional as F

import pickle
from datetime import datetime
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_behavioral(policy2, env_name):

	new_env = gym.make(env_name)
	new_env.seed(100)
	new_env.np_random, _ = seeding.np_random(100)
	new_env.action_space.seed(100)

	episode_states = []
	episode_actions = []
	episode_reward = 0.
	state, done = new_env.reset(), False
	while not done:
		episode_states.append(state)
		a = policy2.select_action(np.array(state))
		episode_actions.append(a)
		state, reward, done, _ = new_env.step(a)
		episode_reward += reward

	print('get_behavioral_actions reward: ', episode_reward)

	return episode_states, episode_actions
def q_val(critic, states, actions):

	with torch.no_grad():

		q = critic.Q1(states, actions)
		return q.flatten().cpu().numpy()

def uncertainty_val(policy, states, actions):

	with torch.no_grad():

		Q_ensemble_value = [critic.Q1(states, actions) for critic in policy.critic_ensemble]

		Q_ensemble_value = torch.stack(Q_ensemble_value)
		min_q  = Q_ensemble_value.min(axis=0)[0]
		mu = Q_ensemble_value.mean(0, keepdim=True)
		uncertainty_estimation = ((Q_ensemble_value - mu) ** 2).mean(0) 
		#coefficient of variation (sigma/mu):

		uncertainty_estimation_score = (torch.sqrt(uncertainty_estimation) / torch.abs(mu))
		return uncertainty_estimation_score.flatten().cpu().numpy(), \
				uncertainty_estimation.flatten().cpu().numpy(), \
				mu.flatten().cpu().numpy(), \
				min_q.flatten().cpu().numpy()

# def projection_val(policy, states, optimal_actions, actions):

# 	with torch.no_grad():

# 		pi_a = policy.actor(states)

# 		copies = int(actions.shape[0]/optimal_actions.shape[0])
# 		optimal_actions_repeat = optimal_actions.unsqueeze(0).repeat(copies,1,1)
# 		optimal_actions_repeat = optimal_actions_repeat.transpose(0, 1)
# 		optimal_actions_repeat = optimal_actions_repeat.reshape((actions.shape[0], -1))

# 		bc = ((optimal_actions_repeat - actions)**2).sum(dim=1,keepdim=True)

# 		q = policy.critic.Q1(states, actions)

# 		#now we have both nabla_u and nabla_q and we can turn to calculate the projection of q onto u
# 		dot_product = (q * bc).sum(dim=1, keepdim=True)
# 		#increasing uncertainty, but we dont mind to decrease it)
# 		projection = (q * dot_product) / (q * q).sum(dim=1, keepdim=True)
# 		#the projection is required only when dot_product is positive (because care about avoiding 
# 		pi_constrained = bc - projection * (dot_product > 0)

# 		# return bc.flatten().cpu().numpy(), q.flatten().cpu().numpy(), pi_constrained.flatten().cpu().numpy()
# 		return pi_constrained.flatten().cpu().numpy()

def sample_gradient_norms(policy):
	if replay_buffer.size == 0:
		return None
	batch_size = 256

	states, _, _, _, _ = replay_buffer.sample(batch_size)

	pi_a = policy.actor(states)

	pi_a_detached = pi_a.detach().clone().requires_grad_(True)

	q_avg = policy.critic.Q1(states, pi_a_detached)
	q_avg.mean().backward()
	nabla_q = pi_a_detached.grad.clone().detach()
	policy.critic.zero_grad()
	policy.actor.zero_grad()

	with torch.no_grad():
		#average over batch
		norm_nabla_q = torch.norm(nabla_q, dim=1).mean()

		return norm_nabla_q.detach().cpu().numpy().item()

def compare_p2_to_p1_uncertainty(policy1, policy2, env_name, seed, eval_episodes=5, \
																		rollout_p2=False, get_uncertainty=False,
																		lagging_q=None):

	eval_env = gym.make(env_name)
	eval_env.seed(seed + 100)
	eval_env.np_random, _ = seeding.np_random(seed + 100)
	eval_env.action_space.seed(seed + 100)

	q = []
	states_actions = []
	avg_reward = 0.
	for _ in range(eval_episodes):
		state, done = eval_env.reset(), False
		episode_rewards = []
		episode_states = []
		episode_p1_actions = []
		episode_p2_actions = []
		while not done:
			episode_states.append(state)

			if rollout_p2:
				a = policy2.select_action(np.array(state))
				episode_p2_actions.append(a)
			else:
				a = policy1.select_action(np.array(state))
				episode_p1_actions.append(a)


			state, reward, done, _ = eval_env.step(a)
			episode_rewards.append(reward)
			avg_reward += reward

		episode_states = torch.FloatTensor(episode_states).to(device)

		if rollout_p2:
			episode_p2_actions = torch.FloatTensor(episode_p2_actions).to(device)
			episode_p1_actions = policy1.actor(episode_states).to(device)
		else:
			episode_p1_actions = torch.FloatTensor(episode_p1_actions).to(device)
			episode_p2_actions = policy2.actor(episode_states).to(device)

		# episode_random_actions = episode_p1_actions + torch.randn(episode_p1_actions.shape).to(device)
		# 		(policy1.select_action(np.array(state))	
		# + np.random.normal(0, max_action * args.expl_noise, size=action_dim)

		##################
		num_state_samples = 5
		num_action_samples = 500
		
		sample_idx = np.random.choice(episode_states.shape[0], num_state_samples, replace=False)

		sampled_states = episode_states[sample_idx] #(5,17)
		sampled_states_repeat = sampled_states.unsqueeze(1).repeat(1,num_action_samples,1) # (5,1,17) -> (5,500,17)
		sampled_states_repeat = sampled_states_repeat.flatten(start_dim=0,end_dim=1) #(2500,17)
		
		p1_a_samples = episode_p1_actions[sample_idx] #(5,6)
		p1_a_samples_repeat = p1_a_samples.unsqueeze(1).repeat(1,num_action_samples,1) #(5,1,6) -> (5,500,6)
		p1_a_samples_repeat = p1_a_samples_repeat.flatten(start_dim=0,end_dim=1) #(2500,6)

		random_uniform = ((torch.rand(p1_a_samples_repeat.shape) * 2) -1).to(device)
		episode_p1_noise_actions = p1_a_samples_repeat+random_uniform
		# episode_p1_noise_actions = (p1_samples+torch.randn(p1_samples.shape).to(device)).clamp(-1, 1)

		p2_a_samples = episode_p2_actions[sample_idx]
		p2_a_samples_repeat = p2_a_samples.unsqueeze(1).repeat(1,num_action_samples,1) #(5,1,6)-> #(5,500,6)
		p2_a_samples_repeat = p2_a_samples_repeat.flatten(start_dim=0,end_dim=1) #(2500,6)

		random_uniform = ((torch.rand(p2_a_samples_repeat.shape) * 2) -1).to(device)
		episode_p2_noise_actions = p2_a_samples_repeat+random_uniform
		# episode_p2_noise_actions = (p2_samples+torch.randn(p2_samples.shape).to(device)).clamp(-1, 1)
		
		episode_random_actions = torch.FloatTensor(
					[env.action_space.sample() for _ in range(episode_states.shape[0])]).to(device)


		episode_random_states = episode_states + torch.randn(episode_states.shape).to(device)

		lagging_a1_s1_q = None
		lagging_a2_s1_q = None
		lagging_aR_s1_q = None
		lagging_aB_sU_q = None
		lagging_aU_sB_q = None
		if lagging_q:
			print('lagging_q')
			lagging_a1_s1_q = q_val(lagging_q, episode_states, episode_p1_actions)
			lagging_a2_s1_q  = q_val(lagging_q, episode_states, episode_p2_actions)
			lagging_aR_s1_q  = q_val(lagging_q, episode_states, episode_random_actions)

			behavioral_states, behavioral_actions = get_behavioral(policy2, env_name)
			behavioral_states = torch.FloatTensor(behavioral_states).to(device)
			behavioral_actions = torch.FloatTensor(behavioral_actions).to(device)
			lagging_aB_sU_q  = q_val(lagging_q, episode_states, behavioral_actions)
			lagging_aU_sB_q  = q_val(lagging_q, behavioral_states, episode_p1_actions)


		a1_s1_q = q_val(policy1.critic, episode_states, episode_p1_actions)
		a2_s1_q  = q_val(policy1.critic, episode_states, episode_p2_actions)

		aR_s1_q  = q_val(policy1.critic, episode_states, episode_random_actions)
		a1_sR_q  = q_val(policy1.critic, episode_random_states, episode_p1_actions)
		aR_sR_q  = q_val(policy1.critic, episode_random_states, episode_random_actions)

		a1R_s1_q = q_val(policy1.critic, sampled_states_repeat, episode_p1_noise_actions)
		a2R_s1_q  = q_val(policy1.critic, sampled_states_repeat, episode_p2_noise_actions)

		a1S_s1_q  = q_val(policy1.critic, sampled_states, p1_a_samples)
		a2S_s1_q  = q_val(policy1.critic, sampled_states, p2_a_samples)

		q_grad_norm = sample_gradient_norms(policy1)
		print('q_grad_norm: ', q_grad_norm)

		if get_uncertainty:
			a1R_s1_u  = uncertainty_val(policy1, sampled_states_repeat, episode_p1_noise_actions)
			a2R_s1_u  = uncertainty_val(policy1, sampled_states_repeat, episode_p2_noise_actions)
			a1S_s1_u  = uncertainty_val(policy1, sampled_states, p1_a_samples)
			a2S_s1_u  = uncertainty_val(policy1, sampled_states, p2_a_samples)
		else:
			a1R_s1_u, a2R_s1_u, a1S_s1_u, a2S_s1_u = None, None, None, None

		q.append((episode_rewards,
					a1_s1_q, a2_s1_q,
					aR_s1_q, a1_sR_q, aR_sR_q,
					a1R_s1_q, a2R_s1_q, 
					a1S_s1_q, a2S_s1_q,
					a1R_s1_u, a2R_s1_u,
					a1S_s1_u, a2S_s1_u,
					lagging_a1_s1_q,
					lagging_a2_s1_q,
					lagging_aR_s1_q,
					lagging_aB_sU_q,
					lagging_aU_sB_q,
					q_grad_norm))

		states_actions.append((episode_states, episode_p1_actions, episode_p2_actions,
								episode_random_actions, episode_random_states,
								episode_p1_noise_actions, episode_p2_noise_actions,
								p1_a_samples, p2_a_samples))

	avg_reward /= eval_episodes

	print("---------------------------------------")
	print(f"Evaluation over {eval_episodes} episodes: {avg_reward:.3f}")
	print("---------------------------------------")
	return (q, states_actions)

def init_policy(policy_type, policy_file, kwargs, with_Q=False):
	if policy_type == "TD3":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3.TD3(**kwargs)
	elif policy_type == "TD3_warm_start":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3_warm_start.TD3_warm_start(**kwargs)
	elif policy_type == "TD3UE_QEnsemble":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3UE_QEnsemble.TD3UE_QEnsemble(**kwargs)
	elif policy_type == "TD3C2":
		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = args.policy_noise * max_action
		kwargs["noise_clip"] = args.noise_clip * max_action
		kwargs["policy_freq"] = args.policy_freq
		policy = TD3C2.TD3C2(**kwargs)

	if with_Q:
		policy.load(f'{policy_file}')
	else:
		policy.load_policy(f'{policy_file}')

	return policy


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--policy1", default="TD3")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--policy2", default="TD3")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--policy1_file", default="")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--policy2_file", default="")                  # Policy name (TD3, DDPG or OurDDPG)
	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	parser.add_argument("--seed", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds
	parser.add_argument("--start_timesteps", default=25e3, type=int)# Time steps initial random policy is used
	parser.add_argument("--start_update_policy", default=25e3, type=int)# Time steps initial random policy is used
	parser.add_argument("--layer_width", default=256, type=int)		# Time steps initial random policy is used
	parser.add_argument("--eval_freq", default=5e3, type=int)       # How often (time steps) we evaluate
	parser.add_argument("--max_timesteps", default=1e6, type=int)   # Max time steps to run environment
	parser.add_argument("--expl_noise", default=0.1)                # Std of Gaussian exploration noise
	parser.add_argument("--batch_size", default=256, type=int)      # Batch size for both actor and critic
	parser.add_argument("--discount", default=0.99)                 # Discount factor
	parser.add_argument("--tau", default=0.005, type=float)                     # Target network update rate
	parser.add_argument("--dropout_rate", default=0.1, type=float)                     # Target network update rate
	parser.add_argument("--policy_noise", default=0.2)              # Noise added to target policy during critic update
	parser.add_argument("--noise_clip", default=0.5)                # Range to clip target policy noise
	parser.add_argument("--policy_freq", default=2, type=int)       # Frequency of delayed policy updates
	parser.add_argument("--log", action="store_true")        		# Save model and optimizer parameters
	parser.add_argument("--with_q", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--rollout_p2", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--get_uncertainty", action="store_true")        	# Save model and optimizer parameters
	parser.add_argument("--alpha", default=0.5)              # Noise added to target policy during critic update
	parser.add_argument("--actor_update_rule", default="")        	# Save model and optimizer parameters
	args = parser.parse_args()

	file_name = f"{args.policy1}_{args.policy2}_{args.env}_{args.seed}_{datetime.now()}"
	print("---------------------------------------")
	print(f"Policy1: {args.policy1}, Policy2: {args.policy2}, Env: {args.env}, Seed: {args.seed}")
	print("---------------------------------------")

	if not os.path.exists("../q_val_compare"):
		os.makedirs("../q_val_compare")

	experiment_args = {
		"policy1": args.policy1,
		"policy2": args.policy2,
		"policy1_file": args.policy1_file,
		"policy2_file": args.policy2_file,
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
		"with_q": args.with_q,
		"rollout_p2": args.rollout_p2,
		"layer_width": args.layer_width,
		"actor_update_rule": args.actor_update_rule,
		"get_uncertainty": args.get_uncertainty,
	}
	if args.log:
		results_dir = os.path.join('../q_val_compare/',file_name+str(datetime.now()))
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

	env = gym.make(args.env)
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
	print('with_q: ', args.with_q)
	print('rollout_p2: ', args.rollout_p2)
	# policy1 = init_policy(args.policy1, args.policy1_file, kwargs)
	policy1 = init_policy(args.policy1, args.policy1_file, kwargs, with_Q=args.with_q)
	policy2 = init_policy(args.policy2, args.policy2_file, kwargs)

	replay_buffer = utils.ReplayBuffer(state_dim, action_dim)

	state, done = env.reset(), False
	episode_reward = 0
	episode_timesteps = 0
	episode_num = 0

	(ep_q, ep_states_actions) = compare_p2_to_p1_uncertainty(policy1, policy2, args.env, args.seed, \
		rollout_p2=args.rollout_p2, get_uncertainty=args.get_uncertainty)
	q = [ep_q]
	states_actions = [ep_states_actions]

	lagging_q=None
	for t in range(int(args.max_timesteps)):
		
		episode_timesteps += 1

		# Select action randomly or according to policy
		# if t < args.start_timesteps:
		# 	action = env.action_space.sample()
		# else:
		action = \
			(policy1.select_action(np.array(state))	
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
			if lagging_q is None and t >= (args.start_timesteps + args.start_update_policy):
				print('saving lagging q')
				lagging_q = copy.deepcopy(policy1.critic)
			policy1.train(replay_buffer, args.batch_size, t)

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
			(ep_q, ep_states_actions) = compare_p2_to_p1_uncertainty(policy1, policy2, args.env, args.seed, \
				rollout_p2=args.rollout_p2, get_uncertainty=args.get_uncertainty, lagging_q=lagging_q)
			q.append(ep_q)
			states_actions.append(ep_states_actions)
			if args.log:
				np.save(f"{results_dir}/q_{file_name}", q)
				np.save(f"{results_dir}/states_actions_{file_name}", states_actions)

