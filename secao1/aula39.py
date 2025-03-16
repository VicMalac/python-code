"""
Iterando strings com while  
"""

# Pega uma string exemplo 'Victor' e transforma em *V*i*c*t*o*r*

### Minha solução
nome = input("Digite o seu nome: ")
count = 0
print('*', end='')
while count < len(nome):
    print(f'{nome[count]}', end='*')
    count += 1

### Solução do professor  
print('')  
nome = 'Maria Helena'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)