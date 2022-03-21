#!/bin/bash

for ((i=0;i<5;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "FetchPush-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../bc_models/Fetch_Push/push' \
	--results_dir '../results/FetchPush-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.01 \
	--start_percentile 0.5 \
	--log \
	--save_model \
	&

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "FetchPush-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../bc_models/Fetch_Push/push' \
	--results_dir '../results/FetchPush-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.001 \
	--start_percentile 0.5 \
	--log \
	--save_model \
	&

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "FetchPush-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../bc_models/Fetch_Push/push' \
	--results_dir '../results/FetchPush-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.0001 \
	--start_percentile 0.5 \
	--log \
	--save_model \

done