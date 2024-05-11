"""
Faça um programa que leia 4 notas, armazene em um vetor e mostre as
notas e a média na tela.

"""

# Cria um vetor vazio para armazenar as notas
notas = []

# Loop para ler as 4 notas e adicionar ao vetor
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Exibe as notas e a média na tela
print("As notas digitadas são:")
for nota in notas:
    print(nota)

print(f"A média das notas é: {media}")
