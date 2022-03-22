# Warm-Start Reinforcement Learning

## Confidence Constrained Learning with Positive Q-value Distance (CCL-PQD) vs. Vanilla TD3

### Usage
The paper results can be reproduced by first creating the experts:
```
./run_experiments.sh
```

Then creating a Behavior Cloned expert:
```
python main.py --env HalfCheetah-v2
```

Then running Warm-Start TD3:
```
python main.py --env HalfCheetah-v2
```

And Warm-Start CCL-PQD:
```
python main.py --env HalfCheetah-v2
```

BC Perturbartion Net:
```
python main.py --env HalfCheetah-v2
```

BC Policy Penalty:
```
python main.py --env HalfCheetah-v2
```

BC Learning Rate Reduction:
```
python main.py --env HalfCheetah-v2
```

BC Gradient Clipping :
```
python main.py --env HalfCheetah-v2
```

### Results
To graph results run:
```
python main.py --env HalfCheetah-v2
```

https://user-images.githubusercontent.com/17824538/159301536-799c12e5-9c15-4bb6-803a-dea994db9548.mp4

![Cheetah Cheetah_Confidence_Scheduled_BC vs  ExperttoTD3 vs  TD3 4000](https://user-images.githubusercontent.com/17824538/159579162-c0a75a9f-a0f3-4925-aaf3-30336e3fc1b1.png)
![Cheetah Cheetah_Confidence_Scheduled_BC vs  ExperttoTD3 vs  TD3 10000](https://user-images.githubusercontent.com/17824538/159579166-2a93640f-e6c4-4a92-8c41-299c1735a3da.png)
![Fetch Slide Confidence_Scheduled_BC vs  ExperttoTD3 vs  TD3](https://user-images.githubusercontent.com/17824538/159579173-c7cc595f-044f-4540-a12d-8cb919cc4499.png)
![Fetch PushPerformance](https://user-images.githubusercontent.com/17824538/159579185-689f2923-f40e-49a7-bdff-0d0d56f36cec.png)
![Fetch Confidence_Scheduled_BC vs  ExperttoTD3 vs  TD3](https://user-images.githubusercontent.com/17824538/159579193-a39780e9-54ab-467e-bba3-7693675a9d4f.png)



Pareto Front Graphs
![Cheetah ExperttoTD3 Constraint Compare4000](https://user-images.githubusercontent.com/17824538/159578884-021b053a-0bf6-4f93-b71a-afb2600e2f44.png)
![Cheetah ExperttoTD3 Constraint Compare10000](https://user-images.githubusercontent.com/17824538/159578889-74cba59a-2605-4352-a14a-3e988e302e81.png)
![FetchPush ExperttoTD3 Constraint Compare (1)](https://user-images.githubusercontent.com/17824538/159578891-c0ccced7-79f9-4601-b034-aa95d6816320.png)
![FetchSlide ExperttoTD3 Constraint Compare (1)](https://user-images.githubusercontent.com/17824538/159578900-443a1266-710f-4eb9-b2e8-cddea367c2b8.png)
![FetchPickAndPlace ExperttoTD3 Constraint Compare (1)](https://user-images.githubusercontent.com/17824538/159578904-6ec76769-11d9-42d2-acab-a2ce3d868609.png)


If you use our code or data please cite the workshop papers [paper](https://arxiv.org/abs/dummy).
### Bibtex

```
@inproceedings{wexleranalyzing,
}
```




