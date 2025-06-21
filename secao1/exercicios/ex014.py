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