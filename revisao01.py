"""
1. Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
a. O produto do dobro do primeiro com a metade do segundo
b. A soma do triplo do primeiro com o terceiro
c. O terceiro elevado ao cubo
"""

n1 = int(input("Informe um numero inteiro: "))
n2 = int(input("Informe outro numero inteiro: "))
n3 = float(input("Informe um numero real: "))

dobro = n1 * 2
metade = n2 / 2
triplo = n1 * 3
cubo = n3 ** 3

a = dobro + metade
b = triplo + n3
c = cubo

print("Letra a. é igual: ", a)
print("Letra b. é igual: ", b)
print("Letra c. é igual: ", c)
