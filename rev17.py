"""
17. O Hipermercado PagSempreMais está com uma promoção de carnes que é imperdível.
Confira:
Até 5 Kg Acima de 5 Kg
Filé Duplo R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
compra for feita no cartão PagSempreMais o cliente receberá ainda um desconto de
5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de
carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do
desconto e valor a pagar.
"""

# Definir os preços por Kg das carnes
precos = {
    "Filé Duplo": {"até 5 Kg": 4.90, "acima de 5 Kg": 5.80},
    "Alcatra": {"até 5 Kg": 5.90, "acima de 5 Kg": 6.80},
    "Picanha": {"até 5 Kg": 6.90, "acima de 5 Kg": 7.80}
}

# Solicitar ao usuário o tipo de carne e a quantidade
tipo_carne = input("Digite o tipo de carne (Filé Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade de carne (em Kg): "))

# Verificar se a compra foi feita no cartão PagSempreMais
pagamento_cartao = input("A compra foi feita no cartão PagSempreMais? (sim/não): ").lower() == "sim"

# Calcular o preço total da compra
if quantidade <= 5:
    preco_total = quantidade * precos[tipo_carne]["até 5 Kg"]
else:
    preco_total = quantidade * precos[tipo_carne]["acima de 5 Kg"]

# Aplicar o desconto de 5% se a compra foi feita no cartão PagSempreMais
if pagamento_cartao:
    desconto = 0.05 * preco_total
    preco_total -= desconto
    tipo_pagamento = "Cartão PagSempreMais"
else:
    desconto = 0
    tipo_pagamento = "Outros meios de pagamento"

# Exibir o cupom fiscal
print("\nCupom Fiscal")
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "Kg")
print("Preço total: R$", "{:.2f}".format(preco_total))
print("Tipo de pagamento:", tipo_pagamento)
print("Valor do desconto: R$", "{:.2f}".format(desconto))
print("Valor a pagar: R$", "{:.2f}".format(preco_total))
