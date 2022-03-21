#!/bin/bash



CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3_learning_rate_scheduled" \
--env "HalfCheetah-v3" \
--max_timesteps 500000 \
--seed 0 \
--load_expert \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--learning_rate 0.0000003 \

# --log \
# &
