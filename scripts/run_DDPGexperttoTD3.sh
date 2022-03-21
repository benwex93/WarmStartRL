#!/bin/bash


for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Half-Cheetah-v3_DDPG_BCQ_model/DDPG_HalfCheetah-v3_0_BCQ' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	# --expert_model '../models/HalfCheetah-v3_DDPG_model/DDPG_HalfCheetah-v3_0_15000' \

done
