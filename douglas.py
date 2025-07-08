# Crie um programa que receba do usuário a idade de duas pessoas em anos inteiros e compare:

# Se elas têm a mesma idade.
# Qual delas é mais velha.


# Exiba mensagens como:
# "Ambas têm a mesma idade"
# ou
# "Pessoa A é mais velha que Pessoa B".
# ou ainda
# "Pessoa B é mais velha que Pessoa A"
from os import system
from time import sleep

idade1 = []
idade2 = []

while True:
    try:
        nome1 = {input("Digite o seu nome:  ") : int(input("Digite a sua idade: "))}
        nome2 = {input("Digite o seu nome:  ") : int(input("Digite a sua idade: "))}
        break
    except:
        system("cls")
        print("Digite apenas números inteiros na idade")
        sleep(3)
        system("cls")
        continue

idade1.append(list(nome1.keys())[0])
idade1.append(list(nome1.values())[0])
idade2.append(list(nome2.keys())[0])
idade2.append(list(nome2.values())[0])


if idade1[1] > idade2[1]:
    print(f"{list(nome1.keys())[0]} é mais velho(a) do que {list(nome2.keys())[0]}")
elif idade1[1] < idade2[1]:
    print(f"{list(nome2.keys())[0]} é mais velho(a) do que {list(nome1.keys())[0]}")
else:
    print("Ambas têm a mesma idade")