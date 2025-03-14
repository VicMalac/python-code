"""
Fatiamento de strings
  012345678
  Olá Mundo
 -987654321
 Fatiamento [i:f:p] [::]
 Obs.: A funcção len retorna a qtd de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[2: 6])
print(len(variavel[1:4]))
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[:])