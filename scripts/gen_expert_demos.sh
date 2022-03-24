#!/bin/bash

CUDA_VISIBLE_DEVICES=1 python ../gen_expert_buff.py \
--env "HalfCheetah-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/HalfCheetah-v3_TD3_model_4K/' \
--replay_buffer_dir '../expert_demos/HalfCheetah-v3_TD3_model_4K/' \
# &

CUDA_VISIBLE_DEVICES=1 python ../gen_expert_buff.py \
--env "HalfCheetah-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/HalfCheetah-v3_TD3_model_10K/' \
--replay_buffer_dir '../expert_demos/HalfCheetah-v3_TD3_model_10K/' \
# &

CUDA_VISIBLE_DEVICES=2 python ../gen_expert_buff.py \
--env "Hopper-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/Hopper-v3_TD3_model/' \
--replay_buffer_dir '../expert_demos/Hopper-v3/' \
# &

CUDA_VISIBLE_DEVICES=3 python ../gen_expert_buff.py \
--env "Humanoid-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/Humanoid-v3_TD3_model/' \
--replay_buffer_dir '../expert_demos/Humanoid-v3/' \
# &

CUDA_VISIBLE_DEVICES=1 python ../gen_expert_buff.py \
--env "FetchPush-v1" \
--num_episodes 1001 \
--expl_noise 0.0 \
--replay_buffer_dir '../expert_demos/FetchPush-v1/' \
# &

CUDA_VISIBLE_DEVICES=2 python ../gen_expert_buff.py \
--env "FetchSlide-v1" \
--num_episodes 1001 \
--expl_noise 0.1 \
--replay_buffer_dir '../expert_demos/FetchSlide-v1/' \
# &

CUDA_VISIBLE_DEVICES=1 python ../gen_expert_buff.py \
--env "FetchPickAndPlace-v1" \
--num_episodes 101 \
--expl_noise 0.1 \
--replay_buffer_dir '../expert_demos/FetchPickAndPlace-v1/' \
# &

CUDA_VISIBLE_DEVICES=3 python ../gen_expert_buff.py \
--env "Ant-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/Ant-v3_TD3_model/' \
--replay_buffer_dir '../expert_demos/Ant-v3/' \
# &