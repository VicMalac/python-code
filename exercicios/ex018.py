# Usar Funções

# def Mensagem():
#     print("Hello World!")

# def Msg():
#     return "Hello World"

# Mensagem()

# texto = Msg()
# print (texto)

# def AcharNota():
#     nota = int(input("Digite uma nota: "))
#     return nota

# def Resultado(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     if media >= 6:
#         print("Aprovado!")
#     elif media < 6 and media >= 4:
#         print("Recuperação!")
#     else:
#         print("Reprovado!")

# a = AcharNota()
# b = AcharNota()
# Resultado(a, b)

arquivo = open('arquivo.txt', 'w')
arquivo.write("Python \n")
arquivo.write("Criei um arquivo com o comando open write e close")
arquivo.close()

leitura = open("arquivo.txt", "r")
print(leitura.read())
leitura.close()

"""
r	Abre o arquivo somente para leitura.
O arquivo deve já existir.
r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
w	Abre o arquivo somente para escrita, no início do arquivo.
Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
a	Abre o arquivo para escrita no final do arquivo.
Não apaga o conteúdo preexistente.
a+	Abre o arquivo para escrita no final do arquivo e leitura.
"""