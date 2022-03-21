#!/bin/bash


for ((i=0;i<1;i+=1))
do 

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Ant-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_bc \
	--log \
	--bc_model '../bc_models/BC_TD3_Ant-v3_0_1000_episodes:_101_states:_85736' \
	--results_dir '../results/Ant-v3_results' \
	--start_update_policy 25000 \
	&

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "HalfCheetah-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_bc \
	--log \
	--bc_model '../bc_models/BC_TD3_HalfCheetah-v3_0_4000_episodes:_101_states:_101000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	&

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Hopper-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_bc \
	--log \
	--bc_model '../bc_models/BC_TD3_Hopper-v3_0_1000_episodes:_101_states:_28960' \
	--results_dir '../results/Hopper-v3_results' \
	--start_update_policy 25000 \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3" \
	--env "Humanoid-v3" \
	--max_timesteps 500000 \
	--seed $i \
	--load_bc \
	--log \
	--bc_model '../bc_models/BC_TD3_Humanoid-v3_0_1000_episodes:_101_states:_21036' \
	--results_dir '../results/Humanoid-v3_results' \
	--start_update_policy 25000 \
	&

done
