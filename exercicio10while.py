# Leitura do valor da compra
valor_compra = float(input("Digite o valor da compra: R$"))

# Verificação do método de pagamento
if valor_compra <= 100:
    print("Pagamento em dinheiro.")
elif valor_compra <= 300:
    print("Pagamento no cartão de débito.")
else:
    print("Pagamento no cartão de crédito.")
