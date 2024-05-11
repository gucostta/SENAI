"""
Faça um programa para selecionar os elementos de uma lista, de forma a
copiá-los para outras duas listas. Nesse caso, considere que, inicialmente,
os valores estão na lista V = [9, 8, 7, 12, 0, 13 , 21], mas que devem ser
copiados para a P, se forem pares; ou para I, se forem ímpares.

"""

# Lista inicial V
V = [9, 8, 7, 12, 0, 13, 21]

# Listas para armazenar os números pares (P) e ímpares (I)
P = []
I = []

# Loop para percorrer os elementos da lista V e copiá-los para P ou I conforme sua paridade
for elemento in V:
    if elemento % 2 == 0:  # Verifica se o elemento é par
        P.append(elemento)  # Adiciona o elemento à lista P
    else:
        I.append(elemento)  # Adiciona o elemento à lista I

# Exibe as listas P e I
print("Lista P (números pares):", P)
print("Lista I (números ímpares):", I)
