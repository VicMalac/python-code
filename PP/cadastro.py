# Descrição:

# Você foi contratado para desenvolver um sistema básico de gerenciamento de funcionários para uma pequena empresa. O sistema deve ser capaz de receber e  armazenar informações sobre os funcionários e realizar operações básicas de manipulação desses dados.


# Requisitos:

# Utilize a função input() realizar um cadastro coletando dados do usuário, como nome, cidade e estado em que reside, idade, escolaridade, cargo e salário.


# Funcionalidades do Sistema:

# O sistema deve oferecer as seguintes funcionalidades:


# 1 - Adicionar um novo funcionário ao sistema, solicitando informações como nome, cargo, salário, e-mail, etc.


# 2- Atualizar as informações de um funcionário existente com base em um identificador único (como um número de identificação ou nome). Exibir informações de um funcionário específico.


# 3 - Listar todos os funcionários cadastrados.


# 4 - Permitir a remoção de um funcionário do sistema.


# Observações Finais: 

# Certifique-se de implementar um sistema de identificação único para cada funcionário. Valide as entradas do usuário para garantir que as operações sejam realizadas corretamente e sem erros. Documente adequadamente seu código com comentários explicativos para ajudar na compreensão. Esse projeto permite aos alunos praticar e consolidar conceitos fundamentais em Python, como operadores, estruturas de controle, estruturas de dados e funções, enquanto constroem um aplicativo útil para gerenciar informações de funcionários de uma empresa fictícia.


from os import system

nome = []; cidade = []; estado = []; idade = []; escolaridade = []; cargo = []; salario = []; id = []
proximoID = 0

def adicionarFunc():
    global proximoID
    print("--- Cadastro de novo funcionário ---")
    nome.append(input("Nome: "))
    cidade.append(input("Cidade: "))
    estado.append(input("Estado: "))
    idade.append(input("Idade: "))
    escolaridade.append(input("Escolaridade: "))
    cargo.append(input("Cargo: "))
    salario.append(input("Salário: "))
    id.append(proximoID)
    print(f'Funcionário cadastrado - ID {id[-1]}')
    proximoID += 1
    
def atualizarFunc():
    while True:
        try:
            atualizaID = int(input("Digite o ID do funcionário que deseja atualizar: "))
            break
        except:
            print("Digite um ID válido!")

    if atualizaID in id:
        i = id.index(atualizaID)
        nome[i] = input("Nome: ")
        cidade[i] = input("Cidade: ")
        estado[i] = input("Estado: ")
        idade[i] = input('Idade: ')
        escolaridade[i] = input('Escolaridade: ')
        cargo[i] = input('Cargo: ')
        salario[i] = input('Salário: ')
    else:
        print("ID não encontrado!")


def mostrarFunc():
    idx = len(id)
    for i in range(idx):
        print(f'ID: {id[i]} - Nome: {nome[i]}, Cidade: {cidade[i]}, Estado: {estado[i]}, Idade: {idade[i]}, Escolaridade: {escolaridade[i]}, Cargo: {cargo[i]}, Salário: {salario[i]}')

def removeFunc():
    while True:
        try:
            removeID = int(input("Digite o ID do funcionário que deseja remover: "))
            break
        except:
            print("ID inválido!")
            
    if removeID in id:
        index = id.index(removeID)
        nome.pop(index)
        cidade.pop(index)
        estado.pop(index)
        idade.pop(index)
        escolaridade.pop(index)
        cargo.pop(index)
        salario.pop(index)
        id.pop(index)
        print("Funcinário removido!")
    else:
        print("ID não encontrado!")


opcao = [
    "[1] Cadastrar novo funcionário",
    "[2] Atualizar cadastro de funcionário",
    "[3] Listar todos os funcionários cadastrados",
    "[4] Remover funcionário",
    "[5] Finalzar sistema"
    ]
while True:
    try:
            for i in range(len(opcao)):
                print(opcao[i])
            escolha = int(input("Escolha uma opção: "))
            system("cls")
            match escolha:
                case 1:
                    adicionarFunc()
                case 2:
                    atualizarFunc()
                case 3:
                    mostrarFunc()
                case 4:
                    removeFunc()
                case 5:
                    print("Obrigado por utilizar nosso sistema :)")
                    break
                case anotherCase:
                    print("Opção inválida")
    except:
            print("Digite um opção válida")