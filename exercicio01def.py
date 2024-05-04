"""
Faça um programa com uma função que retorne o maior de dois números.

"""


def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Exemplo de uso da função
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = maior_numero(num1, num2)
print("O maior número é:", resultado)
