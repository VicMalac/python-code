"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) [Quanto mais afastado da borda, mais complexo(ruim)]
"""

velocidade = 61
local_carro = 98

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passar_radar1 = velocidade > RADAR_1 # True

carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) # local_carro == 100 == True

carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passar_radar1 #X = True and True ou seja X == True

if velocidade_carro_passar_radar1: # se True ...
    print("Velocidade do radar 1 excedida")

if carro_multado_radar1 and velocidade_carro_passar_radar1:
    print("Carro multado em radar 1")

else: 
    print("O seu carro não foi multado")