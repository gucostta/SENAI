"""
Crie um programa que leia uma lista de números e tente acessar um índice
especificado pelo usuário, tratando a exceção de índice fora do intervalo.
"""
def acessar_indice_lista():
    try:
        # Solicita ao usuário para inserir uma lista de números, separados por espaço
        entrada = input("Digite uma lista de números, separados por espaço: ")
        
        # Converte a entrada em uma lista de números inteiros
        lista = [int(x) for x in entrada.split()]
        
        # Solicita ao usuário para inserir o índice que deseja acessar
        indice = int(input("Digite o índice que deseja acessar: "))
        
        # Tenta acessar o índice especificado na lista
        elemento = lista[indice]
        
    except IndexError:
        # Trata o caso em que o índice está fora do intervalo da lista
        print("Erro: Índice fora do intervalo.")
    except ValueError:
        # Trata o caso de valores inválidos (não inteiros)
        print("Erro: Entrada inválida. Certifique-se de que todos os valores são números inteiros.")
    else:
        # Se não houver exceção, imprime o elemento no índice especificado
        print(f"O elemento no índice {indice} é: {elemento}")

# Chama a função para executar o programa
acessar_indice_lista()
