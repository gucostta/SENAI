"""
Faça um programa com uma função que necessite de uma argumento. A
função retorna o valor do caractere ‘P’, se o seu argumento for positivo, e
‘N’, se o ser argumento for zero ou negativo.

"""

def verificar_positivo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Exemplo de uso da função
argumento = float(input("Digite um número: "))

resultado = verificar_positivo(argumento)
print("O valor retornado pela função é:", resultado)
