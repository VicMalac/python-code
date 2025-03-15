"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum ao tentar executar
"""

numero = input("Vou dobrar o número que você digitar: ")

try:
    print(f'STR: ', numero)
    numero = float(numero)
    print(f'FLOAT: ', numero)
    print(f'O dobro de {numero} é {numero * 2}')

except:
    print('Isso não é um número')
