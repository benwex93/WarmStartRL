#!/bin/bash

for ((i=1;i<5;i+=1))
do 
	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_BC_Constraint" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.0001 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3_BC_Constraint" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.01 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_BC_Constraint" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.1 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_BC_Constraint" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--alpha 0.5 \
	# 
done