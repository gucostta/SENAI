"""
12. Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -&gt; 721.
"""

def reverso_numero(numero):
    # Converte o número para string, reverte a string e converte de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Exemplo de uso da função
numero = 127
reverso = reverso_numero(numero)
print("O reverso de", numero, "é", reverso)
