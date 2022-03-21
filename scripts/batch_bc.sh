#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python ../batch_BC.py \
--env "Ant-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/BC_TD3_Ant-v3_0_1000_episodes:_101_states:_85736' \
--save_model \
--max_timesteps 50000 \
&

CUDA_VISIBLE_DEVICES=1 python ../batch_BC.py \
--env "HalfCheetah-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/BC_TD3_HalfCheetah-v3_0_4000_episodes:_101_states:_101000' \
--save_model \
--max_timesteps 50000 \
&

CUDA_VISIBLE_DEVICES=2 python ../batch_BC.py \
--env "Hopper-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/BC_TD3_Hopper-v3_0_1000_episodes:_101_states:_28960' \
--save_model \
--max_timesteps 50000 \
&

CUDA_VISIBLE_DEVICES=3 python ../batch_BC.py \
--env "Humanoid-v3" \
--lr 0.003 \
--expert_demo_file '../expert_demos/BC_TD3_Humanoid-v3_0_1000_episodes:_101_states:_21036' \
--save_model \
--max_timesteps 50000 \
&