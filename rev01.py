"""
1. Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
a. O produto do dobro do primeiro com a metade do segundo
b. A soma do triplo do primeiro com o terceiro
c. O terceiro elevado ao cubo
"""

# Solicitar dois números inteiros e um número real do usuário
primeiro_inteiro = int(input("Digite o primeiro número inteiro: "))
segundo_inteiro = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

# Calcular o produto do dobro do primeiro com a metade do segundo
resultado_a = (2 * primeiro_inteiro) * (segundo_inteiro / 2)

# Calcular a soma do triplo do primeiro com o terceiro
resultado_b = (3 * primeiro_inteiro) + numero_real

# Calcular o terceiro elevado ao cubo
resultado_c = numero_real ** 3

# Mostrar os resultados
print(f"a. O produto do dobro do primeiro com a metade do segundo é: {resultado_a}")
print(f"b. A soma do triplo do primeiro com o terceiro é: {resultado_b}")
print(f"c. O terceiro elevado ao cubo é: {resultado_c}")
