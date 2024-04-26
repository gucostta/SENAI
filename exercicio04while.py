soma = 0

for num in range(1, 501):
    if num % 3 == 0:
        soma += num

print("A soma dos números múltiplos de três no intervalo de 1 a 500 é:", soma)
