"""
Cuidados com dados mutáveis
= - Copiado o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'Victor'
# print(nome)
# print(noutra_variavel)
lista_a = ['Teste', 'Hoje']
lista_b = lista_a.copy()
lista_a[0] = 'Macaco'
print(lista_a)
print(lista_b)