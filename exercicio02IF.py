"""

02. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para
inferiores ou iguais, 15%:

"""

salario = float(input("Digite o salario: "))

aumento1 = salario * 0.1
aumento2 = salario * 0.15

if salario > 1250:
    print("Aumento de 10%", aumento1)
else:
    salario <= 1250
    print("Aumento de 15%", aumento2)
