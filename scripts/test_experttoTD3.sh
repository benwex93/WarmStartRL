#!/bin/bash


for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	# --log \

done
