"""
🧠 Desafio: Sistema de Atendimento Prioritário (Tipo SUS)
🎯 Objetivo
Criar um sistema que simula a fila de atendimento de uma clínica, com prioridade para idosos (60 anos ou mais).

🧑‍⚕️ Regras do sistema
O sistema deve exibir um menu com opções:

Adicionar paciente (nome e idade)

Chamar próximo paciente

Listar fila de espera

Sair

O sistema deve manter duas filas:

Prioritária (idosos, idade ≥ 60)

Normal (restante)

A lógica para chamada de pacientes:

Para cada 3 pacientes normais, 1 prioritário é chamado (caso exista).

Mas se a fila normal estiver vazia, só chama da prioritária, e vice-versa.

O nome e a idade do paciente devem ser armazenados.

🧱 Exemplo de estrutura de dados
fila_prioritaria = []
fila_normal = []
Cada elemento pode ser uma tupla:

("João", 65)
("Maria", 35)
💡 Extras opcionais
Mostrar posição do paciente na fila ao ser adicionado.

Permitir remover paciente da fila (caso ele desista).

Mostrar tempo médio de espera estimado (fixo, por exemplo, 5 min por paciente).
"""

# ? Adicionar paciente (nome e idade)

# ? Chamar próximo paciente

# ? Listar fila de espera

# ! Sair

try:
    while True:
        opcao = input("[1] Adicionar Paciente \n[2] Chamar próximo paciente\n[3] Listar fila de espera\n[4] Sair \nEscolha uma Opção: ")
except:
    ...