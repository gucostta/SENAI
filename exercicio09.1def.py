"""
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

"""

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Função para ler o número
def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
            if numero < 0:
                print("Por favor, digite um número inteiro não negativo.")
            else:
                return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Programa principal
numero = ler_numero()
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero}! é:", fatorial)
