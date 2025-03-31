
from os import system
items = ['milk', 'beans', 'coffe']
OPTIONS = ['[1] Add a Product',
          '[2] Remove a Product',
          '[3] List Products',
          '[4] Close the List']
for i in range(len(OPTIONS)):
    print(OPTIONS[i])
choice = int(input("Choose an option: "))
system("cls")
match choice:
            case 1: # Add a Product
                product = input('Type a product you want to add: ')
                if not product:
                    print("You must add a product!")
                items.append(product)
                print(items)

            case 2: # Remove a Product
                system('cls')
                for index, i in enumerate(items, start= 1):
                    print(index, i.title())
                removeProduct = int(input("Which product do you want to remove: "))
                if not removeProduct or not removeProduct in items:
                    print("Type a valid product!")
                print(f"The product {removeProduct} has been removed. ")
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

            case _: # Invalid Option
                ...