"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar

[2] multiplicar

[3] maior

[4] menor

[5] dividir

[6] subtrair

[7] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""

def somar(num1, num2):
    return num1 + num2

def multiplicar(num1, num2):
    return num1 * num2

def maior(num1, num2):
    return max(num1, num2)

def menor(num1, num2):
    return min(num1, num2)

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero!"
    else:
        return num1 / num2

def subtrair(num1, num2):
    return num1 - num2

# Função para ler os dois valores
def ler_valores():
    while True:
        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            return num1, num2
        except ValueError:
            print("Por favor, digite valores válidos.")

# Programa principal
while True:
    print("\n[1] somar\n[2] multiplicar\n[3] maior\n[4] menor\n[5] dividir\n[6] subtrair\n[7] sair do programa")
    opcao = input("Escolha uma opção: ")

    if opcao == '7':
        print("Programa encerrado.")
        break

    elif opcao in ['1', '2', '3', '4', '5', '6']:
        num1, num2 = ler_valores()
        
        if opcao == '1':
            resultado = somar(num1, num2)
        elif opcao == '2':
            resultado = multiplicar(num1, num2)
        elif opcao == '3':
            resultado = maior(num1, num2)
        elif opcao == '4':
            resultado = menor(num1, num2)
        elif opcao == '5':
            resultado = dividir(num1, num2)
        elif opcao == '6':
            resultado = subtrair(num1, num2)
        
        print("O resultado da operação é:", resultado)
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
