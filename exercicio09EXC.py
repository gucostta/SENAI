"""
Crie um programa que leia um número e calcule sua raiz quadrada, tratando
a exceção se o número for negativo.
"""

import math

def calcular_raiz_quadrada():
    try:
        # Solicita ao usuário para inserir um número
        entrada = input("Digite um número: ")
        
        # Tenta converter a entrada para um número float
        numero = float(entrada)
        
        # Verifica se o número é negativo
        if numero < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        
        # Calcula a raiz quadrada do número
        raiz_quadrada = math.sqrt(numero)
        
    except ValueError as e:
        # Trata o caso em que a entrada não pode ser convertida para um float
        # ou o caso em que o número é negativo
        print(f"Erro: {e}")
    else:
        # Se não houver exceção, imprime a raiz quadrada
        print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

# Chama a função para executar o programa
calcular_raiz_quadrada()
