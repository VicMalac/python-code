#O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira simplificada de identificá-lo é verificando-se apenas o ano de seu nascimento

ano = int(input('Em que ano você nasceu? '))
ano = ano % 12

match ano:
    case 0:
        print('Você nasceu no ano do macaco.')
    case 1:
        print('Você nasceu no ano do galo.')
    case 2:
        print('Você nasceu no ano do cão.')
    case 3:
        print('Você nasceu no ano do porco.')
    case 4:
        print('Você nasceu no ano do rato.')
    case 5:
        print('Você nasceu no ano do boi.')
    case 6:
        print('Você nasceu no ano do tigre.')
    case 7:
        print('Você nasceu no ano do coelho.')
    case 8:
        print('Você nasceu no ano do dragão.')
    case 9:
        print('Você nasceu no ano do serpente.')
    case 10:
        print('Você nasceu no ano do cavalo.')
    case 11:
        print('Você nasceu no ano do carneiro.')
    case _:
        print('Digite um ano válido por favor.')
    