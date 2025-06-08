import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Configurações iniciais
lote = 50  # Quantos por rodada
intervalo_entre_itens = 3  # Segundos entre exclusões
total_removidos = 2484

def perguntar_se_deseja_continuar(total):
    # Janela pop-up perguntando se quer continuar
    root = tk.Tk()
    root.withdraw()  # Oculta janela principal

    resposta = messagebox.askyesno(
        "Continuar?",
        f"{total} produtos foram removidos.\nDeseja continuar apagando mais {lote}?"
    )
    root.destroy()
    return resposta

print("Você tem 5 segundos para posicionar o mouse sobre o ícone de lixeira...")
time.sleep(5)

while True:
    for i in range(lote):
        pyautogui.click()
        print(f'[{total_removidos + 1}] Clique na lixeira.')
        time.sleep(1)
        pyautogui.press('enter')
        print(f'[{total_removidos + 1}] Pressionado ENTER para confirmar.')
        time.sleep(intervalo_entre_itens)
        total_removidos += 1

    # Ao final do lote, pergunta se deseja continuar
    if not perguntar_se_deseja_continuar(total_removidos):
        print("Finalizado pelo usuário.")
        break
