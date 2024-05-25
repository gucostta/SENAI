"""
19. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por
meio de código. Os códigos utilizados são:
 1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex:
1 - Jose/ 2 - João/etc)
 5 - Voto Nulo
 6 - Voto em Branco
Faça um programa que calcule e mostre:
 O total de votos para cada candidato;
 O total de votos nulos;
 O total de votos em branco;
 A percentagem de votos nulos sobre o total de votos;
 A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
"""

# Inicializar variáveis para contar os votos
votos_candidatos = [0, 0, 0, 0]
votos_nulos = 0
votos_em_branco = 0
total_votos = 0

# Loop para receber os votos
while True:
    voto = int(input("Digite o código do voto (1, 2, 3, 4 para os candidatos, 5 para Nulo, 6 para Branco): "))
    
    # Verificar se o voto é válido
    if voto == 0:
        break  # Finalizar a entrada de votos
    elif 1 <= voto <= 4:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    
    total_votos += 1

# Calcular as percentagens
percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_branco = (votos_em_branco / total_votos) * 100 if total_votos > 0 else 0

# Exibir os resultados
print("\nResultado da Eleição")
print("Total de votos para cada candidato:")
for i in range(4):
    print(f"Candidato {i+1}: {votos_candidatos[i]} votos")

print("Total de votos nulos:", votos_nulos)
print("Total de votos em branco:", votos_em_branco)
print("Percentagem de votos nulos sobre o total de votos: {:.2f}%".format(percentual_nulos))
print("Percentagem de votos em branco sobre o total de votos: {:.2f}%".format(percentual_branco))
