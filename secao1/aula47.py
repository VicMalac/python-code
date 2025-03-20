"""
Faça um jogo para o usuário adivinhar qual a plavra secreta
 - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
 - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.

"""               #01234567
palavra_secreta = 'azeiTONA'.lower() # Len == 8
                 #-87654321
letras_adicionadas = ''
tentativas = 0
letra_correta = ''
phrase_ao_contrario = len(palavra_secreta)

while letras_adicionadas != palavra_secreta:
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
            phrase_ao_contrario -= 1
            if chute_usuario == palavra_secreta[i]: # Se o chute existir na palavra, adiciona ela no lugar correto
                print(phrase_ao_contrario)
                letras_adicionadas = '*' * (((len(palavra_secreta)) - phrase_ao_contrario))+ chute_usuario+ 's' * ((len(palavra_secreta) - i + 1))
                continue
    print(letras_adicionadas)