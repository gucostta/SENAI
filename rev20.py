"""
20. Com a ajuda do fluxograma, crie um programa em Python que calcula o custo total e o
troco, de itens comprados.
"""

# Iniciar: Ler o preço por unidade
preco_por_unidade = float(input("Digite o preço por unidade: "))

# Ler a quantidade e o valor pago
quantidade = int(input("Digite a quantidade de itens comprados: "))
valor_pago = float(input("Digite o valor pago: "))

# Calcular o custo total
custo_total = quantidade * preco_por_unidade

# Calcular o troco
troco = valor_pago - custo_total

# Exibir quantidade de itens comprados, custo total e troco
print("\nQuantidade de itens comprados:", quantidade)
print("Custo total:", custo_total)
print("Troco:", troco)

# Fim
