# Leitura dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Pergunta sobre a operação desejada
operacao = input("Qual operação você deseja realizar? (soma (+), subtração (-), multiplicação (*) ou divisão (/)): ")

# Verificação da operação e cálculo do resultado
if operacao == '+':
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)
elif operacao == '-':
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)
elif operacao == '*':
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)
elif operacao == '/':
    # Verifica se o divisor é diferente de zero para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
