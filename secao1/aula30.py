"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) [Quanto mais afastado da borda, mais complexo(ruim)]
"""

velocidade = 61
local_carro = 101

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR_1:
    print("Velocidade acima do permitido")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("Você foi multado")