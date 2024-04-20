"""
Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou
igual a zero e o quadrado do número caso ele seja negativo.

"""

# Solicitar ao usuário um número
numero = float(input("Digite um número: "))

# Verificar se o número é positivo ou igual a zero
if numero >= 0:
    # Calcular e imprimir a raiz quadrada do número
    raiz_quadrada = numero ** 0.5
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    # Calcular e imprimir o quadrado do número
    quadrado = numero ** 2
    print("O quadrado de", numero, "é", quadrado)
