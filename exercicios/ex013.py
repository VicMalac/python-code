"""
🧠 Desafio: Simulador de Caixa Eletrônico com Controle de Notas
🎯 Objetivo
Criar um programa que simule um caixa eletrônico. Ele deve receber um valor a ser sacado e retornar quantas notas de cada valor serão entregues, com base nas notas disponíveis.

💵 Notas disponíveis
R$100

R$50

R$20

R$10

R$5

R$2

📝 Regras
O caixa tem um número limitado de notas.
Exemplo inicial:

notas = {
    100: 5,
    50: 5,
    20: 5,
    10: 5,
    5: 5,
    2: 5
}

O usuário digita um valor a sacar. O programa:

Verifica se o valor é possível com as notas disponíveis.

Exibe quantas notas de cada valor foram entregues.

Atualiza o "estoque" de notas do caixa.

Se não for possível sacar o valor (por falta de notas ou valor inválido), deve avisar o usuário com uma mensagem clara.

O programa continua até o usuário digitar "0" para sair.

🧠 Extras opcionais (se quiser deixar mais difícil):
Mostrar o total de dinheiro restante no caixa.

Permitir o “reabastecimento” manual das notas.

Implementar senha para acessar a área de manutenção.###
"""

notas = { # Uso de dicionários, o primeiro valor representado o nome de uma variável e o restante, o seu valor
    100: 5,
    50: 5,
    20: 5,
    10: 5,
    5: 5,
    2: 5
}
# Criar um programa que simule um caixa eletrônico. Ele deve receber um valor a ser sacado e retornar quantas notas de cada valor serão entregues, com base nas notas disponíveis.

saquePossivel = 0; soma = 0
notasUsadas = {
    100 : 0,
    50 : 0,
    20 : 0,
    10 : 0,
    5 : 0,
    2 : 0
}
# valor de valorSacar = 120 supondo
for i, j in notas.items(): #Verificação da quantia total do valor de notas
    soma += (i * j)

while True:
    for i, j in notasUsadas.items():
        notasUsadas[i] = 0
    valorSacar = int(input("Digite quanto deseja sacar: "))
    if valorSacar == 0:
        break
    for valor, quantidade in notas.items():
        if valorSacar >= valor and quantidade > 0:
            daParaTrocar = True
            for i in range(quantidade):
                if valorSacar > soma:
                    ("Não existem notas o suficiente para sacar esse valor!")
                    continue
                if valorSacar % 2 != 0 and valorSacar % 5 != 0 and notas[2] > 0: # Caso seja 131 por exemplo, uma nota de 100 uma nota de 20 outra de 5 e três de 2
                    valorSacar -= 2
                    saquePossivel += 2
                    notas[2] -= 1 ;notasUsadas[2] += 1
                    continue

                if valorSacar >= valor:
                    saquePossivel += valor; valorSacar -= (valor )
                    quantidade -= 1; notas[valor] -= 1
                    notasUsadas[valor] += 1
                else:
                    continue
    print(notas)
    print(f"Valor total sacado: {saquePossivel}")
    for i, j in notasUsadas.items():
        if j == 0:
            continue
        print(f"Você recebeu {j} notas {i}")