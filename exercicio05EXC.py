"""
Escreva um programa que leia um número e calcule seu quadrado, tratando
a exceção se o valor não for um número inteiro.
"""
def calcular_quadrado():
    try:
        # Solicita ao usuário para inserir um número
        entrada = input("Digite um número inteiro: ")
        
        # Tenta converter a entrada para um número inteiro
        numero = int(entrada)
        
        # Calcula o quadrado do número
        quadrado = numero ** 2
        
    except ValueError:
        # Trata o caso em que a entrada não pode ser convertida para um inteiro
        print("Erro: A entrada fornecida não é um número inteiro válido.")
    else:
        # Se a conversão for bem-sucedida, imprime o quadrado do número
        print(f"O quadrado de {numero} é: {quadrado}")

# Chama a função para executar o programa
calcular_quadrado()
