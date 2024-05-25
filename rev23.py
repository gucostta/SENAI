"""
23. Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km
rodado.
"""

# Solicitar ao usuário que insira a quantidade de km percorridos e a quantidade de dias de aluguel
km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

# Definir os preços
preco_diario = 60.00
preco_por_km = 0.15

# Calcular o preço total do aluguel
preco_total = (dias_aluguel * preco_diario) + (km_percorridos * preco_por_km)

# Exibir o preço total a ser pago
print("O preço total a pagar é R$", preco_total)
