"""
Introdução ao desempacotamento + tuples (tuplas)

Tuplas - São listas que não podem ter modificação de indice, diferente das listas
"""
nome1, *resto = ['Maria', 'Helena', 'Victor'] # Lista
print(nome1, resto)

_, _, name1, _= ['Luiz', 'Ana', 'Livia', 'Gustavo'] # O _ indica que aquela variavel não será utilizada
print(_)
name1 = ['Luiz', 'Ana', 'Livia', 'Gustavo']
# Tipo tupla - Uma lista imutável

nomes = 'Maria', 'Helena', 'Luiz' # Tupla
names = ('tupla', 'teste')
print(nomes[0])
print(names)
print(f'Lista: {name1}', type(name1))
name1 = tuple(name1) # Converte uma lista para tupla
print(f'Tupla: {name1}', type(name1))