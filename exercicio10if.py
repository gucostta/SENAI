"""
Faça um programa em Python que receba um valor de uma compra. Testar se o
cliente gastou até R$ 100,00, deve pagar em dinheiro. Se gastou entre R$ 100,00 e
R$ 300,00, deve pagar no cartão de débito. Se gastou acima de R$ 300,00, pode
pagar no cartão de crédito.

"""

# Solicitar ao usuário o valor da compra
valor_compra = float(input("Digite o valor da compra: R$"))

# Verificar a forma de pagamento com base no valor da compra
if valor_compra <= 100:
    print("Você deve pagar em dinheiro.")
elif 100 < valor_compra <= 300:
    print("Você deve pagar no cartão de débito.")
else:
    print("Você pode pagar no cartão de crédito.")
