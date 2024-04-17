"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do
salário. Calcule o valor da prestação como sendo, o valor da casa a comprar
dividido pelo número de meses a pagar.

"""

valor_casa = float(input("Digite o valor da casa a comprar: "))
salario = float(input("Digite o seu salário: "))
anos_a_pagar = int(input("Digite a quantidade de anos a pagar: "))

meses_a_pagar = anos_a_pagar * 12

prestacao_mensal = valor_casa / meses_a_pagar

limite_prestacao = salario * 0.3

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print("Valor da prestação mensal: R$", prestacao_mensal)
else:
    print("Empréstimo negado! Valor da prestação excede 30% do salário.")
