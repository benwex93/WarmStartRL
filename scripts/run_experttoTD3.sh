#!/bin/bash

# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# --policy "TD3" \
# --env "FetchPush-v1" \
# --max_timesteps 1000000 \
# --seed 0 \
# --load_expert \
# --expert_model '../bc_models/Fetch_Push/push' \
# --results_dir '../results/FetchPush-v1_results' \
# --start_update_policy 25000 \
# --log \

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3" \
--env "FetchSlide-v1" \
--max_timesteps 1000000 \
--seed 1 \
--load_expert \
--expert_model '../bc_models/Fetch_Slide/slide' \
--results_dir '../results/FetchSlide-v1_results' \
--start_update_policy 25000 \
--log \

# for ((i=0;i<5;i+=1))
# do 

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Ant-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_3000' \
# 	--results_dir '../results/Ant-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_3000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Hopper-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
# 	--results_dir '../results/Hopper-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Humanoid-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_3000' \
# 	--results_dir '../results/Humanoid-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# done


# for ((i=0;i<5;i+=1))
# do 

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Ant-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert_with_q \
# 	--log \
# 	--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_4000' \
# 	--results_dir '../results/Ant-v3_results' \
# 	--start_update_policy 25000 \
# 	&

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert_with_q \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	&

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Hopper-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert_with_q \
# 	--log \
# 	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \
# 	--results_dir '../results/Hopper-v3_results' \
# 	--start_update_policy 25000 \
# 	&

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Humanoid-v3" \
# 	--max_timesteps 200000 \
# 	--seed $i \
# 	--load_expert_with_q \
# 	--log \
# 	--expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_4000' \
# 	--results_dir '../results/Humanoid-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# done




# for ((i=0;i<5;i+=1))
# do 

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Ant-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_2000' \
# 	--results_dir '../results/Ant-v3_results' \
# 	--start_update_policy 25000 \
# 	&

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Hopper-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
# 	--results_dir '../results/Hopper-v3_results' \
# 	--start_update_policy 25000 \
# 	&

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3" \
# 	--env "Humanoid-v3" \
# 	--max_timesteps 1000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_2000' \
# 	--results_dir '../results/Humanoid-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# done


