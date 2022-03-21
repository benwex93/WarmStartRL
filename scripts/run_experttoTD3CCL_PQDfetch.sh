#!/bin/bash

for ((i=0;i<5;i+=1))
do 

	# CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "Hopper-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
	# --results_dir '../results/Hopper-v3_results' \
	# --start_update_policy 25000 \
	# --alpha 0.0001 \
	# --start_percentile 0.5 \
	# --log \
	# &

	# CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "Humanoid-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_2000' \
	# --results_dir '../results/Humanoid-v3_results' \
	# --start_update_policy 25000 \
	# --alpha 0.0001 \
	# --start_percentile 0.5 \
	# --log \
	# &

	# CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# --start_update_policy 25000 \
	# --alpha 0.01 \
	# --start_percentile 0.5 \
	# --log \
	# &

	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.001 \
	--start_percentile 0.5 \
	--log \
	&	

	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.0001 \
	--start_percentile 0.5 \
	--log \
	&

	# ###############
	# #10000
	# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# --start_update_policy 25000 \
	# --alpha 0.0001 \
	# --start_percentile 0.5 \
	# --log \
	# &

	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.001 \
	--start_percentile 0.5 \
	--log \
	&

	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	--policy "TD3CCL_PQD" \
	--env "HalfCheetah-v3" \
	--max_timesteps 1000000 \
	--seed $i \
	--load_expert \
	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
	--results_dir '../results/HalfCheetah-v3_results' \
	--start_update_policy 25000 \
	--alpha 0.01 \
	--start_percentile 0.5 \
	--log \
	&

	# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "HalfCheetah-v3" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../bc_models/BC_TD3_HalfCheetah-v3_0_4000_episodes:_101_states:_101000' \
	# --results_dir '../results/HalfCheetah-v3_results' \
	# --start_update_policy 25000 \
	# --alpha 0.01 \
	# --start_percentile 0.5 \
	# --log \
	# &


	# CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
	# --policy "TD3CCL_PQD" \
	# --env "FetchPickAndPlace-v1" \
	# --max_timesteps 1000000 \
	# --seed $i \
	# --load_expert \
	# --expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
	# --results_dir '../results/FetchPickAndPlace-v1_results' \
	# --start_update_policy 25000 \
	# --alpha 0.01 \
	# --start_percentile 0.5 \
	# --log \

done
