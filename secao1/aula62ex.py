"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitod do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex: 746824890
    11  10   9   8   7   6   5   4   3  2
    7   4    6   8   2   4   8   9   0  7 <-- PRIMEIRO DÍGITO
    77  40   54  64  14  24  40  36  0  14

Somar todos os reslttados:
77+40+54+64+14+24+40+36+0+14= 363
Multiplicaro resltado anterior por 10
363 * 10  = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf = input("Digite o seu cpf sem os dígitos finais: ").replace(".", "").replace("-", "")
soma = 0
mult = 10
for i in cpf:
    i = int(i)
    soma += i * mult
    mult -= 1
soma = (soma * 10) % 11
if soma > 9:
    soma = 0
print(f"O primeiro dígito é: {soma}")
soma = str(soma); cpf += soma; soma = 0

# Nesse caso soma == "7"

mult = 11
for i in cpf:
    i = int(i)
    soma += i * mult
    mult -= 1
soma = (soma * 10) % 11
if soma > 9:
    soma = 0
print(f"O segundo dígito é: {soma}")    