#!/bin/bash

for ((i=0;i<5;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--log \

done


