# Criar um programa que leia 10 números inteiros e imprima o maior e o menor número.
from os import system
num = []

for i in range(0, 10):
    nuum = int(input("Digite um número: "))
    num.append(nuum)
    maior = num[0]
    menor = num[0]

for i in range(0, 10):
    system("cls")
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]

print(f"Maior: {maior}\nMenor: {menor}")