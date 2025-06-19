import random
import sys

for i in range(10):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    cpf = cpf[:9]
    soma = 0
    mult = 10
    for i in cpf:
        i = int(i)
        soma += i * mult
        mult -= 1
    soma = (soma * 10) % 11
    if soma > 9:
        soma = 0
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
    cpf = f'{cpf}{soma}'
    print(cpf)

