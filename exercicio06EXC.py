"""
Escreva um programa que leia uma entrada do usuário e converta para um
número decimal (float), tratando a exceção se a entrada não for um número.
"""
def ler_numero_decimal():
    try:
        # Solicita ao usuário para inserir um valor
        entrada = input("Digite um número decimal: ")
        
        # Tenta converter a entrada para um número decimal (float)
        numero = float(entrada)
        
    except ValueError:
        # Trata o caso em que a entrada não pode ser convertida para um float
        print("Erro: A entrada fornecida não é um número decimal válido.")
    else:
        # Se a conversão for bem-sucedida, imprime o número
        print(f"O número decimal fornecido é: {numero}")

# Chama a função para executar o programa
ler_numero_decimal()
