"""
For in com lista

Exercício
Exiba os índices da lista
0 - Maria
1 - Ana
2 - Victor
"""

lista = ['Maria', 'Victor', 'Ana', 'André', 'Teste']
num = 0
for nome in lista: # Nome é uma str, então não dá para usar como contador
    print(num, '-', nome)
    num += 1

print()

indices = range(len(lista)) # Indices já é inteiro, então pode ser usado como contador
for indice in indices: 
    print(indice, lista[indice], type(lista[indice]))