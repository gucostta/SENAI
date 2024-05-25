"""
28. Faça um programa em Python que mostre um menu onde o usuário poderá escolher
se quer converter uma temperatura de Celcius para Fahrenheit ou o contrário. Para
converter uma temperatura digitada em Celsius para Fahrenheit: F = C * (9 / 5) + 32.
Para converte de Fahrenheit para Celsius, use C = (F - 32) * 5 / 9
"""

# Função para converter temperatura de Celsius para Fahrenheit
def celsius_para_fahrenheit(temp_c):
    return temp_c * (9 / 5) + 32

# Função para converter temperatura de Fahrenheit para Celsius
def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

# Função principal
def main():
    while True:
        # Exibir o menu
        print("\nEscolha a opção desejada:")
        print("1. Converter de Celsius para Fahrenheit")
        print("2. Converter de Fahrenheit para Celsius")
        print("3. Sair")
        
        # Solicitar a escolha do usuário
        escolha = input("Opção: ")
        
        # Verificar a escolha do usuário
        if escolha == '1':
            temp_c = float(input("Digite a temperatura em Celsius: "))
            temp_f = celsius_para_fahrenheit(temp_c)
            print("{:.2f} ºC corresponde a {:.2f} ºF".format(temp_c, temp_f))
        elif escolha == '2':
            temp_f = float(input("Digite a temperatura em Fahrenheit: "))
            temp_c = fahrenheit_para_celsius(temp_f)
            print("{:.2f} ºF corresponde a {:.2f} ºC".format(temp_f, temp_c))
        elif escolha == '3':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o programa
if __name__ == "__main__":
    main()
