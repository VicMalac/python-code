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

string = 'ABCDE' # 5 caracteres (len)
lista = [123, True, 'Victor', 1.3, ['macaco']]
lista[2] = 'Ana Luiza'
listinha = []
# print(string[4], type(string))
# print(lista[2][2], type(list), bool(list))
# print(lista[2], type(list), bool(list))
# print(lista, type(list), bool(list))
# print(listinha, type(list), bool(listinha))

lista.append(12)
lista.append("Manaus")
# lista.clear()
lista.append("Amor")
# Remove o último valor da lista até o momento
var = lista.pop()
print("Removido: ", var)
lista.append(24.2)
lista.insert(1, "Alex")
lista.insert((len(lista)), "Susto") #Insere no ultimo lugar da lista
print(lista)
print(len(lista))