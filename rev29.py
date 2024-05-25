"""
29. Escreva o menu de opções abaixo. Leia a opção ao do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção:
"""

# Função para calcular a soma de dois números


def soma(a, b):
    return a + b

# Função para calcular a diferença entre dois números (maior pelo menor)


def diferenca(a, b):
    return abs(a - b)

# Função para calcular o produto entre dois números


def produto(a, b):
    return a * b

# Função para calcular a divisão entre dois números (o denominador não pode ser zero)


def divisao(a, b):
    if b == 0:
        return "Erro: O denominador não pode ser zero."
    else:
        return a / b

# Função principal


def main():
    while True:
        # Exibir o menu de opções
        print("\nEscolha a opção:")
        print("1- Soma de 2 números.")
        print("2- Diferença entre 2 números (maior pelo menor).")
        print("3- Produto entre 2 números.")
        print("4- Divisão entre 2 números (o denominador não pode ser zero).")
        print("5- Sair")

        # Solicitar a escolha do usuário
        opcao = input("Opção: ")

        # Verificar a opção escolhida e executar a operação correspondente
        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("A soma é:", soma(num1, num2))
        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("A diferença é:", diferenca(num1, num2))
        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("O produto é:", produto(num1, num2))
        elif opcao == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número (o denominador): "))
            print("O resultado da divisão é:", divisao(num1, num2))
        elif opcao == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Executar o programa
if __name__ == "__main__":
    main()
