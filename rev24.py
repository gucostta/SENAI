"""
24. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = (basemaior + basemenor) * altura / 2
"""

# Solicitar ao usuário que insira os valores da base maior, base menor e altura
base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

# Calcular a área do trapézio usando a fórmula
area = (base_maior + base_menor) * altura / 2

# Exibir a área do trapézio
print("A área do trapézio é:", area)
