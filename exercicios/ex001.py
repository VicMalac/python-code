# Criar um programa que leia 10 números inteiros e imprima o maior e o menor número.

number = ''
maior = 0
menor = 0

while True:
    for i in range(0, 10):
        mamei = int(input("Digite um número: "))
    
    for i in range(0, 10):
        number = f'{number}' + f'{mamei}'
        number = int(number)
        if number > maior:
            maior = number
        
    break
print('Maior: ', maior)