"""
Array dentro array
Array dentro do outro pode ser chamado conforme mais  []  você  adiciona, mas fica muito complexo se executado da maneira errada
"""

lista = ["lista1", "lista1-1", ["lista2", "lista2-1", ["lista3", "lista3-1"]]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[2][0])
print(lista[2][1])
print(lista[2][2])
print(lista[2][2][0])
print(lista[2][2][1])