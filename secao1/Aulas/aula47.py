"""
Faça um jogo para o usuário adivinhar qual a plavra secreta
 - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
 - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.

"""               #01234567
while True:
    palavra_secreta = input('Escreva a sua palavra secreta: ').lower() # Len == 8
    if palavra_secreta.isdigit():
        print('Escreva apenas letras!!!')
        continue
    else:
        break
                 #-87654321
letras_adicionadas = '*' * len(palavra_secreta)
tentativas = 0
letra_correta = ''
phrase_ao_contrario = len(palavra_secreta)

while letras_adicionadas != palavra_secreta:
    tentativas += 1
    phrase_ao_contrario = 0
    chute_usuario = input("Digite uma letra: ")
    if chute_usuario.isdigit():
        print("Apenas letras.")
        exit()
        
    if len(chute_usuario) > 1: # Se o usuario digitar mais de um caractere
        print("Digite somente uma letra.")
        continue
    chute_usuario = chute_usuario.lower()

    if chute_usuario in palavra_secreta: #  Se o chute do usuario estiver na palavra ele revela a/as letras
        for i in range(len(palavra_secreta)):
            phrase_ao_contrario = len(palavra_secreta) - len(palavra_secreta) - len(palavra_secreta)
            if chute_usuario == palavra_secreta[i]: # Se o chute existir na palavra, adiciona ela no lugar correto  
                letras_adicionadas = letras_adicionadas[:i] + chute_usuario + letras_adicionadas[i+1:] 
                continue
    else:
        print('Essa letra não existe na palavra!')
        continue
    print(letras_adicionadas)

else:
    print('         PARABÉNS\nVocê acertou a palavra secreta')
    print(f'Número de tentativas: {tentativas}')