primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite um valor: ")

if primeiro_valor == segundo_valor:
    print("Os valores são iguais")

elif primeiro_valor > segundo_valor:
    print(f"O {primeiro_valor=} é maior do que {segundo_valor=}")

else:
    print(f"O {segundo_valor=} é maior do que {primeiro_valor=}")