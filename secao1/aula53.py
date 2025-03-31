"""
enumerate = enumera iteráveis (índices)
"""
lista = ['Maria', 'Ana', 'Victor', 'Anais']
lista.append('Luiz')

lista_enumerada = tuple(enumerate(lista, start=1))

# for i in lista_enumerada: # index vai receber o indice da lista e i recebe o valor ex: index = 0 e i = 'Maria'
#     a, b = i
#     print(a, b)

# for indice, nome in lista_enumerada:
#     print(indice, nome)

# print(lista_enumerada) # consumiu os valores então retorna somente o iterador

for tupla_enumerada in enumerate(lista):
    print("FOR da tupla: ")
    for valor in tupla_enumerada:
        print(f'\t{valor}')