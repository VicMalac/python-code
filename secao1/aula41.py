# While / else

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == " ":
        break
    print(letra)
    i += 1

else:
    print('Não encontrei espaço.') #Não funciona com o break no  while