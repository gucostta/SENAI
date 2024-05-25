"""
5. Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -&gt; 721. Além da função, faça com que o programa
execute a função criada.
"""

def reverso_numero(numero):
    # Converte o número para string, reverte a string e converte de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Programa principal que solicita um número ao usuário e exibe o reverso
numero_informado = int(input("Digite um número inteiro: "))
numero_reverso = reverso_numero(numero_informado)

print(f"O reverso do número {numero_informado} é {numero_reverso}")
