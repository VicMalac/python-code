"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregure o seu iterador
"""

# texto = 'Victor'.__iter__() # Metodo
# texto2 = iter("Luiz")
# numeros = range(1, 10)
# print(texto)
# print(texto2.__next__())
# print(texto2.__next__())
# print(next(texto2))
# print(next(texto2))

texto = 'Victor'
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration: # Erro de iterador, se tem 4 iteradore, a quinta iteração dá erro pois só existe 4 então roda o except e prosegue o código
        break # Quebra o While
        # exit() finaliza o código por completo