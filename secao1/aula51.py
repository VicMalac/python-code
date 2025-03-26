"""
For in com lista

Exercício
Exiba os índices da lista
0 - Maria
1 - Ana Luiza
2 - Victor
"""
# fora_da_lista = 2
# lista = ["Maria", 'Helena', 'Victor', 'Luiz', 14, fora_da_lista]
# for nome in lista:
#     print(nome, type(nome))
lista = 'Maria', 'Victor', 'Ana Luiza'
num = 0
for nome in lista: # Nome é uma ste, então não dá para usar como contador
    print(num, '-', nome)
    num += 1

print()

indices = range(len(lista)) # Indices já é inteiro, então pode ser usado como contador
for indice in indices: 
    print(indice, lista[indice], type(lista[indice]))