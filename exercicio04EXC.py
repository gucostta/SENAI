"""
Crie um programa que tente concatenar uma string com um número,
tratando a exceção de operação inválida.
"""
def concatenar_string_e_numero():
    try:
        # Solicita ao usuário para inserir uma string
        string_input = input("Digite uma string: ")
        
        # Solicita ao usuário para inserir um número
        numero_input = input("Digite um número: ")
        
        # Tenta concatenar a string com o número
        # Como a operação de concatenar uma string com um número não é permitida diretamente,
        # é necessário converter o número para string
        resultado = string_input + str(numero_input)
        
    except TypeError:
        # Trata o caso de operação inválida de tipo
        print("Erro: Não é possível concatenar uma string com um tipo não string.")
    else:
        # Se não houver exceção, imprime o resultado da concatenação
        print(f"O resultado da concatenação é: {resultado}")

# Chama a função para executar o programa
concatenar_string_e_numero()
