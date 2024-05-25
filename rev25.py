"""
25. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
 Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
 Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
 A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.
"""

# Definir as variáveis
ano_contratacao = 1995
salario_inicial = 1000.00
ano_atual = 2024

# Calcular o salário atual do funcionário
salario_atual = salario_inicial
percentual_aumento = 0.015  # 1.5% de aumento em 1996

for ano in range(ano_contratacao + 1, ano_atual + 1):
    percentual_aumento *= 2  # Aumento é o dobro do ano anterior
    aumento = salario_atual * percentual_aumento
    salario_atual += aumento

# Exibir o salário atual do funcionário
print("O salário atual do funcionário é R$ {:.2f}".format(salario_atual))

#==========================================================================================================

# Solicitar ao usuário que insira o salário inicial do funcionário
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

# Calcular o salário atual do funcionário
salario_atual = salario_inicial
percentual_aumento = 0.015  # 1.5% de aumento em 1996

for ano in range(ano_contratacao + 1, ano_atual + 1):
    percentual_aumento *= 2  # Aumento é o dobro do ano anterior
    aumento = salario_atual * percentual_aumento
    salario_atual += aumento

# Exibir o salário atual do funcionário
print("O salário atual do funcionário é R$ {:.2f}".format(salario_atual))
