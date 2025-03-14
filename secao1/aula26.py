"""
Formatação básica de strings
s - string
d - int
f - float

!<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >11}')
print(f'{variavel: <11}')
print(f'{variavel: ^11}')
print(f'{2505.14552585202548:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') # Não é o momento de uso