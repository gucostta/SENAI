"""
14. Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do
outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo
do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
"""

# Inicializar variáveis
valores = []
soma = 0
quantidade = 0

# Ler os valores até que seja informado -1
while True:
    valor = float(input("Digite um valor (ou -1 para encerrar): "))
    if valor == -1:
        break
    valores.append(valor)
    soma += valor
    quantidade += 1

# Mostrar a quantidade de valores lidos
print("\na. Quantidade de valores lidos:", quantidade)

# Mostrar todos os valores na ordem em que foram informados, um ao lado do outro
print("b. Valores na ordem em que foram informados:", " ".join(map(str, valores)))

# Mostrar todos os valores na ordem inversa à que foram informados, um abaixo do outro
print("c. Valores na ordem inversa à que foram informados:")
for valor in reversed(valores):
    print(valor)

# Mostrar a soma dos valores
print("d. Soma dos valores:", soma)

# Calcular a média dos valores
media = soma / quantidade

# Mostrar a média dos valores
print("e. Média dos valores:", media)

# Calcular e mostrar a quantidade de valores acima da média
acima_da_media = sum(1 for valor in valores if valor > media)
print("f. Quantidade de valores acima da média:", acima_da_media)

# Calcular e mostrar a quantidade de valores abaixo de sete
abaixo_de_sete = sum(1 for valor in valores if valor < 7)
print("g. Quantidade de valores abaixo de sete:", abaixo_de_sete)

# Encerrar o programa com uma mensagem
print("\nPrograma encerrado.")
