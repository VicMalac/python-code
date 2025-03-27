# Considerando um número inteiro ímpar, digitado pelo usuário, exiba na tela um diamante, por exemplo, se o usuário digitou nove, devemos obter a seguinda saída:
"""
    *    
   ***   
  *****
 *******
*********
 *******
  *****
   ***  
    * 
"""

num = int(input('Digite um número ímpar: '))
linha = num
coluna = num
for i in range(num):
    for i in range(num):
        if num - i == 0:
            print("#", end="")
        else:
            print("0", end='')
    print("")


# for i in range(num):
#     if (num-1) - i != 0: # 0 - 8 != 0 True; 8 - 8 != 0 True
#         print("0", end='')
#     else:
#         print("1")