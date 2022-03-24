# Warm-Start Reinforcement Learning

If you use our code or data please cite the workshop papers [paper](https://arxiv.org/abs/dummy).
### Bibtex

```
@inproceedings{wexleranalyzing,
}
```

## Confidence Constrained Learning with Positive Q-value Distance (CCL-PQD) vs. Vanilla TD3

### Usage
The paper results can be reproduced by first creating the experts for HalfCheetah 4K reward, HalfCheetah 10K reward, Hopper, Humanoid (Fetch Slide, Push, and Pick-and-Place have hard-coded experts in *env_experts.py*:

```
cd scripts
sh train_TD3_envs.sh
```

Then rolling-out expert trajectories:
```
sh gen_expert_demos.sh
```

Then creating a **Behavior Cloned** expert:
```
sh batch_bc.sh
```

Then running **Warm-Start TD3**:
```
sh run_experttoTD3.sh
```

And **Warm-Start CCL-PQD**:
```
sh ./CCL-PQD/run_experttoTD3CCL_PQD<env-name>.sh
```

### Other benchmarks:

**BC Perturbation Net**:
```
sh ./BC-Perturbation/run_experttoTD3_BC_Pertubation<env-name>.sh
```

**BC Policy Penalty**:
```
sh ./BC-Perturbation/run_experttoTD3_BC_Constraint_Cheetah<env-name>.sh
```

**Learning Rate Reduction**:
```
sh ./LR-Reduction/run_experttoTD3_learning_rate<env-name>.sh
```

**Gradient Clipping**:
```
sh ./Gradient-Clipping/run_experttoTD3_gradient_clipping_cheetah<env-name>.sh
```

### Results
To draw perforance graphs, enter results directories and run:
```
cd draw_graphs
python draw_<env-name>ExperttoTD3vsTD3vsConfidenceScheduleBC.py
```

To draw pareto graphs, enter results directories and run:
```
python draw_<env-name>ExperttoTD3_Constraint_Compare.py
```

## Video
https://user-images.githubusercontent.com/17824538/159301536-799c12e5-9c15-4bb6-803a-dea994db9548.mp4

## Performance Graphs
<p float="left">
  <img src="https://user-images.githubusercontent.com/17824538/159579162-c0a75a9f-a0f3-4925-aaf3-30336e3fc1b1.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159579166-2a93640f-e6c4-4a92-8c41-299c1735a3da.png" width="400" /> 
  <img src="https://user-images.githubusercontent.com/17824538/159580567-2fd1463e-4069-4c8a-9ad9-d71e19858a07.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159579185-689f2923-f40e-49a7-bdff-0d0d56f36cec.png" width="400" /> 
  <img src="https://user-images.githubusercontent.com/17824538/159579173-c7cc595f-044f-4540-a12d-8cb919cc4499.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159579193-a39780e9-54ab-467e-bba3-7693675a9d4f.png" width="400" />
</p>

## Pareto Front Plots
<p float="left">
  <img src="https://user-images.githubusercontent.com/17824538/159578884-021b053a-0bf6-4f93-b71a-afb2600e2f44.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159578889-74cba59a-2605-4352-a14a-3e988e302e81.png" width="400" /> 
  <img src="https://user-images.githubusercontent.com/17824538/159580591-d5856b93-1b83-4874-b177-a31e06fe3b5b.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159578900-443a1266-710f-4eb9-b2e8-cddea367c2b8.png" width="400" /> 
  <img src="https://user-images.githubusercontent.com/17824538/159578891-c0ccced7-79f9-4601-b034-aa95d6816320.png" width="400" />
  <img src="https://user-images.githubusercontent.com/17824538/159578904-6ec76769-11d9-42d2-acab-a2ce3d868609.png" width="400" />
</p>




