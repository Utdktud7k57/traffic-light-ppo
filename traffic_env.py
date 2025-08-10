import gym
from gym import spaces
import numpy as np

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=100, shape=(4,), dtype=np.int32)
        self.reset()

    def reset(self):
        self.queues = np.zeros(4, dtype=np.int32)
        self.current_phase = 0
        self.time = 0
        return self.queues

    def step(self, action):
        if action == 1:
            self.current_phase = 1 - self.current_phase

        arrivals = np.random.poisson(2, size=4)
        self.queues += arrivals

        green_directions = [0, 1] if self.current_phase == 0 else [2, 3]
        for i in green_directions:
            passed = min(self.queues[i], 3)
            self.queues[i] -= passed

        self.queues = np.clip(self.queues, 0, None)
        reward = -np.sum(self.queues ** 2)
        self.time += 1
        done = self.time >= 100
        return self.queues, reward, done, {}

    def render(self, mode='human'):
        print(f"Time: {self.time} | Queues: {self.queues} | Phase: {'NS Green' if self.current_phase == 0 else 'EW Green'}")
