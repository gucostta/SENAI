"""
9. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A - álcool, G - gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro
do álcool é R$ 1,90.
"""

def calcular_valor_pago(tipo_combustivel, litros_vendidos):
    # Preços por litro
    preco_gasolina = 2.50
    preco_alcool = 1.90
    
    # Definir o preço por litro e o desconto com base no tipo de combustível
    if tipo_combustivel == 'A':
        preco_por_litro = preco_alcool
        if litros_vendidos <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo_combustivel == 'G':
        preco_por_litro = preco_gasolina
        if litros_vendidos <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    else:
        print("Tipo de combustível inválido")
        return None

    # Calcular o valor total sem desconto
    valor_bruto = preco_por_litro * litros_vendidos
    # Calcular o valor do desconto
    valor_desconto = valor_bruto * desconto
    # Calcular o valor final a ser pago
    valor_pago = valor_bruto - valor_desconto

    return valor_pago

# Solicitar a quantidade de litros vendidos e o tipo de combustível
litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Calcular o valor a ser pago pelo cliente
valor_pago = calcular_valor_pago(tipo_combustivel, litros_vendidos)

# Verificar se o valor foi calculado e imprimir o resultado
if valor_pago is not None:
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")
