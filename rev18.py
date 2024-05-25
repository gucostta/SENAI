"""
18. Faça um programa que calcule a média ponderada de um aluno. Leia três notas, a
primeira nota tem peso 2, a segunda nota tem peso 3 e a terceira nota tem peso 5.
Calcule a média ponderada e imprima o resultado na tela. Considere que cada nota
pode ir de 0 a 10.0.
"""

# Solicitar ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota (de 0 a 10): "))
nota2 = float(input("Digite a segunda nota (de 0 a 10): "))
nota3 = float(input("Digite a terceira nota (de 0 a 10): "))

# Definir os pesos das notas
peso1 = 2
peso2 = 3
peso3 = 5

# Calcular a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibir o resultado
print("A média ponderada do aluno é:", media_ponderada)
