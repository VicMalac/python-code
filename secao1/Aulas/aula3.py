"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte #### Linguagem dinâmica significa que Python define o tipo da variável automaticamente
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

#? print(1234, "Luiz "Otávio"") Exemplo de erro

# Aspas simples
print('Luiz Otávio') ## Imprime texto normalmente usando aspas simples
print(1, 'Luiz "Otávio"') ## Maneira simples de se imprimir as aspas duplas em um texto usando aspas simples

# Aspas duplas
print("Luiz Otávio") ## Imprime texto normalmente usando aspas duplas
print(2, "Luiz 'Otávio'") ## Maneira simples de se imprimir as aspas simples em um texto com as aspas duplas

# Escape
print("Luiz \"Otávio\"") # Utiliza a contra barra (\) junto das aspas para imprimir no console as mesmas

# r
print(r"Luiz \"Otávio\"") # Utiliza o r antes da string para imprimir a contra barra (\) e as aspas duplas