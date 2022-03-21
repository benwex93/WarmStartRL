#!/bin/bash

for ((i=1;i<5;i+=1))
do 
	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_gradient_clipping" \
	--env "Hopper-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	--gradient_clipping 0.000000003 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3_gradient_clipping" \
	--env "Hopper-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	--gradient_clipping 0.00000003 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_gradient_clipping" \
	--env "Hopper-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	--gradient_clipping 0.000003 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3_gradient_clipping" \
	--env "Hopper-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	--gradient_clipping 0.003 \
	# &

done
