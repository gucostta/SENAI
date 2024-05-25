"""
7. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
usuário. Calcule o total em segundos.
"""

# Solicitar a quantidade de dias, horas, minutos e segundos do usuário
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Calcular o total em segundos
total_segundos = (
    dias * 24 * 3600 +  # Converte dias para segundos
    horas * 3600 +      # Converte horas para segundos
    minutos * 60 +      # Converte minutos para segundos
    segundos            # Segundos
)

# Imprimir o resultado
print(f"O total em segundos é: {total_segundos}")
