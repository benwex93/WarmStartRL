# #!/bin/bash

# CUDA_VISIBLE_DEVICES=1 python ../train_behavioral.py \
# --policy "TD3" \
# --env "Ant-v3" \
# --max_timesteps 1000000 \
# --seed 0 \
# --log \
# --results_dir '../results/Ant-v3_results' \
# --model_dir '../models/Ant-v3_TD3_model/' \
# --save_model \
# --desired_performance 4000 \
# --save_replay_buffer \

# CUDA_VISIBLE_DEVICES=0 python ../train_behavioral.py \
# --policy "TD3" \
# --env "HalfCheetah-v3" \
# --max_timesteps 1000000 \
# --seed 0 \
# --log \
# --results_dir '../results/HalfCheetah-v3_results/' \
# --model_dir '../models/HalfCheetah-v3_TD3_model/' \
# --save_model \
# --desired_performance 4000 \
# --save_replay_buffer \
# &

# CUDA_VISIBLE_DEVICES=3 python ../train_behavioral.py \
# --policy "TD3" \
# --env "Hopper-v3" \
# --max_timesteps 1000000 \
# --seed 0 \
# --log \
# --results_dir '../results/Hopper-v3_results' \
# --model_dir '../models/Hopper-v3_TD3_model/' \
# --save_model \
# --desired_performance 4000 \
# --save_replay_buffer \
# &

# CUDA_VISIBLE_DEVICES=1 python ../train_behavioral.py \
# --policy "TD3" \
# --env "Humanoid-v3" \
# --max_timesteps 1000000 \
# --seed 0 \
# --log \
# --results_dir '../results/Humanoid-v3_results' \
# --model_dir '../models/Humanoid-v3_TD3_model/' \
# --save_model \
# --desired_performance 4000 \
# --save_replay_buffer \

# CUDA_VISIBLE_DEVICES=3 python ../train_behavioral.py \
# --policy "TD3" \
# --env "FetchPush-v1" \
# --max_timesteps 1000000 \
# --seed 0 \
# --log \
# --results_dir '../results/FetchPush-v1_results' \
# --desired_performance 4000 \
# --model_dir '../models/FetchPush-v1_TD3_model/' \

CUDA_VISIBLE_DEVICES=0 python ../train_behavioral.py \
--policy "TD3" \
--env "FetchSlide-v1" \
--max_timesteps 100000 \
--seed 0 \
--log \
--results_dir '../results/FetchSlide-v1_results' \
--desired_performance 4000 \
--model_dir '../models/FetchSlide-v1_TD3_model/' \

# --save_model \
# --save_replay_buffer \
