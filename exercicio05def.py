"""
Faça um programa com uma função que receba o raio (R) de um círculo e
retorne a sua área. Fórmula: A = pi * R2.

"""

import math

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

# Exemplo de uso da função
raio = float(input("Digite o valor do raio do círculo: "))

area_circulo = calcular_area_circulo(raio)
print("A área do círculo é:", area_circulo)
