#!/bin/bash


for ((i=0;i<5;i+=1))
do 

	# CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	# --policy "TD3" \
	# --env "Ant-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --log \
	# --results_dir '../results/Ant-v3_results' \
	# &

	# CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	# --policy "TD3" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --log \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# # &

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Ant-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_4000' \
	--results_dir '../results/Ant-v3_results' \
	--start_update_policy 25000 \
	# &



done
