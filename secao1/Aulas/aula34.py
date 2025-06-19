"""
Repetições
while (enquanto)
Executa uma ação enquanti uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while True:
    nome = input('Qual é o seu nome? ')
    if nome == 'sair':
        break
    print(f'Olá {nome}!')
print('Acabou')