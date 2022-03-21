#!/bin/bash

# for ((i=1;i<5;i+=1))
# do 

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3_learning_rate" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--learning_rate 0.0000003 \
# 	&

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3_learning_rate" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--learning_rate 0.000003 \
# 	&

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3_learning_rate" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--learning_rate 0.00003 \
# 	&

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3_learning_rate" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--learning_rate 0.0003

# done

# for ((i=1;i<5;i+=1))
for ((i=1;i<2;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3_learning_rate" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--learning_rate 0.0000003 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3_learning_rate" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--learning_rate 0.000003 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3_learning_rate" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--learning_rate 0.00003 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3_learning_rate" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--log \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--learning_rate 0.0003

done