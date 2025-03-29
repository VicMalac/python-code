"""
Agenda de Contatos:

Objetivo: Implementar um programa que permite ao usuário adicionar, remover, buscar e listar contatos. Cada contato deve conter nome, telefone e e-mail.
"""
nomes = ['victor', 'victor', '123', 'rato']
telefones = ['123', '3321', '123', '4321']
print(telefones[1])

while True:
        num = 0
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
                remover = input("Qual contato deseja remover: ")
                if nomes.count(remover) >= 2:
                    for nome in nomes: # Nome é uma str, então não dá para usar como contador
                        print(f'nome[{num + 1}] - {nome}')
                        num += 1
                    remove = input("Existem contatos com nomes iguais, qual deseja remover: ")

                elif telefones.count(remover) >= 2:
                    for telefone in telefones:
                        print(f'tel[{num + 1}] - {telefone}')
                        num += 1
                    remove = input("Existem contatos com telefones iguais, qual deseja remover: ")

                else:
                    varn = nomes.index(remover) # 3

                    print(f"Indice: {varn}")

                    if remover in telefones:
                        telefones.remove(remover)
                        nomes.remove(telefones[varn])
                        print('telefone', telefones)
                        print('nome', telefones)
                    else:
                        nomes.remove(remover)
                        telefones.remove(telefones[varn])
                        print('telefone', telefones)
                        print('nome', telefones)

                continue




            case 3: # Ver Contatos (Funcionando)
                for i in range(len(nomes)):
                    print(f'{nomes[i]}, {telefones[i - 1]}')
                continue
            case 4: # Buscar Contatos (Em Processo)
                continue
            case 5: # Encerrar Agenda (Funcionando)
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