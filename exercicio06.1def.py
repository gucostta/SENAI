"""
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o.

"""

def soma_pares(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma

# Função para ler os seis números inteiros
def ler_numeros():
    numeros = []
    for i in range(1, 7):
        while True:
            try:
                num = int(input(f"Digite o {i}º número inteiro: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
    return numeros

# Programa principal
print("Digite seis números inteiros:")
numeros = ler_numeros()
soma_pares = soma_pares(numeros)
print("A soma dos números pares é:", soma_pares)
