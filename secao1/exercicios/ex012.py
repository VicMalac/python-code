a = 21
b = 9
c = 6

print(f'A: {a}\nB: {b} \nC: {c}\n')
b = b - a
a = b + a
b = a - b

c = c - a
a = c + a
c = a - c

print(f'A: {a}\nB: {b} \nC: {c}')