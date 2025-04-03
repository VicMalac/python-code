### Variação de pontos flutuantes, final da seção 1 do curso de python
### Elaboração por conta própria um programa de controle de finanças, com adição de salario e extras, contas a pagar, e diversos
credito = "Não"
carro = "Não"
contas = "Não"
outros = "Não"

sal = float(input("Digite o seu salário: (Ex: R$ 1929.00) \nR$ "))
carro = input("Tem gasto com carro esse mês? (Gasolina, manutençao, etc) (Sim/Não) ")
credito = input("Tem gasto com crédito esse mês? (Sim/Não) ")
contas = input("Tem gasto com contas esse mês? (Sim/Não) ")
outros = input("Tem outros gastos esse mês? (Sim/Não) ")

if carro == "Sim":
    carro = int(input("Quanto irá gastar: "))
if