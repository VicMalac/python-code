import os
import cv2
import numpy as np
from PIL import ImageGrab
import keyboard
import time

region = (650, 470, 750, 510)  # AJUSTE com base na posição real do jogo

# Cria pastas se não existirem
for pasta in ["pular", "abaixar", "nada"]:
    os.makedirs(f"dataset/{pasta}", exist_ok=True)

def salvar(imagem, classe):
    nome = f"{classe}_{len(os.listdir(f'dataset/{classe}'))}.png"
    caminho = os.path.join("dataset", classe, nome)
    cv2.imwrite(caminho, imagem)

print("Use: P (pular), A (abaixar), N (nada), ESC (sair)")

while True:
    img = ImageGrab.grab(bbox=region).convert('L')
    img_np = np.array(img)
    cv2.imshow("Coleta", img_np)

    if keyboard.is_pressed("p"):
        salvar(img_np, "pular")
        print("Salvo: pular")
        time.sleep(0.5)  # evita múltiplos cliques
    elif keyboard.is_pressed("a"):
        salvar(img_np, "abaixar")
        print("Salvo: abaixar")
        time.sleep(0.5)
    elif keyboard.is_pressed("n"):
        salvar(img_np, "nada")
        print("Salvo: nada")
        time.sleep(0.5)
    elif keyboard.is_pressed("esc"):
        break

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
