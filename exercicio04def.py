"""
Faça um programa com uma função que receba a base e a altura de um
triângulo e retorne a sua área. Fórmula: A = (base * altura) / 2

"""

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Exemplo de uso da função
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area_triangulo = calcular_area_triangulo(base, altura)
print("A área do triângulo é:", area_triangulo)
