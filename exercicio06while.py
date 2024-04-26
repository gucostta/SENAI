soma_pares = 0

# Lê os seis números inteiros
for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    # Verifica se o número é par e adiciona à soma se for
    if numero % 2 == 0:
        soma_pares += numero

# Mostra a soma dos números pares
print("A soma dos números pares digitados é:", soma_pares)
