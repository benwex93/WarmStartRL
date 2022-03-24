# #!/bin/bash

CUDA_VISIBLE_DEVICES=0 python ../train_behavioral.py \
--policy "TD3" \
--env "HalfCheetah-v3" \
--max_timesteps 1000000 \
--seed 0 \
--model_dir '../models/HalfCheetah-v3_TD3_model_4K/' \
--save_model \
--desired_performance 4000 \
--save_replay_buffer \
# &

CUDA_VISIBLE_DEVICES=0 python ../train_behavioral.py \
--policy "TD3" \
--env "HalfCheetah-v3" \
--max_timesteps 1000000 \
--seed 0 \
--model_dir '../models/HalfCheetah-v3_TD3_model_10K/' \
--save_model \
--desired_performance 10000 \
--save_replay_buffer \
# &

CUDA_VISIBLE_DEVICES=3 python ../train_behavioral.py \
--policy "TD3" \
--env "Hopper-v3" \
--max_timesteps 1000000 \
--seed 0 \
--model_dir '../models/Hopper-v3_TD3_model/' \
--save_model \
--desired_performance 2000 \
--save_replay_buffer \
# &

CUDA_VISIBLE_DEVICES=1 python ../train_behavioral.py \
--policy "TD3" \
--env "Humanoid-v3" \
--max_timesteps 1000000 \
--seed 0 \
--model_dir '../models/Humanoid-v3_TD3_model/' \
--save_model \
--desired_performance 2000 \
--save_replay_buffer \
# &