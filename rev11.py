"""
11. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg Acima de 5 Kg
Morango R$ 2,50 por Kg R$ 2,20 por Kg
Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$
25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""
# Definir os preços por Kg das frutas
preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

# Solicitar a quantidade de Kg de morangos e maçãs adquiridos
kg_morangos = float(input("Digite a quantidade de Kg de morangos adquiridos: "))
kg_macas = float(input("Digite a quantidade de Kg de maçãs adquiridas: "))

# Calcular o preço total dos morangos
if kg_morangos <= 5:
    preco_total_morangos = kg_morangos * preco_morango_ate_5kg
else:
    preco_total_morangos = kg_morangos * preco_morango_acima_5kg

# Calcular o preço total das maçãs
if kg_macas <= 5:
    preco_total_macas = kg_macas * preco_maca_ate_5kg
else:
    preco_total_macas = kg_macas * preco_maca_acima_5kg

# Calcular o preço total da compra
preco_total_compra = preco_total_morangos + preco_total_macas

# Aplicar o desconto se necessário
if kg_morangos + kg_macas > 8 or preco_total_compra > 25:
    desconto = 0.10 * preco_total_compra
    preco_total_compra -= desconto

# Imprimir o valor a ser pago pelo cliente
print(f"Valor a ser pago pelo cliente: R$ {preco_total_compra:.2f}")

