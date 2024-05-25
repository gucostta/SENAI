"""
26. Calcule as raízes da equação de 2° grau.
"""

import math

# Solicitar ao usuário que insira os coeficientes da equação do segundo grau
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcular o discriminante
delta = b**2 - 4*a*c

# Verificar se a equação tem raízes reais
if delta > 0:
    # Calcular as raízes reais
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
elif delta == 0:
    # Calcular a raiz real única
    x = -b / (2*a)
    print("A equação tem uma raiz real única:", x)
else:
    # Não há raízes reais
    print("A equação não tem raízes reais.")
