#


## RISE
[source](https://github.com/RLE-Foundation/Hsuanwu/blob/main/hsuanwu/xplore/reward/rise.py/#L59)
```python 
RISE(
   observation_space: Union[gym.Space, DictConfig], action_space: Union[gym.Space,
   DictConfig], device: str = 'cpu', beta: float = 0.05, kappa: float = 2.5e-05,
   latent_dim: int = 128, alpha: float = 0.5, k: int = 5, average_entropy: bool = False
)
```


---
Rényi State Entropy Maximization for Exploration Acceleration in Reinforcement Learning (RISE).
See paper: https://ieeexplore.ieee.org/abstract/document/9802917/


**Args**

* **observation_space** (Space or DictConfig) : The observation space of environment. When invoked by Hydra,
    'observation_space' is a 'DictConfig' like {"shape": observation_space.shape, }.
* **action_space** (Space or DictConfig) : The action space of environment. When invoked by Hydra,
    'action_space' is a 'DictConfig' like
    {"shape": (n, ), "type": "Discrete", "range": [0, n - 1]} or
    {"shape": action_space.shape, "type": "Box", "range": [action_space.low[0], action_space.high[0]]}.
* **device** (str) : Device (cpu, cuda, ...) on which the code should be run.
* **beta** (float) : The initial weighting coefficient of the intrinsic rewards.
* **kappa** (float) : The decay rate.
* **latent_dim** (int) : The dimension of encoding vectors.
* **alpha** (alpha) : The The order of Rényi entropy.
* **k** (int) : Use the k-th neighbors.
* **average_entropy** (bool) : Use the average of entropy estimation.


**Returns**

Instance of RISE.


**Methods:**


### .compute_irs
[source](https://github.com/RLE-Foundation/Hsuanwu/blob/main/hsuanwu/xplore/reward/rise.py/#L109)
```python
.compute_irs(
   samples: Dict, step: int = 0
)
```

---
Compute the intrinsic rewards for current samples.


**Args**

* **samples** (Dict) : The collected samples. A python dict like
    {obs (n_steps, n_envs, *obs_shape) <class 'th.Tensor'>,
    actions (n_steps, n_envs, *action_shape) <class 'th.Tensor'>,
    rewards (n_steps, n_envs) <class 'th.Tensor'>,
    next_obs (n_steps, n_envs, *obs_shape) <class 'th.Tensor'>}.
* **step** (int) : The global training step.


**Returns**

The intrinsic rewards.

### .update
[source](https://github.com/RLE-Foundation/Hsuanwu/blob/main/hsuanwu/xplore/reward/rise.py/#L145)
```python
.update(
   samples: Dict
)
```

---
Update the intrinsic reward module if necessary.


**Args**

* **samples**  : The collected samples. A python dict like
    {obs (n_steps, n_envs, *obs_shape) <class 'th.Tensor'>,
    actions (n_steps, n_envs, *action_shape) <class 'th.Tensor'>,
    rewards (n_steps, n_envs) <class 'th.Tensor'>,
    next_obs (n_steps, n_envs, *obs_shape) <class 'th.Tensor'>}.


**Returns**

None