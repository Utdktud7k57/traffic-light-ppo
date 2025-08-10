import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from traffic_env import TrafficEnv

def evaluate_agent(env, model, episodes=100):
    rewards = []
    for _ in range(episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _ = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    return rewards

def evaluate_random_policy(env, episodes=100):
    rewards = []
    for _ in range(episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        while not done:
            action = env.action_space.sample()
            obs, reward, done, _ = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    return rewards

env = TrafficEnv()
model = PPO.load("traffic_model", env=env)

random_rewards = evaluate_random_policy(env)
trained_rewards = evaluate_agent(env, model)

plt.plot(random_rewards, label='Random Policy')
plt.plot(trained_rewards, label='Trained PPO')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Policy Comparison')
plt.legend()
plt.show()
