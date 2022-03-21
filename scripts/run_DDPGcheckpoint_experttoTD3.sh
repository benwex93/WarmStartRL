#!/bin/bash


for ((i=1;i<21;i+=1))
do 
	let ss=$i*20000-1

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 80000 \
	--seed $i \
	--load_model_checkpoint \
	--log \
	--expert_model '../model_checkpoints/HalfCheetah-v3_DDPG_model/DDPG_HalfCheetah-v3_0_15000' \
	--results_dir '../results/HalfCheetah-v3_checkpoint_results' \
	--save_steps $ss \
	--start_update_policy 25000 \
	# --expert_model '../models/HalfCheetah-v3_DDPG_model/DDPG_HalfCheetah-v3_0_15000' \

done
