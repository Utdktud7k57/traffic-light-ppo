# 🚦 Traffic Light Optimization using PPO

This project uses **Reinforcement Learning (PPO)** from **Stable-Baselines3** to optimize traffic light control at a simulated four-way intersection.  
The goal: **Minimize queue lengths** by deciding when to switch lights.

---

## 📖 Project Overview
We define a custom **Gym environment** `TrafficEnv` where:
- Cars arrive from **North, South, East, West** (Poisson distribution)
- Lights have two phases: `NS Green` or `EW Green`
- The agent decides to **keep** or **switch** the light
- Reward = negative squared sum of queue lengths (penalizing long waits)

The PPO agent learns an optimal switching strategy by interacting with the environment.

---

## ⚙️ Features
✅ Custom OpenAI Gym environment  
✅ PPO training using Stable-Baselines3  
✅ Evaluation of **Random vs Trained policy**  
✅ Visualization of:
- Total reward per episode
- Queue length changes over time
- Actions taken (switch/keep)

---

## 📂 Project Structure
traffic-light-ppo/
- ├── traffic_env.py       # Custom traffic environment
- ├── train.py             # Train PPO agent
- ├── simulate.py          # Run trained model and visualize results
- ├── requirements.txt     # Python dependencies
- └── README.md            # Project documentation


---

## 🛠 Installation

Clone this repository:

git clone https://github.com/Utdktud7k57/traffic-light-ppo.git
cd traffic-light-ppo
Install dependencies:

- pip install -r requirements.txt
## ▶️ Usage
- Train the model
  python train.py
-Simulate & visualize results
  python simulate.py
## 📊 Results
- Policy Comparison
 Trained PPO policy achieves significantly higher rewards than a random policy.
 - Queue Lengths Over Time
 The PPO agent keeps queue lengths lower over the simulation.

![Descriptive Alt Text](images/Policy_comparision.png)

## 📌 Requirements
- See requirements.txt:
nginx
gym
numpy
matplotlib
stable-baselines3





##  Author 
- Tejaswini Samudrala
- GitHub: https://github.com/Utdktud7k57
