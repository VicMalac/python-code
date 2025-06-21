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
from os import system

entrada = ''
carro = {
    'DRH-8575' : {'entrada' : '12:30', 'saida' : '13:31', 'pagar' : ''},
    'CUY-5052' : {'entrada' : '13:51', 'saida' : '21:29', 'pagar' : ''},
}

placa = '0'; horaEntrada = '0'; horaSaida = '0'

def calcularHora():
    for placa, horarios in carro.items():
        if horarios['saida'] == '':
            continue
        entrada = datetime.strptime(horarios['entrada'], "%H:%M")
        saida = datetime.strptime(horarios['saida'], '%H:%M')
        calculo = int((saida - entrada).total_seconds() // 3600)
        carro[placa]['pagar'] = f'{calculo}'

def registro(escolha): # Registrando a entrada
    if escolha == '1':
        placa = input("Placa do carro: ").upper()
        if placa in carro:
            if carro[placa]['saida'] != '':
                opcao = input("Este carro já saiu, deseja adicionar outra entrada? ").lower()
                if opcao == "sim":
                    horaEntrada = input("Entrada: ")
                    carro[placa] = {
                    'entrada': f'{horaEntrada}',
                    'saida' : f''
                    }
                    return 0
                else:
                    return 0
        horaEntrada = input("Entrada: ")
        carro[placa] = {
        'entrada': f'{horaEntrada}',
        'saida' : f''
        }
        print(f"Entrada de {placa} registrada com sucesso!")
    elif escolha == '2':
        placa = input("Placa do carro: ").upper()
        if placa in carro:
            if carro[placa]['saida'] != '':
                print("Este carro já saiu!")
            else:
                horaSaida = input("Saída: ")
                carro[placa]['saida'] = f'{horaSaida}'
                print(f"Saída de {placa} registrada com sucesso!")
        else:
            print("Essa placa não existe")


def listar():
    print('--- Carros Estacionados ---')
    for placa, horarios in carro.items():
        if horarios['saida']:
            print(f"{placa} - Entrada: {horarios['entrada']} | Saída: {horarios['saida']} | Valor a pagar: R${horarios['pagar']:.2f}")
        else:
            print(f"{placa} - Entrada: {horarios['entrada']} | Aguardando saída")


def saidas():
    print("--- Log de Saídas ---")
    for placa, horarios in carro.items():
        if horarios['saida'] != '':
            print(f"{placa} - Saída às {horarios['saida']}")

def pagar():
    for placa, horas in carro.items():
        if not horas['saida']:
            continue
        pagamento = int(carro[placa]['pagar'])
        if pagamento == 1:
            carro[placa]['pagar'] = 5.00
        elif pagamento == 2:
            carro[placa]['pagar'] = 9.00
        elif 2 < pagamento <= 3:
            carro[placa]['pagar'] = 12.00
        else:
            carro[placa]['pagar'] = 12.00 + (pagamento - 3) * 3


while entrada != "5":
    entrada = input("[1] Registrar entrada\n"\
                    "[2] Registrar saída\n"
                    "[3] Listar carros\n"\
                    "[4] Log de saídas\n"\
                    "[5] Sair\n"\
                    "Escolha uma opção: "
                    )
    system("cls")
    match entrada:
        case '1':
            registro(entrada)
        case '2':
            registro(entrada)
        case '3':
            calcularHora()
            pagar()
            listar()
        case '4':
            saidas()
        case '5':
            print("Obrigado por usar o nosso programa de estacionamento!")
            break
        case _:
            print("Opção invalida!")



# placa = input("Digite a placa do carro (ou 'sair' para encerrar): ")
#     if placa.lower() == 'sair':
#         break

#     hora = input("Digite o horário de entrada do carro (formato HH:MM): ")
#     carro[placa] = hora  # Adiciona ao dicionário