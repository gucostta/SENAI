# Lista para armazenar os pesos
pesos = []

# Lê os pesos das cinco pessoas
for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    pesos.append(peso)

# Encontra o maior e o menor peso
maior_peso = max(pesos)
menor_peso = min(pesos)

# Mostra o maior e o menor peso
print("O maior peso lido foi:", maior_peso)
print("O menor peso lido foi:", menor_peso)
