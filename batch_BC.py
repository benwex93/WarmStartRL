import numpy as np
import torch
import gym
import argparse
import os

import BC
import utils
from envs import init_env
from gym.utils import seeding

def eval_policy(policy, env_name, seed, eval_episodes=10):
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

parser = argparse.ArgumentParser()
if __name__ == "__main__":
	
	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	boolean_feature("log", True, 'to log to tensorboard')
	parser.add_argument("--seed", default=0, type=int)              # Sets Gym, PyTorch and Numpy seeds

	parser.add_argument("--eval_freq", default=5e2, type=int)       # How often (time steps) we evaluate
	parser.add_argument("--max_timesteps", default=1e6, type=int)   # Max time steps to run environment
	parser.add_argument("--expl_noise", default=0.1)                # Std of Gaussian exploration noise
	parser.add_argument("--batch_size", default=256, type=int)      # Batch size for both actor and critic
	parser.add_argument("--discount", default=0.99)                 # Discount factor
	parser.add_argument("--tau", default=0.005)                     # Target network update rate
	parser.add_argument("--policy_noise", default=0.2)              # Noise added to target policy during critic update
	parser.add_argument("--noise_clip", default=0.5)                # Range to clip target policy noise
	parser.add_argument("--policy_freq", default=2, type=int)       # Frequency of delayed policy updates
	parser.add_argument("--expert_demo_file", default='')       # Frequency of delayed policy updates
	parser.add_argument("--save_model_dir", default='')       # Frequency of delayed policy updates
	parser.add_argument("--lr", default=0.0003, type=float)       # Frequency of delayed policy updates
	parser.add_argument("--save_model", action="store_true")        # Save model and optimizer parameters
	args = parser.parse_args()

	torch.manual_seed(args.seed)
	torch.cuda.manual_seed(args.seed)
	torch.backends.cudnn.deterministic = True
	torch.backends.cudnn.enabled=False
	torch.backends.cudnn.benchmark = False
	np.random.seed(args.seed)
	
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

	if args.log:
		experiment_args = {
			"env": args.env,
			"seed": args.seed,
			"eval_freq": args.eval_freq,
			"max_timesteps": args.max_timesteps,
			"expl_noise": args.expl_noise,
			"batch_size": args.batch_size,
			"discount": args.discount,
			"tau": args.tau,
			"policy_noise": args.policy_noise,
			"noise_clip": args.noise_clip,
			"policy_freq": args.policy_freq,
			"discount": args.discount,
			"tau": args.tau,
			"env_name": args.env,
			"lr": args.lr,
		}

	# Target policy smoothing is scaled wrt the action scale
	kwargs["policy_noise"] = args.policy_noise * max_action
	kwargs["noise_clip"] = args.noise_clip * max_action
	kwargs["policy_freq"] = args.policy_freq
	kwargs["lr"] = args.lr
	policy = BC.BC(**kwargs)

	demo_dir = '../expert_demos/'
	replay_buffer = None
	evaluations = []

	if not os.path.exists(args.save_model_dir):
		os.makedirs(args.save_model_dir)

	import pickle
	with open(os.path.join(args.expert_demo_file), 'rb') as filehandler: 
		replay_buffer = pickle.load(filehandler)
	# for filename in os.listdir(demo_dir):

	# 	if filename == args.expert_demo_dir:
	# 		with open(os.path.join(demo_dir,filename), 'rb') as filehandler: 
	# 			replay_buffer = pickle.load(filehandler)
	# file_name = f"{args.policy}_{args.env}"

	for t in range(int(args.max_timesteps)):
		# Train agent after collecting sufficient data
		policy.train(expert_replay_buffer=replay_buffer, batch_size=args.batch_size)
		if (t + 1) % args.eval_freq == 0:
			evaluations.append(\
				eval_policy(policy, args.env, args.seed))

		expert_name = str(args.expert_demo_file).split('/')[-1]
		if args.save_model:
			policy.save(f"{args.save_model_dir}/BC_model")
		if args.log:
			np.save(f"../results/{args.expert_demo_file}", evaluations)

