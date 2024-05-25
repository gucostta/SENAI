"""
2. Desenvolva um programa que armazene quatro notas em uma lista e que apresente a
média final. Caso a média seja igual ou superior a 7, apresente a mensagem
“APROVADO”, caso contrário, armazenar a nota da prova final e recalcular a média.
Caso a nova média seja igual ou superior a 5, apresentar a mensagem “APROVADO”,
caso contrário, apresentar a mensagem “REPROVADO”.
"""

# Solicitar quatro notas do usuário
notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

# Calcular a média inicial
media_inicial = sum(notas) / len(notas)

# Verificar se a média inicial é suficiente para aprovação
if media_inicial >= 7:
    print(f"APROVADO com média {media_inicial:.2f}")
else:
    print(f"Média inicial {media_inicial:.2f} é insuficiente. É necessário fazer a prova final.")
    nota_final = float(input("Digite a nota da prova final: "))
    nova_media = (media_inicial + nota_final) / 2
    
    # Verificar se a nova média é suficiente para aprovação
    if nova_media >= 5:
        print(f"APROVADO com média {nova_media:.2f}")
    else:
        print(f"REPROVADO com média {nova_media:.2f}")
