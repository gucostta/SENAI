"""
Escreva um programa que leia uma entrada do usuário e converta para um
número inteiro, tratando a exceção se a entrada não for um número.
"""
def ler_inteiro():
    try:
        # Solicita ao usuário para inserir um valor
        entrada = input("Digite um número inteiro: ")
        
        # Tenta converter a entrada para um inteiro
        numero = int(entrada)
        
    except ValueError:
        # Trata o caso em que a entrada não pode ser convertida para um inteiro
        print("Erro: A entrada fornecida não é um número inteiro válido.")
    else:
        # Se a conversão for bem-sucedida, imprime o número
        print(f"O número inteiro fornecido é: {numero}")

# Chama a função para executar o programa
ler_inteiro()
