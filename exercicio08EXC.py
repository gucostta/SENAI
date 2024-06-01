"""
Escreva uma função que recebe dois argumentos e retorna sua soma. Trate a
exceção caso os argumentos não sejam números.
"""
def soma_numeros(a, b):
    try:
        # Tenta converter os argumentos para números float
        num1 = float(a)
        num2 = float(b)
        
        # Calcula a soma dos dois números
        resultado = num1 + num2
        
    except ValueError:
        # Trata o caso em que um ou ambos os argumentos não são números válidos
        return "Erro: Ambos os argumentos devem ser números."
    
    # Retorna o resultado da soma
    return resultado

# Exemplos de chamadas à função
print(soma_numeros(10, 20))        # Saída esperada: 30.0
print(soma_numeros("10", "20"))    # Saída esperada: 30.0
print(soma_numeros("dez", 20))     # Saída esperada: Erro: Ambos os argumentos devem ser números.
