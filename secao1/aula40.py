# Calculadora com while

while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    opr = input("Digite o operador Ex:\n[+] Adição\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n[**]Potenciação\n[//]Divisão Inteira\n[%] Módulo\n: ")


    if opr == '+': # Adição
            print(f'{num1} + {num2} = {float(num1) + float(num2)}')
    elif opr == '-': # Subtração
            print(f'{num1} - {num2} = {float(num1) - float(num2)}')
    elif opr == '*': # Multiplicação
            print(f'{num1} * {num2} = {float(num1) * float(num2)}')
    elif opr == '/': # Divisão
            print(f'{num1} / {num2} = {float(num1) / float(num2)}') ## Analisar
    elif opr == '**': # Potenciação
            print(f'{num1} ** {num2} = {float(num1) ** float(num2)}')
    elif opr == '//': # Divisão inteira
            print(f'{num1} // {num2} = {float(num1) // float(num2)}')
    elif opr == '%': # Modulo
        print(f'{num1} % {num2} = {float(num1) % float(num2):.1f}')
        

    sair = input("Deseja sair? [s]im ou [n]ão: ").lower().startswith('s')
    if sair:
        break