"""
🧠 Desafio: Sistema de Controle de Estacionamento
🎯 Objetivo
Simular um sistema de estacionamento simples que calcula o tempo que um carro ficou estacionado e o valor a pagar, com base nas regras de cobrança.

🚗 Regras do sistema
O usuário pode:

Registrar a entrada de um carro (placa e horário).

Registrar a saída de um carro (placa e horário).

Listar todos os carros estacionados no momento.

Ver quanto cada carro deve pagar ao sair.

Regras de cobrança (exemplo):

Até 1 hora: R$ 5,00

Até 2 horas: R$ 9,00

Até 3 horas: R$ 12,00

Acima de 3h: R$ 12,00 + R$ 3,00 por hora extra

O horário pode ser digitado no formato HH:MM (por exemplo, "14:30").

📦 Requisitos
Usar dicionário para armazenar carros com a placa como chave e horário de entrada como valor.

Calcular a diferença de horas entre entrada e saída (use datetime.strptime() para converter string em tempo).

Mostrar o valor que deve ser pago com base no tempo.

Permitir múltiplos carros no estacionamento.

💡 Extras opcionais
Bloquear placas duplicadas (não deixar registrar um carro já estacionado).

Adicionar um "log" de carros que já saíram.
"""
from datetime import datetime
from time import sleep
from os import system

entrada = 0
carro = {
    'DRH-8575' : {'entrada' : '12:30', 'saida' : '13:31', 'pagar' : ''},
    'CUY-5052' : {'entrada' : '13:51', 'saida' : '21:29', 'pagar' : ''},
}

placa = '0'; horaEntrada = '0'; horaSaida = '0'

pc, pv = list(carro.items())[0]

def calcularHora():
    for placa, horarios in carro.items():
        entrada = datetime.strptime(horarios['entrada'], "%H:%M")
        saida = datetime.strptime(horarios['saida'], '%H:%M')
        calculo = int((saida - entrada).total_seconds() // 3600)
        carro[placa]['pagar'] = f'{calculo}'


def registro(): # Registrando a entrada
    global placa, horaSaida, horaEntrada
    placa = input("Placa do carro: ").upper()
    if placa in carro:
        print("Este carro já está estacionado!")
        return 0
    horaEntrada = input("Entrada: ")
    horaSaida = input("Saída: ")
    carro[placa] = {
        'entrada': f'{horaEntrada}',
        'saida' : f'{horaSaida}'
    }
    print(f"{placa} registrado com sucesso!")


def listar():
    print('--- Carros Estacionados ---')
    for placa, horarios in carro.items():
        print(f"{placa} - Entrada: {horarios['entrada']} | Saída: {horarios['saida']} | Valor a pagar: R${horarios['pagar']}")


def pagar():
    for placa, horas in carro.items():
        pagamento = int(carro[placa]['pagar'])
        if pagamento == 1:
            carro[placa]['pagar'] = "5,00"
        elif pagamento == 2:
            carro[placa]['pagar'] = "9,00"
        elif pagamento <= 3 & pagamento > 2:
            carro[placa]['pagar'] = "12,00"
        else:
            carro[placa]['pagar'] = f"{12 + (pagamento - 3) * 3},00"


while entrada != "3":
    entrada = input("[1] Registrar carro\n"\
                    "[2] Listar carros\n"\
                    "[3] Sair\n"\
                    "Escolha uma opção: "
                    )
    system("cls")
    match entrada:
        case '1':
            registro()
        case '2':
            calcularHora()
            pagar()
            listar()
        case '3':
            print("Obrigado por usar o nosso programa de estacionamento!")
            break
        case _:
            print("Opção invalida!")


# placa = input("Digite a placa do carro (ou 'sair' para encerrar): ")
#     if placa.lower() == 'sair':
#         break

#     hora = input("Digite o horário de entrada do carro (formato HH:MM): ")
#     carro[placa] = hora  # Adiciona ao dicionário