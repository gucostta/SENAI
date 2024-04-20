"""
Exemplo 02 de while
"""

numero = 0

while numero < 5:
    numero += 1

    if numero == 3:
        print("Vamos pular a interação para", numero)
        continue

    print("Numero:", numero)

print("Fim do loop")
