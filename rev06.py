"""
6. Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se
o mesmo é: equilátero, isósceles ou escaleno. Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
- Triângulo equilátero – três lados iguais
- Triângulo isósceles – quaisquer dois lados iguais
- Triângulo escaleno – três lados diferentes
"""

def tipo_triangulo(lado1, lado2, lado3):
    # Verificar se os lados podem formar um triângulo
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        # Verificar o tipo de triângulo
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"

# Programa principal que solicita os lados do triângulo ao usuário
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Determinar o tipo de triângulo
resultado = tipo_triangulo(lado1, lado2, lado3)

# Imprimir o resultado
print(f"Os lados informados formam um triângulo {resultado}")
