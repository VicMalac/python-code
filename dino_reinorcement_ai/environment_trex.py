import gym
from gym import spaces
import numpy as np
import cv2
import pyautogui
import mss
import time

class TrexEnv(gym.Env):
    def __init__(self):
        super(TrexEnv, self).__init__()
        
        self.monitor = {"top": 470, "left": 650, "width": 100, "height": 40}
        self.done_monitor = {"top": 440, "left": 690, "width": 160, "height": 50}  # onde aparece "Game Over"
        self.sct = mss.mss()
        
        # Ações: 0 = nada, 1 = pular, 2 = abaixar
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=255, shape=(40, 100), dtype=np.uint8)

    def reset(self):
        print("🔄 Reiniciando o jogo. Clique e pressione espaço...")
        time.sleep(2)
        pyautogui.press("space")  # reinicia o jogo
        time.sleep(1)
        return self._get_observation()

    def step(self, action):
        reward = 1  # ganha 1 por sobreviver
        done = self._check_game_over()

        if action == 1:
            pyautogui.press("space")
        elif action == 2:
            pyautogui.keyDown("down")
            time.sleep(0.1)
            pyautogui.keyUp("down")

        obs = self._get_observation()

        if done:
            reward = -100  # punição por morrer

        return obs, reward, done, {}

    def _get_observation(self):
        img = self.sct.grab(self.monitor)
        frame = np.array(img)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def _check_game_over(self):
        img = self.sct.grab(self.done_monitor)
        frame = np.array(img)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # Se a região tiver muito texto branco (como "GAME OVER")
        return np.count_nonzero(thresh) > 300

    def render(self, mode='human'):
        cv2.imshow("Dino Vision", self._get_observation())
        if cv2.waitKey(1) == ord('q'):
            self.close()

    def close(self):
        cv2.destroyAllWindows()
