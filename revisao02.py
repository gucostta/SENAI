"""
Desenvolva um programa que armazene quatro notas em uma lista e que apresente a
média final. Caso a média seja igual ou superior a 7, apresente a mensagem
“APROVADO”, caso contrário, armazenar a nota da prova final e recalcular a média.
Caso a nova média seja igual ou superior a 5, apresentar a mensagem “APROVADO”,
caso contrário, apresentar a mensagem “REPROVADO”.
"""

# Cria um vetor vazio para armazenar as notas
notas = []
Pfinal = []

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

for n in range(1):
    final = float(input(f"Digite a PROVA FINAL {n+1}ª nota: "))
    Pfinal.append(final)

if media >= 7:
    print("APROVADO!!")
else:
        print("REPROVADO")
if media <= 5:
    media + final
elif media >= 5:
    print("APROVADO!!")
else:
    print("REPROVADO!!")

