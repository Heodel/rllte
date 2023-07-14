# =============================================================================
# MIT License

# Copyright (c) 2023 Reinforcement Learning Evolution Foundation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================


import argparse

from rllte.agent import PPO
from rllte.env import make_bullet_env

parser = argparse.ArgumentParser()
parser.add_argument("--env-id", type=str, default="AntBulletEnv-v0")
parser.add_argument("--device", type=str, default="cuda")
parser.add_argument("--seed", type=int, default=1)

if __name__ == "__main__":
    args = parser.parse_args()
    # create env
    env = make_bullet_env(
        env_id=args.env_id,
        num_envs=1,
        device=args.device,
        seed=args.seed,
    )
    eval_env = make_bullet_env(
        env_id=args.env_id,
        num_envs=1,
        device=args.device,
        seed=args.seed,
    )
    # create agent
    feature_dim = 64
    agent = PPO(
        env=env,
        eval_env=eval_env,
        tag=f"ppo_bullet_{args.env_id}_seed_{args.seed}",
        seed=args.seed,
        device=args.device,
        num_steps=2048,
        feature_dim=feature_dim,
        batch_size=64,
        lr=2e-4,
        eps=1e-5,
        clip_range=0.2,
        clip_range_vf=None,
        n_epochs=10,
        vf_coef=0.5,
        ent_coef=0.0,
        max_grad_norm=0.5,
        network_init_method="orthogonal",
    )
    # training
    agent.train(num_train_steps=1000000)
