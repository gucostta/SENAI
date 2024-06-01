"""
Crie um programa que leia dois números e tente dividir o primeiro pelo
segundo, tratando a exceção de divisão por zero.
"""
def dividir_numeros():
    try:
        # Solicita ao usuário para inserir o primeiro número
        numero1 = float(input("Digite o primeiro número: "))
        
        # Solicita ao usuário para inserir o segundo número
        numero2 = float(input("Digite o segundo número: "))
        
        # Tenta realizar a divisão
        resultado = numero1 / numero2
        
    except ZeroDivisionError:
        # Trata o caso de divisão por zero
        print("Erro: Não é possível dividir por zero.")
    except ValueError:
        # Trata o caso de valores inválidos que não podem ser convertidos para float
        print("Erro: Por favor, insira números válidos.")
    else:
        # Se não houver exceção, imprime o resultado
        print(f"O resultado de {numero1} dividido por {numero2} é {resultado}")

# Chama a função para executar o programa
dividir_numeros()
