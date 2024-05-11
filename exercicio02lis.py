"""
Faça um programa que leia um vetor de 10 números inteiros e mostre-os na
tela na ordem inversa.

"""

# Cria um vetor vazio
vetor = []

# Loop para ler 10 números inteiros e adicionar ao vetor
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

# Exibe os números na tela na ordem inversa
print("Os números digitados na ordem inversa são:")
for numero in reversed(vetor):
    print(numero)
