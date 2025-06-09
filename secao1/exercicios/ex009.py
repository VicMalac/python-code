# Mostre os primeiros n números da sequência de Fibonacci.
# 1 1 2 3 5 8 13 21 34 55 89 144 233

num = int(input('Digite um número: '))
x = 1
y = 1

for i in range(1, num, 2):
    print(f'{x}', end = ' ')
    print(f'{y}', end = ' ')
    x += y
    y += x

if num % 2 != 0:
    print(f'{x}', end = ' ')