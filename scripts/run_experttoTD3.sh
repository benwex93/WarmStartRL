#!/bin/bash

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3" \
--env "HalfCheetah-v3" \
--max_timesteps 200000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/HalfCheetah-v3_4K/BC_model' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
# &

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3" \
--env "Hopper-v3" \
--max_timesteps 200000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Hopper-v3_10K/BC_model' \
--results_dir '../results/Hopper-v3_results' \
--start_update_policy 25000 \
# &

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3" \
--env "Humanoid-v3" \
--max_timesteps 200000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Humanoid-v3/BC_model' \
--results_dir '../results/Humanoid-v3_results' \
--start_update_policy 25000 \
# &

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--log \
# &

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3" \
--env "FetchSlide-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchSlide-v1/BC_model' \
--results_dir '../results/FetchSlide-v1_results' \
--start_update_policy 25000 \
--log \
# &

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3" \
--env "FetchPickAndPlace-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchPickAndPlace-v1/BC_model' \
--results_dir '../results/FetchPickAndPlace-v1_results' \
--start_update_policy 25000 \
--log \
# &

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3" \
--env "Ant-v3" \
--max_timesteps 200000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Ant-v3/BC_model' \
--results_dir '../results/Ant-v3_results' \
--start_update_policy 25000 \
# &