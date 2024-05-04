"""
Faça um programa em Python que receba um valor de uma compra. Testar se o
cliente gastou até R$ 100,00, deve pagar em dinheiro. Se gastou entre R$ 100,00 e
R$ 300,00, deve pagar no cartão de débito. Se gastou acima de R$ 300,00, pode
pagar no cartão de crédito.

"""

def forma_pagamento(valor_compra):
    if valor_compra <= 100:
        return "Pagamento em dinheiro."
    elif valor_compra <= 300:
        return "Pagamento no cartão de débito."
    else:
        return "Pagamento no cartão de crédito."

# Função para ler o valor da compra
def ler_valor_compra():
    while True:
        try:
            valor = float(input("Digite o valor da compra: R$ "))
            if valor < 0:
                print("Por favor, digite um valor válido.")
            else:
                return valor
        except ValueError:
            print("Por favor, digite um valor válido.")

# Programa principal
valor_compra = ler_valor_compra()
forma = forma_pagamento(valor_compra)
print("Forma de pagamento:", forma)
