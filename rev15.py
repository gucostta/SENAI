"""
15. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
número do aluno e o segundo representando a sua altura em centímetros. Encontre o
aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do
aluno mais baixo, junto com suas alturas.
"""

# Inicializar variáveis para armazenar o número e a altura do aluno mais alto e mais baixo
numero_aluno_mais_alto = 0
altura_aluno_mais_alto = 0
numero_aluno_mais_baixo = 0
altura_aluno_mais_baixo = float('inf')  # Inicializar com um valor muito alto para garantir que qualquer altura seja menor

# Ler os dez conjuntos de valores
for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do {i}º aluno: "))
    altura_aluno = float(input(f"Digite a altura (em centímetros) do {i}º aluno: "))

    # Verificar se o aluno é o mais alto
    if altura_aluno > altura_aluno_mais_alto:
        numero_aluno_mais_alto = numero_aluno
        altura_aluno_mais_alto = altura_aluno

    # Verificar se o aluno é o mais baixo
    if altura_aluno < altura_aluno_mais_baixo:
        numero_aluno_mais_baixo = numero_aluno
        altura_aluno_mais_baixo = altura_aluno

# Mostrar o número e a altura do aluno mais alto e mais baixo
print("\nAluno mais alto:")
print("Número:", numero_aluno_mais_alto)
print("Altura:", altura_aluno_mais_alto, "cm")

print("\nAluno mais baixo:")
print("Número:", numero_aluno_mais_baixo)
print("Altura:", altura_aluno_mais_baixo, "cm")
