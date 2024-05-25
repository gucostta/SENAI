"""
8. Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor
do novo salário reajustado de acordo com a tabela abaixo:
Salário Atual Reajuste
Abaixo de R$ 500,00 15%
De R$ 500,00 até R$ 1000,00 10%
Acima de R$ 1000,00 5%
"""

def calcular_reajuste(salario_atual):
    if salario_atual < 500:
        reajuste = 0.15
    elif 500 <= salario_atual <= 1000:
        reajuste = 0.10
    else:
        reajuste = 0.05

    novo_salario = salario_atual * (1 + reajuste)
    return novo_salario

# Solicitar o salário atual do funcionário
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

# Calcular o novo salário com reajuste
novo_salario = calcular_reajuste(salario_atual)

# Imprimir o resultado
print(f"O novo salário reajustado é: R$ {novo_salario:.2f}")
