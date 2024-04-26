while True:
    # Menu
    print("\n[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Menor")
    print("[5] Dividir")
    print("[6] Subtrair")
    print("[7] Sair do programa")

    # Leitura da opção do usuário
    opcao = int(input("Escolha uma opção: "))

    # Se a opção for sair, encerra o programa
    if opcao == 7:
        print("Programa encerrado.")
        break

    # Leitura dos dois valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    # Realização da operação correspondente à opção escolhida
    if opcao == 1:
        resultado = valor1 + valor2
        print("A soma é:", resultado)
    elif opcao == 2:
        resultado = valor1 * valor2
        print("A multiplicação é:", resultado)
    elif opcao == 3:
        resultado = max(valor1, valor2)
        print("O maior valor é:", resultado)
    elif opcao == 4:
        resultado = min(valor1, valor2)
        print("O menor valor é:", resultado)
    elif opcao == 5:
        # Verifica se o divisor é diferente de zero para evitar divisão por zero
        if valor2 != 0:
            resultado = valor1 / valor2
            print("A divisão é:", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif opcao == 6:
        resultado = valor1 - valor2
        print("A subtração é:", resultado)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
