# 🧠 Desafio: Jogo de Batalha de Dados (Estilo RPG)
# 🎯 Objetivo
# Criar um mini-jogo onde o jogador enfrenta um inimigo em batalhas por turnos, com ataques baseados em sorte (dados aleatórios).

# ⚔️ Regras do Jogo
# Cada jogador (você e o inimigo) começa com 100 de vida.

# A cada turno:

# O jogador escolhe: Atacar, Curar ou Desistir

# O inimigo ataca automaticamente com um dano aleatório (ex: de 5 a 15)

# Se o jogador atacar:

# Rola um dado (ex: randint(10, 20)) para causar dano no inimigo

# Se o jogador curar:

# Recupera uma quantidade aleatória de vida (ex: randint(5, 15))

# Mas o inimigo ainda ataca naquele turno

# Se o jogador desistir, o jogo termina

# O jogo termina quando:

# A vida do jogador ou do inimigo chega a 0

# O jogador desiste

# 🧱 Estrutura sugerida
# Usar random.randint() para simular dados

# Controle de turnos com while True

# Mostrar a cada turno:

# Vida do jogador e do inimigo

# Ação realizada

# Resultado do turno

# 💡 Extras opcionais
# Adicionar níveis (fases com inimigos mais fortes)

# Criar uma barra de vida com # no terminal

# Permitir o uso de "itens" como poções com quantidade limitada

# ! ######################################################### ! #

# Criar um mini-jogo onde o jogador enfrenta um inimigo em batalhas por turnos, com ataques baseados em sorte (dados aleatórios).

# ⚔️ Regras do Jogo

# O inimigo ataca automaticamente com um dano aleatório (ex: de 5 a 15)

# Se o jogador atacar:

# Rola um dado (ex: randint(10, 20)) para causar dano no inimigo

from random import randint

player = 100; inimigo = 100;


def atqEnemy(dano, inimigo):
    inimigo -= dano
    return inimigo
def atqPlayer(dano, player):
    player -= dano
    return player


while True:
    escolha = int(input("[1] Atacar \n[2] Curar \n[3] Desistir \nEscolha uma opção: "))
    match (escolha):
        case 1:
            atq = randint(10, 20); atkInimigo = randint(5, 15)
            player = atqEnemy(atkInimigo, inimigo)
            inimigo = atqPlayer(atq, player)
            print(f"Vida inimigo: {inimigo}\nVida Jogador: {player}")
        case 2:
            cura = randint(5, 15)
        case 3:
            exit()
        case _:
            print("Apenas escolha 1 a 3")