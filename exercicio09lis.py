"""
Faça um programa que peça as 4 notas de 10 alunos, calcule a armazene em
um vetor a média de cada aluno, imprima o número de alunos com média
maior ou igual a 7.0.

"""

# Lista para armazenar as médias dos alunos
medias = []

# Loop para calcular a média de cada aluno
for aluno in range(10):
    notas = []  # Lista para armazenar as notas do aluno
    
    # Loop para pedir as 4 notas do aluno
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno {aluno+1}: "))
        notas.append(nota)
    
    # Calcula a média do aluno e armazena na lista de médias
    media_aluno = sum(notas) / len(notas)
    medias.append(media_aluno)

# Contador para contar o número de alunos com média maior ou igual a 7.0
alunos_aprovados = 0

# Loop para contar os alunos com média maior ou igual a 7.0
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

# Imprime o número de alunos aprovados
print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")
