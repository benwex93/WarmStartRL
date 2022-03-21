#!/bin/bash


for ((i=0;i<5;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchSlide-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../bc_models/Fetch_Slide/slide' \
	--results_dir '../results/FetchSlide-v1_results' \
	--start_update_policy 25000 \
	--log \
	&

	# CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	# --policy "TD3" \
	# --env "FetchPush-v1" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../bc_models/Fetch_Push/push' \
	# --results_dir '../results/FetchPush-v1_results' \
	# --start_update_policy 25000 \
	# --log \
	# &

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "FetchPickAndPlace-v1" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	--results_dir '../results/FetchPickAndPlace-v1_results' \
	--start_update_policy 25000 \
	--log \
	&

done


