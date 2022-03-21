#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python ../gen_expert_buff.py \
--env "Ant-v3" \
--num_episodes 101 \
--expl_noise 0.1 \
--expert_model_dir '../models/Ant-v3_TD3_model/TD3_Ant-v3_0_1000' \
--replay_buffer_dir '../expert_demos' \
&

CUDA_VISIBLE_DEVICES=1 python ../gen_expert_buff.py \
--env "HalfCheetah-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/HalfCheetah-v3_TD3_model/TD3_HalfCheetah-v3_0_4000' \
--replay_buffer_dir '../expert_demos' \
&

CUDA_VISIBLE_DEVICES=2 python ../gen_expert_buff.py \
--env "Hopper-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/Hopper-v3_TD3_model/TD3_Hopper-v3_0_1000' \
--replay_buffer_dir '../expert_demos' \
&

CUDA_VISIBLE_DEVICES=3 python ../gen_expert_buff.py \
--env "Humanoid-v3" \
--expl_noise 0.1 \
--num_episodes 101 \
--expert_model_dir '../models/Humanoid-v3_TD3_model/TD3_Humanoid-v3_0_1000' \
--replay_buffer_dir '../expert_demos' \
&

