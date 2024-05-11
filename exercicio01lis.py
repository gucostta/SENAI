"""
Faça um programa que leia um vetor de 5 números inteiros e mostre-os na
tela.

"""
# Cria um vetor vazio
vetor = []

# Loop para ler 5 números inteiros e adicionar ao vetor
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

# Exibe os números na tela
print("Os números digitados são:")
for numero in vetor:
    print(numero)
