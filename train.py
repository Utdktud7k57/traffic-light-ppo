from stable_baselines3 import PPO
from traffic_env import TrafficEnv

env = TrafficEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=50000)
model.save("traffic_model")
