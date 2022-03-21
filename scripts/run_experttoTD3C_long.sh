#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3C" \
--env "Ant-v3" \
--max_timesteps 10000000 \
--seed 0 \
--load_expert \
--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_3000' \
--results_dir '../results/Ant-v3_results' \
--start_update_policy 25000 \
--log \
--expl_noise 0.2 \

# --policy_noise 0.2 \
# --buffer_size 100000 \
# &
# # --expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_4000' \

# CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# --policy "TD3C" \
# --env "HalfCheetah-v3" \
# --max_timesteps 2000000 \
# --seed 0 \
# --load_expert \
# --log \
# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_3000' \
# --results_dir '../results/HalfCheetah-v3_results' \
# --start_update_policy 25000 \
# &
# # --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \

# CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# --policy "TD3C" \
# --env "Hopper-v3" \
# --max_timesteps 2000000 \
# --seed 0 \
# --load_expert \
# --log \
# --expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
# --results_dir '../results/Hopper-v3_results' \
# --start_update_policy 25000 \
# &
# # --expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_4000' \

# CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# --policy "TD3C" \
# --env "Humanoid-v3" \
# --max_timesteps 2000000 \
# --seed 0 \
# --load_expert \
# --log \
# --expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_3000' \
# --results_dir '../results/Humanoid-v3_results' \
# --start_update_policy 25000 \
# &
# # --expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_4000' \

# for ((i=1;i<5;i+=1))
# do 

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3C" \
# 	--env "Ant-v3" \
# 	--max_timesteps 2000000 \
# 	--seed $i \
# 	--load_expert \
# 	--expert_model '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_3000' \
# 	--results_dir '../results/Ant-v3_results' \
# 	--start_update_policy 25000 \
# 	--log \
# 	# &

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3C" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 2000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_3000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3C" \
# 	--env "Hopper-v3" \
# 	--max_timesteps 2000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_2000' \
# 	--results_dir '../results/Hopper-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3C" \
# 	--env "Humanoid-v3" \
# 	--max_timesteps 2000000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_3000' \
# 	--results_dir '../results/Humanoid-v3_results' \
# 	--start_update_policy 25000 \
# 	# &

# done
