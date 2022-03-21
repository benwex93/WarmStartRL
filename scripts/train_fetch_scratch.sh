#!/bin/bash

for ((i=0;i<5;i+=1))
do 

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchSlide-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/FetchSlide-v1_results' \
	--start_update_policy 25000 \
	--log \
	--save_model \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchPush-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--results_dir '../results/FetchPush-v1_results' \
	--start_update_policy 25000 \
	--log \
	--save_model

done