"""
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T =
[-10, -8, 0 1, 2, 5, -2, -4]. Faça um programa que imprima a maior e a menor
temperatura, assim como a temperatura média.

"""

# Lista de temperaturas de Mons, na Bélgica
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Calcula a maior temperatura
maior_temperatura = max(T)

# Calcula a menor temperatura
menor_temperatura = min(T)

# Calcula a temperatura média
temperatura_media = sum(T) / len(T)

# Exibe os resultados na tela
print("Maior temperatura:", maior_temperatura)
print("Menor temperatura:", menor_temperatura)
print("Temperatura média:", temperatura_media)
