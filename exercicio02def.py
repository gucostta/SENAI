"""
Faça um programa com uma função que receba dois números e retorne True
se o primeiro for múltiplo do segundo.

"""

def verificar_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

# Exemplo de uso da função
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = verificar_multiplo(num1, num2)
print("O primeiro número é múltiplo do segundo?", resultado)
