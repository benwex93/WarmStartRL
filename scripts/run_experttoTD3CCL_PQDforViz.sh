#!/bin/bash

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "HalfCheetah-v3" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.01 \
--start_percentile 0.5 \
--log \
--save_model \
&

###############
#10000
CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "HalfCheetah-v3" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.0001 \
--start_percentile 0.5 \
--log \
--save_model \
&

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "Humanoid-v3" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_2000' \
--results_dir '../results/Humanoid-v3_results' \
--start_update_policy 25000 \
--alpha 0.0001 \
--start_percentile 0.5 \
--log \
--save_model \
&