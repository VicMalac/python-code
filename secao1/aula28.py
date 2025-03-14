"""
Exercício
Peça o nome
Peça a idade
Se nome e idade forem digitados
    Exiba:
    Seu nome é {nome} Facil normal
    Seu nome invertido é {nome_invertido} [::-i]
    Se nome contém (ou não) espaços True ou não
    Seu nome tem {n} letras len()
    A primeira letra do seu nome é {letra} [0]
    A última letra do seu nome é {letra} [-1]
Se nada for digitado em nome ou idade:
    Exiba:Exiba "Desculpe, você deixou campos vazios input = ... or " "
"""
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome and idade: 
    print(f"O seu nome é {nome}")
    print(f"O seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("O seu nome contém espaços")
    else:
        print("O seu nome não contém espaços")
    print(f"O seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")