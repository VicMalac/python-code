"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis: append, insert, pop, del, celar, extend, +
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update Delete
Criar Ler   Alterar Apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
#lista_d = lista_a.extend(lista_b) # Ele mexe diretamente no A, então não dará certo, irá retornar None
lista_a.extend(lista_b)
print(lista_a)
print(lista_c)
#print(lista_d)