#!/bin/bash

seed=1

#Warm-Start Degradation
#######################
# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchSlide-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/FetchSlide-v1_results/TD3_FetchSlide-v1_0_2022-03-02 23:32:57.3847812022-03-02 23:32:57.385009/model_TD3_FetchSlide-v1_0_2022-03-02 23:32:57.384781' \
# --movie_name 'FetchSlide_TD3_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPush-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/FetchPush-v1_results/TD3_FetchPush-v1_0_2022-03-02 23:32:57.9643282022-03-02 23:32:57.964730/model_TD3_FetchPush-v1_0_2022-03-02 23:32:57.964328' \
# --movie_name 'FetchPush_TD3_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPickAndPlace-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_0_2022-03-02 23:32:57.8417762022-03-02 23:32:57.842129/model_TD3_FetchPickAndPlace-v1_0_2022-03-02 23:32:57.841776' \
# --movie_name 'FetchPickAndPlace_TD3_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=3 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2022-03-02 23:32:53.1985692022-03-02 23:32:53.198659/model_TD3_HalfCheetah-v3_0_2022-03-02 23:32:53.198569' \
# --movie_name 'HalfCheetah10K_TD3_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2022-03-02 23:32:57.5538762022-03-02 23:32:57.553957/model_TD3_HalfCheetah-v3_0_2022-03-02 23:32:57.553876' \
# --movie_name 'HalfCheetah4K_TD3_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "Humanoid-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/Humanoid-v3_results/TD3_Humanoid-v3_0_2022-03-02 23:32:57.2358342022-03-02 23:32:57.235910/model_TD3_Humanoid-v3_0_2022-03-02 23:32:57.235834' \
# --movie_name 'Humanoid_TD3_AfterUpdate' \
# &


#CCL_PQD without Degradation
#######################

CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
--policy "TD3" \
--env "FetchSlide-v1" \
--max_timesteps 1 \
--seed $seed \
--expert_model '../results/FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-03-03 17:23:36.7875362022-03-03 17:23:36.788411/model_TD3CCL_PQD_FetchSlide-v1_0_2022-03-03 17:23:36.787536' \
--movie_name 'FetchSlide_CCL_PQD_AfterUpdate' \
&
#0.01
# --expert_model '../results/FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-03-02 23:33:28.4805762022-03-02 23:33:28.480891/model_TD3CCL_PQD_FetchSlide-v1_0_2022-03-02 23:33:28.480576' \

CUDA_VISIBLE_DEVICES=3 python ../visualize_policy.py \
--policy "TD3" \
--env "FetchPush-v1" \
--max_timesteps 1 \
--seed $seed \
--expert_model '../results/FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-03-03 17:23:36.9167272022-03-03 17:23:36.917148/model_TD3CCL_PQD_FetchPush-v1_0_2022-03-03 17:23:36.916727' \
--movie_name 'FetchPush_CCL_PQD_AfterUpdate' \
&
#0.01
# --expert_model '../results/FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-03-02 23:33:28.0957592022-03-02 23:33:28.095997/model_TD3CCL_PQD_FetchPush-v1_0_2022-03-02 23:33:28.095759' \

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "FetchPickAndPlace-v1" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-03-03 16:17:52.5009642022-03-03 16:17:52.502117/model_TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-03-03 16:17:52.500964' \
# --movie_name 'FetchPickAndPlace_CCL_PQD_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=1 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:33:25.0167252022-03-02 23:33:25.017261/model_TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:33:25.016725' \
# --movie_name 'HalfCheetah10K_CCL_PQD_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=2 python ../visualize_policy.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/HalfCheetah-v3_results/TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:33:28.2519972022-03-02 23:33:28.252081/model_TD3CCL_PQD_HalfCheetah-v3_0_2022-03-02 23:33:28.251997' \
# --movie_name 'HalfCheetah4K_CCL_PQD_AfterUpdate' \
# &

# CUDA_VISIBLE_DEVICES=0 python ../visualize_policy.py \
# --policy "TD3" \
# --env "Humanoid-v3" \
# --max_timesteps 1 \
# --seed $seed \
# --expert_model '../results/Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-03-03 15:19:55.5252412022-03-03 15:19:55.525638/model_TD3CCL_PQD_Humanoid-v3_0_2022-03-03 15:19:55.525241' \
# --movie_name 'Humanoid_CCL_PQD_AfterUpdate' \
# &

