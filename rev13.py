"""
13. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e
a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você
deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
com as notas restantes). As notas não são informadas ordenadas. Um exemplo de
saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9.04
"""

def calcular_media_notas(notas):
    # Remover a melhor e a pior nota
    notas_sem_extremos = sorted(notas)[1:-1]
    # Calcular a média das notas restantes
    media = sum(notas_sem_extremos) / len(notas_sem_extremos)
    return media

# Solicitar o nome do ginasta
nome_ginasta = input("Digite o nome do ginasta: ")

# Solicitar as notas dos sete jurados
notas = []
for i in range(7):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Calcular a média das notas após remover a melhor e a pior nota
media = calcular_media_notas(notas)

# Exibir o resultado final
print("\nResultado final:")
print("Atleta:", nome_ginasta)
print("Melhor nota:", max(notas))
print("Pior nota:", min(notas))
print("Média:", "{:.2f}".format(media))
