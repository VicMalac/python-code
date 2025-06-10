"""
Programa criado para a empresa Via Dolce para automatizar a exclusão de fotos do Google, funciona de forma simples
Após rodar o código, você tem 5 segundos para posicionar o mouse em cima do ícone de excluir
Então o programa simula o botão de clique e depois aperta o enter para confirmar a exclusão e prossegue o número de vezes que for colocado na variável 'lote'
"""
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

lote = 50 # Quantidade de produtos que serão excluídos
intervalo_entre_itens = 3 # Em segundos
arquivo = open('arquivo.txt', 'r')
total_removidos = int(arquivo.read()) # Número total de remoções, sendo adicionado em um .txt
arquivo.close()
arquivo = open('arquivo.txt', 'w')
arquivo.write(f'{total_removidos}')
arquivo.close()

def perguntar_se_deseja_continuar(total): # Janela de confirmação
    arquivo = open('arquivo.txt', 'w')
    arquivo.write(f'{total_removidos}')
    arquivo.close()
    root = tk.Tk()
    root.withdraw()

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
        print(f'Total de fotos removidas: {total_removidos + 1}')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(intervalo_entre_itens)
        total_removidos += 1

    if not perguntar_se_deseja_continuar(total_removidos):
        print("Finalizado pelo usuário.")
        break
