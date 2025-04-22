from environment_trex import TrexEnv
from stable_baselines3 import PPO
import time

env = TrexEnv()
model = PPO.load("ppo_dino")

obs = env.reset()
time.sleep(1)

print("🎮 Jogando com IA treinada...")

while True:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
