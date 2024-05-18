"""
3. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
a. Salário Bruto até 900 (inclusive) - isento
b. Salário Bruto até 1500 (inclusive) - desconto de 5%
c. Salário Bruto até 2500 (inclusive) - desconto de 10%
d. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
informações, dispostas conforme o exemplo abaixo. No exemplo o valor da
hora é 5 e a quantidade de hora é 220.
e. Dar a saída formatada como abaixo:
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS (10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de Descontos : R$ 165,00
Salário Líquido : R$ 935,00
"""

valor = float(input("Informe o valor de sua hora: "))
ht = float(input("Informe as horas trabalhadas: "))
bruto = valor * ht

ir = 0
inss = bruto * 0.1
fgts = bruto * 0.11
d0 = 0
d1 = bruto * 0.05
d2 = bruto * 0.10
d3 = bruto * 0.20


if bruto <= 900:
    ir = d0
elif bruto <= 1500:
    ir = d1
elif bruto <= 2500:
    ir = d2
else:
    ir = d3
    
td = inss + ir
liquido = bruto - td

    
print(f"Salário Bruto: ({valor} * {ht}): R$%6.2f" % bruto)
print(f"(-) IR (5): R$%6.2f" % ir)
print(f"(-) INSS (10): R$%6.2f" % inss)
print(f"FGTS (11): R$%6.2f" % fgts)
print(f"Total de Descontos: R$%6.2f" % td)
print(f"Salario Líquido: R$%6.2f" % liquido)
