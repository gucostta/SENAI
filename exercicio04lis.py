"""
Faça um programa que leia um vetor de 10 caracteres minúsculos e diga
quantas consoantes foram lidas.

"""

# Função para verificar se um caractere é uma consoante minúscula
def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    return caractere in consoantes

# Cria um vetor vazio para armazenar os caracteres
caracteres = []

# Loop para ler os 10 caracteres e adicionar ao vetor
for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere minúsculo: ")
    caracteres.append(caractere)

# Contador para contar o número de consoantes
num_consoantes = 0

# Loop para verificar cada caractere e contar as consoantes
for caractere in caracteres:
    if eh_consoante(caractere):
        num_consoantes += 1

# Exibe o número de consoantes na tela
print(f"O número de consoantes lidas é: {num_consoantes}")
