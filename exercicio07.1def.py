"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.

"""

def ler_pesos():
    pesos = []
    for i in range(1, 6):
        while True:
            try:
                peso = float(input(f"Digite o peso da {i}ª pessoa: "))
                pesos.append(peso)
                break
            except ValueError:
                print("Por favor, digite um peso válido.")
    return pesos

def encontrar_maior_menor(pesos):
    maior_peso = max(pesos)
    menor_peso = min(pesos)
    return maior_peso, menor_peso

# Programa principal
print("Digite o peso de cinco pessoas:")
pesos = ler_pesos()
maior_peso, menor_peso = encontrar_maior_menor(pesos)
print("O maior peso lido foi:", maior_peso)
print("O menor peso lido foi:", menor_peso)
