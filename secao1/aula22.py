# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu) -> 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

print(0 or False or False or 'qwerty' or True)
senha = input("Senha: ") or 'Sem senha'

print(senha)