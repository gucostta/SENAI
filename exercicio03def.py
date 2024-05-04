"""
Faça um programa com uma função que receba o lado (l) de um quadrado e
retorne a sua área (A = lado2).

"""

def calcular_area_quadrado(lado):
    area = lado ** 2
    return area

# Exemplo de uso da função
lado = float(input("Digite o tamanho do lado do quadrado: "))

area_quadrado = calcular_area_quadrado(lado)
print("A área do quadrado é:", area_quadrado)
