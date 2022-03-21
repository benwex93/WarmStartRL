#!/bin/bash

# ################3
# for ((i=1;i<2;i+=1))
# do 
# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.000000003 \
# 	&
# 	# --max_timesteps 1000000 \

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.00000003 \
# 	&
# 	# --max_timesteps 1000000 \

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.0000003 \
# 	&
# 	# --max_timesteps 1000000 \

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.000003 \

# 	CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.00003 \

# 	CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.0003 \

# 	CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.003 \

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.03 \

# 	CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
# 	--policy "TD3_BC_Penalty" \
# 	--env "HalfCheetah-v3" \
# 	--max_timesteps 100000 \
# 	--seed $i \
# 	--load_expert \
# 	--log \
# 	--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# 	--results_dir '../results/HalfCheetah-v3_results' \
# 	--start_update_policy 25000 \
# 	--alpha 0.3 \
# 	# &
# 	# --max_timesteps 1000000 \
# done

################3
CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.000000003 \
&
# --max_timesteps 1000000 \

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.00000003 \
&
# --max_timesteps 1000000 \

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.0000003 \
&
# --max_timesteps 1000000 \

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.000003 \
&

CUDA_VISIBLE_DEVICES=0 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.00003 \
&

CUDA_VISIBLE_DEVICES=1 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.0003 \
&

CUDA_VISIBLE_DEVICES=2 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.003 \
&

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.03 \
&

CUDA_VISIBLE_DEVICES=3 python ../warm_start_TD3.py \
--policy "TD3_BC_Penalty" \
--env "HalfCheetah-v3" \
--max_timesteps 100000 \
--seed 0 \
--load_expert \
--log \
--expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
--results_dir '../results/HalfCheetah-v3_results' \
--start_update_policy 25000 \
--alpha 0.3 \
&

