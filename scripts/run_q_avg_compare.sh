#!/bin/bash

for ((i=0;i<1;i+=1))
do 
	# --policy1 "TD3UE_QEnsemble" \
	# --policy2 "TD3UE_QEnsemble" \
	# --get_uncertainty \
	# --policy1 "TD3C2" \
	# --policy2 "TD3C2" \

	
	# CUDA_VISIBLE_DEVICES=2 python ../q_avg_compare.py \
	# --policy1 "TD3" \
	# --policy2 "TD3" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 500000 \
	# --start_update_policy 25000 \
	# --seed $i \
	# --policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	# --policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	# --log \

	CUDA_VISIBLE_DEVICES=1 python ../q_avg_compare.py \
	--policy1 "TD3" \
	--policy2 "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--start_update_policy 25000 \
	--seed $i \
	--policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--log \
	&

	CUDA_VISIBLE_DEVICES=2 python ../q_avg_compare.py \
	--policy1 "TD3" \
	--policy2 "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--start_update_policy 25000 \
	--seed $i \
	--with_q \
	--policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--log \


	# --start_update_policy 25000 \

	# --with_q \
	# --policy1_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	# --policy2_file '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	# --rollout_p2 \
	# &

	# CUDA_VISIBLE_DEVICES=3 python uncertainty_compare.py \
	# --policy1 "TD3UE_Dropout2" \
	# --policy2 "TD3UE_Dropout2" \
	# --env "HalfCheetah-v3" \
	# --dropout_rate 0.25 \
	# --max_timesteps 500000 \
	# --start_update_policy 1000000 \
	# --tau 0.005 \
	# --layer_width 256 \
	# --seed $i \
	# --policy1_file 'BC_HalfCheetah-v3' \
	# --policy2_file 'BC_HalfCheetah-v3_9000' \
	# --log \
	# &

done
