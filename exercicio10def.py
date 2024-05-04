"""
Escreva um programa, com uma função que leia 2 valores (A e B), calcule
e mostre a soma dos números ímpares entre eles (inclusive A e B). Nesse
caso, considere que só serão informados valores inteiros positivos e que A é
menor que B.

"""

def soma_impares_entre(a, b):
    soma = 0
    for num in range(a, b + 1):
        if num % 2 != 0:
            soma += num
    return soma

# Função para ler os valores de A e B
def ler_valores():
    while True:
        try:
            a = int(input("Digite o valor de A (inteiro positivo): "))
            b = int(input("Digite o valor de B (inteiro positivo, maior que A): "))
            if a < 0 or b < 0 or b <= a:
                print("Por favor, digite valores válidos: A deve ser menor que B e ambos devem ser inteiros positivos.")
            else:
                return a, b
        except ValueError:
            print("Por favor, digite valores válidos.")

# Programa principal
a, b = ler_valores()
resultado = soma_impares_entre(a, b)
print("A soma dos números ímpares entre", a, "e", b, "é:", resultado)
