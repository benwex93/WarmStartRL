#!/bin/bash

################3
for ((i=1;i<5;i+=1))
do 
	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.01 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.1 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.25 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.2 \
	&

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 1 \
	# &
done


for ((i=1;i<5;i+=1))
do 
	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.01 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.1 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.25 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.2 \
	&

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_BC_Pertubation" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 1 \
	# &
done