"""
Repetições
while (enquanto)
Executa uma ação enquanti uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador >= 10 and contador <= 27:
        print('Não vou imprimir o número', contador)
        continue ## Pula para a próxima iteração (próximo laço)

    print(contador)

    if contador == 46:
        break ## Termina imediatamente o loop