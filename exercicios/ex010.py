# Adivinhar um número

import random

num = random.randrange(0, 100, 1)

while True:
    chute = int(input("Digite o seu chute: "))
    if chute > num:
        print("O seu número é maior")
        continue
    elif chute < num:
        print("O seu número é menor")
        continue
    else:
        print("Você acertou!")
        break