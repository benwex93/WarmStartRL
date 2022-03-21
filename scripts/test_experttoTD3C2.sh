#!/bin/bash


for ((i=0;i<1;i+=1))
do 

	# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	# --policy "TD3C2" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# --start_update_policy 25000 \
	# # --log \
	# # --start_update_policy 0 \
	# # --start_timesteps 0 \

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3C2" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	# --start_update_policy 0 \
	# --start_timesteps 0 \
	# --log \

done
