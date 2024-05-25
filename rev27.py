"""
27. Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius,
em seu programa o usuário deverá inserir uma sequência de valores que representam
a temperatura em graus Fahrenheit, seu programa deve receber esses valores e
armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco
(uma string vazia). Converta todos os valores presentar na lista para graus Celsius e
imprima na tela em uma formatação amigável ao usuário.
Exemplos de entrada Exemplos de saída
86 86 ºF corresponde a 30 ºC
77 77 ºF corresponde a 25 ºC
89.6 89.6 ºF corresponde a 32 ºC
73.4 73.4 ºF corresponde a 23 ºC
69.8 69.8 ºF corresponde a 21 ºC
"""

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

# Lista para armazenar as temperaturas em Fahrenheit
temperaturas_fahrenheit = []

# Loop para receber as temperaturas em Fahrenheit do usuário
while True:
    temp_f_str = input("Digite a temperatura em Fahrenheit (ou deixe em branco para encerrar): ")
    
    # Verificar se o usuário inseriu um valor em branco
    if temp_f_str == "":
        break
    
    # Converter a entrada para float e adicionar à lista
    temp_f = float(temp_f_str)
    temperaturas_fahrenheit.append(temp_f)

# Converter as temperaturas para Celsius e imprimir na tela
print("\nTemperaturas convertidas para Celsius:")
for temp_f in temperaturas_fahrenheit:
    temp_c = fahrenheit_para_celsius(temp_f)
    print("{:.1f} ºF corresponde a {:.1f} ºC".format(temp_f, temp_c))
