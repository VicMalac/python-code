"""
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
"""



try:
    num = input('Digite um número: ')
    num = float(num)
    numimp = num % 2 == 0
    if numimp:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
except:
    print('Você não digitou um número inteiro.')



"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""




try:
    hour = input('Que horas são agora? ')
    hour = hour[0:2]
    hour = int(hour)
    hour = f'{hour:=02}'

    if int(hour) >= 0 and int(hour) <= 11:
        print("Bom Dia!")
    elif int(hour) >= 12 and int(hour) <= 17:
        print("Boa Tarde!")
    elif int(hour) >= 24:
        print("Você digitou uma hora inválida.")
    else:
        print("Boa Noite!")
except:
    print('Você não digitou uma hora válida.')




"""
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""



nome = input("Digite o seu primeiro nome: ")
if len(nome) > 1:
    if len(nome) <= 4:
        print("O seu nome é curto.")
    elif len(nome) >= 5 and len(nome) <= 6:
        print("O seu nome tem um tamanho normal.")
    else:
        print("O seu nome é muito grande.")
else:
    print('Digite mais de uma letra.')