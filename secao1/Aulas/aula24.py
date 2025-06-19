# Operadores in e not in
# String são iteráveis
# 0 1 2 3 4 5
# V I C T O R
#-6-5-4-3-2-1
nome = input("Digite o seu nome: ")
encontrar = input("Escreva o que deseja encontrar: ")

"""
print(nome[2])
print(nome[-2])
print('tor' in nome)
print('vic' in nome)
print('Vic' not in nome)
print('tro' not in nome)
"""

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f"{encontrar} não está em {nome}")