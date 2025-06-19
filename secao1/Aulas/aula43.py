## Laço de repetição for

# i = 0
# tamanho_string = len(texto)
# senha_digitada = ""
# senha_salva = "123456"
# i = 0
# while senha_digitada != senha_salva:
#     senha_digitada = input(f"Senha incorreta (N° de tentativas: {i}x) ")
#     i += 1

# else:
#     print("Senha correta!")
texto = 'Python' 

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + "*")