# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

num = []
for i in range(0, 3):
    nuum = int(input("Digite um número: "))
    num.append(nuum)
    maior = num[0] 
    meio = num[0] 
    menor = num[0]

for i in range(0, 3): 
    if num[i] > maior: # Se o valor do indice for maior do que o 'maior' que é == 4...
        maior = num[i] # maior = (O valor do indice)
    if num[i] < menor: # Se o valor do indice for menor do que o 'menor' que é == 4...
        menor = num[i] # menor = (O valor do indice)

for i in range(0, 3):
    if num[i] != maior and num[i] != menor:
        meio = num[i]
print(f"Maior: {maior}\nMeio: {meio}\nMenor: {menor}")




# num = [1, 2, 3]  # Lista com os números
# maior = num[0]
# menor = num[0]
# meio = num[0]

# # Encontrar maior e menor
# for i in range(1, 3):
#     if num[i] > maior:
#         maior = num[i]
#     if num[i] < menor:
#         menor = num[i]

# # O número do meio é aquele que não é nem o maior nem o menor
# for i in range(3):
#     if num[i] != maior and num[i] != menor:
#         meio = num[i]

# print(f"Maior: {maior}, Meio: {meio}, Menor: {menor}")
