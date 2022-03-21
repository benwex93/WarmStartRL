#!/bin/bash

for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=1 python ../train_behavioral.py \
	--policy "TD3" \
	--env "Humanoid-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--log \
	--results_dir '../results/Humanoid-v3_results/' \
	--model_dir '../models/Humanoid-v3_TD3_model/' \
	--save_model \
	--desired_performance 4000 \
	--save_replay_buffer \
	# --desired_performance 15000 \
	# &

done
