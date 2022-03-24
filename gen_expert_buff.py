import numpy as np
import gym
import argparse
import os

import utils

from envs import init_env
from env_experts import init_expert

def boolean_feature(feature, default, help):

    global parser
    featurename = feature.replace("-", "_")
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--%s' % feature, dest=featurename, action='store_true', help=help)
    feature_parser.add_argument('--no-%s' % feature, dest=featurename, action='store_false', help=help)
    parser.set_defaults(**{featurename: default})

parser = argparse.ArgumentParser()
if __name__ == "__main__":
	boolean_feature("log", True, 'to log to tensorboard')

	parser.add_argument("--env", default="HalfCheetah-v2")          # OpenAI gym environment name
	parser.add_argument("--expert_model_dir", default="")          # OpenAI gym environment name
	parser.add_argument("--replay_buffer_dir", default="")          # OpenAI gym environment name
	parser.add_argument("--num_episodes", default=1e4, type=int)   # Max time steps to run environment
	parser.add_argument("--discount", default=0.99)                 # Discount factor
	parser.add_argument("--expl_noise", type=float, default=0)                # Std of Gaussian exploration noise
	args = parser.parse_args()


	if not os.path.exists(str(args.replay_buffer_dir)):
		os.makedirs(str(args.replay_buffer_dir))

	env = init_env(args.env)
	state_dim = env.observation_space.shape[0]

	action_dim = env.action_space.shape[0]
	max_action = float(env.action_space.high[0])

	replay_buffer = utils.ReplayBuffer(state_dim, action_dim)

	expert = init_expert(args.env, args.expl_noise, args.expert_model_dir)

	evaluations = []
	overall_states = 0
	for t in range(int(args.num_episodes)):

		ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool = expert.play_episode()
			
		if ep_state == ep_actions == ep_next_state == ep_reward == ep_done_bool == None:
			continue

		if sum(ep_reward) > 0:
			print(replay_buffer.size)
			replay_buffer.add_episode( \
				ep_state, ep_actions, ep_next_state, ep_reward, ep_done_bool)

		overall_states += len(ep_state)

		evaluations.append(sum(ep_reward))
		# +1 to account for 0 indexing. +0 on ep_timesteps since it will increment +1 even if done=True
		print(f"Total states: {overall_states} Episode Num: {t+1} Episode T: Reward: {sum(ep_reward):.3f}")

	# file_name = f"episodes:_{t+1}_states:_{overall_states}"
	file_name = f"{args.env}_rollout_episodes"


	expert_name = str(args.expert_model_dir).split('/')[-1]
	save_location = os.path.join(f"{args.replay_buffer_dir}",f"BC{expert_name}_{file_name}")

	import pickle

	with open(save_location, 'wb') as file_pi:
		pickle.dump(replay_buffer, file_pi)
	# if args.log:
	# 	np.save(f"{args.replay_buffer_dir}{file_name}", evaluations)
