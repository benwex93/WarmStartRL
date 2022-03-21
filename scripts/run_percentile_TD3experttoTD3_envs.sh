#!/bin/bash

# for ((i=0;i<5;i+=1))
for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Ant-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/Ant-v3_results' \
	--start_update_policy 25000 \
	--log \
	--calculate_percentile \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--log \
	--calculate_percentile \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Hopper-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	--log \
	--calculate_percentile \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Humanoid-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/Humanoid-v3_results' \
	--start_update_policy 25000 \
	--log \
	--calculate_percentile \
	&

done
