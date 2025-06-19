"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'victor josé \tmalachias' # Imutável
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel.expandtabs(1))
print(string.capitalize().expandtabs(1))
print(string.upper().expandtabs(1))
print(string.expandtabs(tabsize=15)) # Aumenta o tamanho do tab, ou deixa a frase com o tamanho do tab
print(string.removeprefix('victor, ').expandtabs(1)) # Remove o prefixo
print(string.removesuffix('malachias')) # Remove o sufixo
print(string.replace('victor', 'LUIZ').expandtabs(1)) # Substitui a palavra
print(string.split(' ')) # Divide a string    
print(string.strip()) #???
print(string.swapcase()) # Inverte as letras, se era minusculo vira maiusculo e vice-versa
print(string.title())
print(string.zfill(30)) # Preenche com zeros a esquerda