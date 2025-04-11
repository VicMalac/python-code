"""
split e join com list e str
split - divide uma string
join - une uma string
strip - Significa que irá cortar os espaços no começo e no fim da frase
rstrip - Significa que irá cortar os espaços da direita
lstrip - Significa que irá cortar os espaços da esquerda
"""

frase = "Farei uma atividade amanhã      , não gosto"
lista_palavras = frase.split(",") # Coloca dentro da função o que quer seja splitado para dividido
print(lista_palavras)
lista_palavras_corretas = []
for i, frase in enumerate(lista_palavras):
    lista_palavras_corretas.append(lista_palavras[i].strip())

# print(lista_palavras)
# print(lista_palavras_corretas)

frases_unidas = '-'.join('abc')
print(frases_unidas)