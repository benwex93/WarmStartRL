#!/bin/bash

################3
CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3_BC_Pertubation" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Fetch_Push/push' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.01 \
&

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_BC_Pertubation" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Fetch_Push/push' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.1 \
&

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_BC_Pertubation" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Fetch_Push/push' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.25 \
&

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Pertubation" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Fetch_Push/push' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 0.2 \
&

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Pertubation" \
--env "FetchPush-v1" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../bc_models/Fetch_Push/push' \
--results_dir '../results/FetchPush-v1_results' \
--start_update_policy 25000 \
--alpha 1 \
&