"""
Faça um lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de indiices  inexistentes na lista.
"""
from os import system
items = ['milk', 'beans', 'coffe']
OPTIONS = ['[1] Add a Product',
          '[2] Remove a Product',
          '[3] List Products',
          '[4] Close the List']

while True:
    try:
        for i in range(len(OPTIONS)):
            print(OPTIONS[i])
        choice = int(input("Choose an option: "))
        system("cls")
        match choice:
            case 1: # Add a Product
                product = input('Type a product you want to add: ').lower()
                if not product:
                    print("You must add a product!")
                    continue
                elif product.isdigit():
                    print("Only words are allowed")
                    continue
                items.append(product)

            case 2: # Remove a Product
                system('cls')
                for index, i in enumerate(items, start= 1):
                    print(index, i.title())
                removeProduct = input("Which product do you want to remove: ").lower()
                if not removeProduct or not removeProduct in items:
                    print("Type a valid product!")
                    continue
                print(f"The product {removeProduct.title()} has been removed. ")
                items.remove(removeProduct)

            case 3: # List Products
                system('cls')
                print("Products at the moment")
                for index, i in enumerate(items, start= 1):
                    print(index, i.title())

            case 4: # Close the List
                system('cls')
                print("Complete product list")
                for index, i in enumerate(items, start=1):
                    print(index, i.title())
                break

            case _: # Invalid Option
                system("cls")
                print("Type a valid option!")
    except: # Error Message
        system("cls")
        print("Type a valid option!")
        continue