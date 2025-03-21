# Criar um programa que leia 10 números inteiros e imprima o maior e o menor número.

number = ''
maior = 0
menor = 0

while True:
    for i in range(0, 10):
        mamei = input("Digite um número: ")
        if not mamei.isdigit():
            print('Digite apenas números!')
            continue
    
    for i in range(0, 10):
        number = int(number)
        if number >= 0:
            maior = number[i]

    print('Maior: ', maior)