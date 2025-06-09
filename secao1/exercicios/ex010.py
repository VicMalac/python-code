# Adivinhar um número

import random
import os

num = random.randrange(0, 100, 1)
tentativas = 0
os.system("cls")
while True:
    tentativas += 1
    chute = int(input("Digite o seu chute: "))
    if chute > num:
        print("O seu número é maior")
        continue
    elif chute < num:
        print("O seu número é menor")
        continue
    else:
        print("Você acertou!")
        print(f"Número de tentativas: {tentativas}")
        break