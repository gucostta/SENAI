# Leitura do número
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial
for i in range(1, numero + 1):
    fatorial *= i

# Mostra o resultado
print(f"O fatorial de {numero}! é:", fatorial)
