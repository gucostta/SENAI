"""
Faça um programa peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem
inversa à ordem lida.

"""

# Vetores para armazenar as idades e alturas
idades = []
alturas = []

# Loop para pedir a idade e a altura de 5 pessoas
for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    
    # Adiciona a idade e a altura aos vetores
    idades.append(idade)
    alturas.append(altura)

# Imprime as idades e alturas na ordem inversa
print("\nIdades e alturas na ordem inversa:")
for j in range(4, -1, -1):
    print(f"Idade: {idades[j]}, Altura: {alturas[j]} metros")
