"""
Agenda de Contatos:

Objetivo: Implementar um programa que permite ao usuário adicionar, remover, buscar e listar contatos. Cada contato deve conter nome, telefone e e-mail.
"""
nomes = []
telefones = []
num = 0
while True:
        parcont = int(input("[1] Adicionar Contato\n[2] Remover Contato\n[3] Ver Contatos\n[4] Buscar Contato\n[5] Encerrar Agenda\nEscolha uma opção: "))
        #system("cls")
        match parcont:
            case 1: # Contatos Adicionados (Funcionando)
                nome = input("Digite o nome do contato: ")
                nomes.append(nome)
                telefone = input("Digite o número de telefone do contato: ")
                telefones.append(telefone)
                print(nomes[len(nomes) - 1], telefone)
                continue
            case 2: # Remover Contatos (Em Processo)
                remove = input("Qual contato deseja remover: ")
                if nomes.count(remove) >= 2:
                    #remove = input("Existem contatos com informações iguais, qual deseja remover: ")
                    for nome in nomes: # Nome é uma str, então não dá para usar como contador
                        print(num, '-', nome)
                        num += 1
                elif telefones.count(remove) >= 2:
                    ...
                continue
            case 3: # Ver Contatos (Em Processo)
                for i in range(len(nomes)):
                    print(f'{nomes[i]}, {telefones[i]}')
                continue
            case 4: # Buscar Contatos (Em Processo)
                continue
            case 5: # Encerrar Agenda (Em Processo)
                print("Obrigado por utilizar a agenda! :)")
                break
            case _:
                print("Número Inválido!")
# try:
#     while True:
#         parcont = int(input("[1] Adicionar Contato\n[2] Remover Contato\n[3] Ver Contatos\n[4] Buscar Contato\n[5] Encerrar Agenda\nEscolha uma opção: "))
#         #system("cls")
#         match parcont:
#             case 1: # Contatos Adicionados (Funcionando)
#                 nome = input("Digite o nome do contato: ")
#                 nomes.append(nome)
#                 telefone = input("Digite o número de telefone do contato")
#                 telefones.append(telefone)
#                 print(nomes[len(nomes) - 1], telefone)
#                 continue
#             case 2: # Remover Contatos (Em Processo)
#                 continue
#             case 3: # Ver Contatos (Em Processo)
#                 for i in range(len(nomes)):
#                     print(nomes[i], telefones[i])
#                 continue
#             case 4: # Buscar Contatos (Em Processo)
#                 continue
#             case 5: # Encerrar Agenda (Em Processo)
#                 print("Obrigado por utilizar a agenda! :)")
#                 break
#             case _:
#                 print("Número Inválido!")



# except:
#     print("Um erro ocorreu")