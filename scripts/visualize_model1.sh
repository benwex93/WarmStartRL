#!/bin/bash

seed=1

# #ExpertPolicy
# #######################
# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchSlide-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../bc_models/Fetch_Slide/slide' \
# --movie_name 'FetchSlide_ExpertPolicy' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPush-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../bc_models/Fetch_Push/push' \
# --movie_name 'FetchPush_ExpertPolicy' \
# &

# CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPickAndPlace-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../bc_models/DetBC_FetchPickAndPlace-v1' \
# --movie_name 'FetchPickAndPlace_ExpertPolicy' \
# &

# CUDA_VISIBLE_DEVICES=3 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_10000' \
# --movie_name 'HalfCheetah10K_ExpertPolicy' \
# &

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
# --movie_name 'HalfCheetah4K_ExpertPolicy' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "Humanoid-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_2000' \
# --movie_name 'Humanoid_ExpertPolicy' \
# &


#CCL_PQD
#######################

CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
--policy "TD3" \
--env "FetchSlide-v1" \
--max_timesteps 1 \
--seed $seed \
--expert_model '../results/FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:24.7503682022-02-25 13:43:24.750601/model_TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:24.750368' \
--movie_name 'FetchSlide_CCL_PQD' \
&
#0.01
# --expert_model '../results/FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:37.1231412022-02-25 13:43:37.123218/model_TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:37.123141' \

CUDA_VISIBLE_DEVICES=3 python ../visualize_policy.py \
--policy "TD3" \
--env "FetchPush-v1" \
--max_timesteps 1 \
--seed $seed \
--movie_name 'FetchPush_CCL_PQD' \
--expert_model '../results/FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:29.9934402022-02-15 22:02:29.993525/model_TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:29.993440' \
&
#0.01
# --expert_model '../results/FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:25.9402272022-02-15 22:02:25.940467/model_TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:25.940227' \

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPickAndPlace-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:16.2669012022-02-27 00:07:16.267215/model_TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:16.266901' \
# --movie_name 'FetchPickAndPlace_CCL_PQD' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:26:28.5267822022-03-02 23:26:28.526974/model_TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:26:28.526782' \
# --movie_name 'HalfCheetah10K_CCL_PQD' \
# &

# CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:26:31.8707142022-03-02 23:26:31.870795/model_TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:26:31.870714' \
# --movie_name 'HalfCheetah4K_CCL_PQD' \
# &

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "Humanoid-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-03-02 23:24:29.7753552022-03-02 23:24:29.776156/model_TD3CCL_PQD_Humanoid-v3_0_2022-03-02 23:24:29.775355' \
# --movie_name 'Humanoid_CCL_PQD' \
# &

