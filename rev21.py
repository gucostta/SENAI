"""
21. Faça um programa em linguagem Python, que lê um número n e imprime os n
primeiros números da sequência de Fibonacci.
"""

def fibonacci(n):
    fibonacci_seq = [0, 1]  # Inicializamos a sequência de Fibonacci com os dois primeiros números
    while len(fibonacci_seq) < n:  # Continuamos adicionando números à sequência até atingir n
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])  # Adicionamos o próximo número como a soma dos dois últimos números
    return fibonacci_seq

# Lê o número n
n = int(input("Digite o número de termos da sequência de Fibonacci que deseja gerar: "))

# Imprime os n primeiros números da sequência de Fibonacci
print("Os", n, "primeiros números da sequência de Fibonacci são:")
print(fibonacci(n))
