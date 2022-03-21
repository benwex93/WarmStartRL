#!/bin/bash

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "Hopper-v3" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
--results_dir '../results/Hopper-v3_results' \
--start_update_policy 25000 \
--alpha 0.001 \
--start_percentile 0.5 \
--log \
&	

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3CCL_PQD" \
--env "Hopper-v3" \
--max_timesteps 1000000 \
--seed 0 \
--load_expert \
--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
--results_dir '../results/Hopper-v3_results' \
--start_update_policy 25000 \
--alpha 0.01 \
--start_percentile 0.5 \
--log \
&

# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# --policy "TD3CCL_PQD" \
# --env "Humanoid-v3" \
# --max_timesteps 1000000 \
# --seed 0 \
# --load_expert \
# --expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_2000' \
# --results_dir '../results/Humanoid-v3_results' \
# --start_update_policy 25000 \
# --alpha 0.0001 \
# --start_percentile 0.5 \
# --log \
# &
