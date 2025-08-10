import matplotlib.pyplot as plt
import numpy as np
from stable_baselines3 import PPO
from traffic_env import TrafficEnv

def simulate_and_collect_data(env, model):
    obs = env.reset()
    done = False
    queue_history = []
    actions = []
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        queue_history.append(obs.copy())
        actions.append(action)
    return np.array(queue_history), actions

env = TrafficEnv()
model = PPO.load("traffic_model", env=env)
queues, actions = simulate_and_collect_data(env, model)

plt.figure(figsize=(12,6))
for i, direction in enumerate(['North', 'South', 'East', 'West']):
    plt.plot(queues[:, i], label=f'Queue {direction}')
plt.xlabel('Time step')
plt.ylabel('Queue length')
plt.title('Queue lengths over time')
plt.legend()
plt.show()

plt.figure(figsize=(12,3))
plt.step(range(len(actions)), actions, where='post')
plt.xlabel('Time step')
plt.ylabel('Action (0=keep, 1=switch)')
plt.title('Traffic light actions over time')
plt.show()
