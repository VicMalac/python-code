# Desenvolver uma rotina que a partir de um caractere e uma determinada quantidade de linhas e colunas, todos fornecidoss pelo usuuário, realize a repetição do respectivo caractere na quantidade de linhas e colunas que foram digitadas. Por exemplo:

"""
?Entrada:
Linhas: 3
Colunas: 5
Caractere: X

?Saída:
XXXXX
XXXXX
XXXXX
"""
from os import system

linha = int(input("Linhas: "))
coluna = int(input("Colunas: "))
char = input("Caractere: ")
system("cls")
for i in range(linha):
    for i in range(coluna):
        print(char, end = "")
    print("")