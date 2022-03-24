#!/bin/bash


CUDA_VISIBLE_DEVICES=1 python ../batch_BC.py \
--env "HalfCheetah-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/HalfCheetah-v3_TD3_model_4K/BC_HalfCheetah-v3_rollout_episodes' \
--save_model \
--save_model_dir '../bc_models/HalfCheetah-v3_4K/' \
--max_timesteps 5000 \
# &

CUDA_VISIBLE_DEVICES=1 python ../batch_BC.py \
--env "HalfCheetah-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/HalfCheetah-v3_TD3_model_10K/BC_HalfCheetah-v3_rollout_episodes' \
--save_model \
--save_model_dir '../bc_models/HalfCheetah-v3_10K/' \
--max_timesteps 5000 \
# &

CUDA_VISIBLE_DEVICES=2 python ../batch_BC.py \
--env "Hopper-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/Hopper-v3/BC_Hopper-v3_rollout_episodes' \
--save_model_dir '../bc_models/Hopper-v3/' \
--save_model \
--max_timesteps 50000 \
# &

CUDA_VISIBLE_DEVICES=3 python ../batch_BC.py \
--env "Humanoid-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/Humanoid-v3/BC_Humanoid-v3_rollout_episodes' \
--save_model_dir '../bc_models/Humanoid-v3/' \
--save_model \
--max_timesteps 50000 \
# &

CUDA_VISIBLE_DEVICES=1 python batch_BC.py \
--policy 'DetBC' \
--env "FetchPush-v1" \
--lr 0.003 \
--expert_demo_dir '../expert_demos/FetchPush-v1/BC_FetchPush-v1_rollout_episodes' \
--save_model_dir '../bc_models/FetchPush-v1/' \
--save-model  \
--max_timesteps 50000 \
# &

CUDA_VISIBLE_DEVICES=1 python batch_BC.py \
--policy 'DetBC' \
--env "FetchSlide-v1" \
--lr 0.003 \
--expert_demo_dir '../expert_demos/FetchSlide-v1/BC_FetchSlide-v1_rollout_episodes' \
--save_model_dir '../bc_models/FetchSlide-v1/' \
--save-model  \
--max_timesteps 50000 \
# &

CUDA_VISIBLE_DEVICES=1 python batch_BC.py \
--policy 'DetBC' \
--env "FetchPickAndPlace-v1" \
--lr 0.003 \
--expert_demo_dir '../expert_demos/FetchPickAndPlace-v1/BC_FetchPickAndPlace-v1_rollout_episodes' \
--save_model_dir '../bc_models/FetchPickAndPlace-v1/' \
--save-model  \
--max_timesteps 50000 \
# &

CUDA_VISIBLE_DEVICES=0 python ../batch_BC.py \
--env "Ant-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/Ant-v3/BC_Ant-v3_rollout_episodes' \
--save_model \
--max_timesteps 50000 \
# &