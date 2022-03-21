#!/bin/bash


for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3C" \
	--env "HalfCheetah-v3" \
	--max_timesteps 2000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--learning_rate 0.0003 \
	# --log \
	# --start_update_policy 0 \
	# --start_timesteps 0 \

	# CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	# --policy "TD3C" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 2000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# --start_update_policy 25000 \
	# # --log \
	# # --start_update_policy 0 \
	# # --start_timesteps 0 \

done
