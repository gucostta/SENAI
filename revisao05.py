"""
5. Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -&gt; 721. Além da função, faça com que o programa
execute a função criada.
"""

def reverso_numero(numero):
    # Converte o número em uma string para facilitar a inversão
    numero_str = str(numero)
    # Inverte a string
    reverso_str = numero_str[::-1]
    # Converte a string invertida de volta para um número inteiro
    reverso_numero = int(reverso_str)
    return reverso_numero

def main():
    numero = int(input("Digite um número inteiro: "))
    reverso = reverso_numero(numero)
    print("O reverso de", numero, "é:", reverso)

if __name__ == "__main__":
    main()
