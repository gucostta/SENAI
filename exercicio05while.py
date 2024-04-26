# Solicita ao usuário para inserir o número para o qual deseja a tabuada
numero = int(input("Digite o número para o qual deseja ver a tabuada: "))

# Loop for para iterar de 1 a 10 e mostrar a tabuada
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
