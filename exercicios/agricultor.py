# Exercício da InterFatec 2025 (Agricultor)

from os import system

t = 0.0 # Indica o risco de evaporação da água no solo
u = 0.0 # Quantidade de água presente no solo e disponível para as plantas
p = False # Indica se há expectativa de chuva para o período
rnr = [] # rnr == Regar Não Regar
tup = input() # Dessa maneira sempre será uma string

for i in range(int(tup)):
    lista = input().split()
    t = float(lista[0])
    u = float(lista[1])
    p = int(lista[2])
    if p == 1:
        rnr.append("NÃO REGAR")
        continue
    rnr.append("REGAR" if t > 30.0 and u < 50.0 else "NÃO REGAR")

system("cls")
for i in range(int(tup)):
    print(rnr[i])