"""
3. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
valor do salario e a porcentagem do aumento. Exiba o valor do aumento e do
novo salário. Para exemplo, teste a porcentagem de aumento de 5%.
"""

n1 = float(input("Digite seu salario atual:"))
n2 = int(input("Digite a porcentagem de aumento desejada:"))

aumento = n1 / 100 * n2

print("Seu aumento foi de:", aumento)
