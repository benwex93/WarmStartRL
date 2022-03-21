#!/bin/bash

for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../q_avg_compare.py \
	--policy1 "TD3" \
	--policy2 "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--start_update_policy 25000 \
	--seed $i \
	--policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_equalSA_HalfCheetah-v3_0_10000' \
	--policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_equalSA_HalfCheetah-v3_0_10000' \
	--log \
	# &

	# CUDA_VISIBLE_DEVICES=2 python ../q_avg_compare.py \
	# --policy1 "TD3" \
	# --policy2 "TD3" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 500000 \
	# --start_update_policy 25000 \
	# --seed $i \
	# --with_q \
	# --policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	# --policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	# --log \

done
