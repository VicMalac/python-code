### Variação de pontos flutuantes, final da seção 1 do curso de python
### Elaboração por conta própria um programa de controle de finanças, com adição de salario e extras, contas a pagar, e diversos
import decimal
numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print("Padrão: ", numero3) # Não dá 0.8 pelas imprecisões das linguagens
print(f'Format: {numero3:.2f}') # Formata o número (Oq faz dar 0.8)
print("Porcentagem: %f" % (numero3)) # Formata o número também
print("Função Round: ", round(numero3, 12)) # Função que arredonda para a quantia de casas decimais desejadas, nesse caso sendo 12

numero1 = decimal.Decimal(0.1) # Uso de classes para formatar (Ótimo para número muito grandes depois da vírgula)
numero2 = decimal.Decimal(0.7)
numero3 = numero1 + numero2
print("Decimal completo: ", numero3) # Bom para número muito grandes e que você precisa ser preciso, exemplo 0,0000000000000000000000001
