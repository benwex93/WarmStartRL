#!/bin/bash


CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3_learning_rate" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--learning_rate 0.0000003 \
# &

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3_learning_rate" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--learning_rate 0.000003 \
# &

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_learning_rate" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--learning_rate 0.00003 \
# &

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_learning_rate" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--learning_rate 0.0003 \
# &
