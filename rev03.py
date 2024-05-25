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

# Solicitar o valor da hora e a quantidade de horas trabalhadas no mês
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcular o desconto do Imposto de Renda (IR)
if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 0.05
elif salario_bruto <= 2500:
    ir_percentual = 0.10
else:
    ir_percentual = 0.20

desconto_ir = salario_bruto * ir_percentual

# Calcular o desconto do INSS (10%)
desconto_inss = salario_bruto * 0.10

# Calcular o FGTS (11%, não descontado)
fgts = salario_bruto * 0.11

# Calcular o desconto do Sindicato (3%)
desconto_sindicato = salario_bruto * 0.03

# Calcular o total de descontos
total_descontos = desconto_ir + desconto_inss + desconto_sindicato

# Calcular o salário líquido
salario_liquido = salario_bruto - total_descontos

# Imprimir as informações formatadas
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual * 100:.0f}%) : R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%) : R$ {desconto_inss:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de Descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
