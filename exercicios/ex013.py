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

# Quantidade de cedulas

notas = { # Uso de dicionários, o primeiro valor representado o nome de uma variável e o restante, o seu valor
    100: 5,
    50: 5,
    20: 5,
    10: 5,
    5: 5,
    2: 5
}
# Criar um programa que simule um caixa eletrônico. Ele deve receber um valor a ser sacado e retornar quantas notas de cada valor serão entregues, com base nas notas disponíveis.

valorSacar = int(input("Digite quanto deseja sacar: "))
saquePossivel = 0
# valor de valorSacar = 120 supondo
for valor, quantidade in notas.items():
    if valorSacar > valor and quantidade > 0:
        daParaTrocar = True
        for i in range(quantidade):
            print(f"Valor {valor}");print(valorSacar)
            saquePossivel += valorSacar - valor; valorSacar -= (valor )
            quantidade -= 1
            print(f"Valor sacar: {valorSacar}")
    else:
        daParaTrocar = False
    
    if daParaTrocar == True:
        print(f"Troquei por {valor}")
print(f"Valor sacado: {saquePossivel}")