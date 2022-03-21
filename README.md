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

### Results
To graph results run:
```
python main.py --env HalfCheetah-v2
```

https://user-images.githubusercontent.com/17824538/159301536-799c12e5-9c15-4bb6-803a-dea994db9548.mp4

If you use our code or data please cite the workshop papers [paper](https://arxiv.org/abs/dummy).
### Bibtex

```
@inproceedings{wexleranalyzing,
}
```




