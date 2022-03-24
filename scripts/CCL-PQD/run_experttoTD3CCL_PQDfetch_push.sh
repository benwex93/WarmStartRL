#!/bin/bash


CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.01 \
--start_percentile 0.5 \
--log \
# &

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.001 \
--start_percentile 0.5 \
--log \
# &

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../bc_models/FetchPush-v1/BC_model' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.0001 \
--start_percentile 0.5 \
--log \
# &

