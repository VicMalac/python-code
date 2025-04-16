"""
Operação ternária
if e else em uma única linha
<valor> if <condicao> else <outro valor>
"""
# x = 1
# variavel = 1 if x == 3 else 0
# print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

teste = "Valor" if False else "Outro Valor" if False else "Valor Final"
print(teste)