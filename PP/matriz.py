matriz = []; soma = 0, linha = []

for i in range(3):
    for j in range(3):
        valor = int(input(f"Digite um número para a matriz {i} {j}: "))
        linha.append(valor)
    matriz.append(linha)


for i in range(3):
    soma = soma + matriz[i][i]

print(soma)