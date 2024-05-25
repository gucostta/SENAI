"""
16. Faça um programa que receba um número digitado pelo usuário e calcule a soma de
todos os números de 1 até ao número digitado. Por exemplo, se o usuário digitou o
número 4, a saída deve ser 10.
"""

# Solicitar ao usuário que digite um número
numero = int(input("Digite um número: "))

# Calcular a soma de todos os números de 1 até o número digitado
soma = numero * (numero + 1) // 2

# Exibir o resultado
print("A soma de todos os números de 1 até", numero, "é", soma)
