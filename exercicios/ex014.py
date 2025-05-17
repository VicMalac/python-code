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
import datetime
carro = {
    'DRH-8575' : "12:30"
}

hora_str = "18:30"
hora_obj = datetime.datetime.strptime(carro["DRH-8575"], "%H:%M")
print(hora_obj.time())
