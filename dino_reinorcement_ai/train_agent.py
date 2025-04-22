from environment_trex import TrexEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

# Criar ambiente
env = TrexEnv()

# Verificar integridade do ambiente (opcional)
check_env(env, warn=True)

# Criar modelo
model = PPO("CnnPolicy", env, verbose=1)

# Treinar
print("🚀 Iniciando treino...")
model.learn(total_timesteps=100000)  # você pode aumentar esse valor depois

# Salvar modelo
model.save("ppo_dino")
print("✅ Modelo salvo como 'ppo_dino.zip'")
