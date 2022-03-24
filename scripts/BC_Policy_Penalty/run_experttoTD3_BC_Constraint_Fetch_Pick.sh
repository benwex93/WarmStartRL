#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3_BC_Constraint" \
--env "FetchPickAndPlace-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPickAndPlace-v1/BC_model' \
--results_dir '../results/FetchPickAndPlace-v1_results' \
--start_update_policy 25000 \
--alpha 0.0001 \
# &

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3_BC_Constraint" \
--env "FetchPickAndPlace-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPickAndPlace-v1/BC_model' \
--results_dir '../results/FetchPickAndPlace-v1_results' \
--start_update_policy 25000 \
--alpha 0.01 \
# &

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_BC_Constraint" \
--env "FetchPickAndPlace-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPickAndPlace-v1/BC_model' \
--results_dir '../results/FetchPickAndPlace-v1_results' \
--start_update_policy 25000 \
--alpha 0.1 \
# &

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Constraint" \
--env "FetchPickAndPlace-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/FetchPickAndPlace-v1/BC_model' \
--results_dir '../results/FetchPickAndPlace-v1_results' \
--start_update_policy 25000 \
--alpha 0.5 \
# &
