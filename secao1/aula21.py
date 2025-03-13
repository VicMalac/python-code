# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu) -> 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E] Entrar ou [S] Sair: ')
senha = input('Digite sua senha: ')

senhaCorreta = '123456'

if entrada == 'E' and senhaCorreta == senha:
    print("Bem-vindo")
else: 
    print("Senha incorreta ou opção inválida")

# Avaliação de curto circuito
print(True and False and True) #Para sempre no que é falso
print(True and 0 and True) # 0 é falso, por isso parou nele

if 1 and 1:
    print(True and 1 and True)