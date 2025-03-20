frase = (
    'aabbb'
    )

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1


print(f'A letra que mais apareceu foi {letra_apareceu_mais_vezes!r}')

# O que meu código faz?
# ele conta quantas vezes uma letra aparece na frase