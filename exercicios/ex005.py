# Elaborar um programa que a partir de uma determinada quantidade de linhas e colunas digitadas pelo usuário exiba um retângulo, por exemplo:
"""
*Entrada:
Linhas: 4
Colunas: 6

!Saída:
+----+
|    |
|    |
+----+
"""

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

for i in range(linhas):
    if i == 0:
        comfim = True
    elif i < linhas - 1:
        comfim = False
    else:
        comfim = True
    for i in range(colunas):
        # Linha Inicial
        if i == 0:
            if comfim == True:
                print('+', end="")
            else:
                print("|", end='')

        #Linhas do Meio
        elif (i < colunas and comfim == False):
            if i == colunas - 1:
                print("|", end='')
            else:
                print(" ", end='')

        # Linha Final
        else:
            if i == colunas -1:
                print("+", end="")
            else:
                print('-', end='')
    print("")