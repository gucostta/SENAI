"""
10. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. &quot;Telefonou para a vítima?&quot;
b. &quot;Esteve no local do crime?&quot;
c. &quot;Mora perto da vítima?&quot;
d. &quot;Devia para a vítima?&quot;
e. &quot;Já trabalhou com a vítima?&quot;
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como &quot;Suspeita&quot;, entre 3 e 4 como &quot;Cúmplice&quot; e 5 como &quot;Assassino&quot;. Caso contrário,
ele será classificado como &quot;Inocente&quot;.
"""

# Inicializar o contador de respostas positivas
respostas_positivas = 0

# Fazer as 5 perguntas
print("Responda 'sim' ou 'não' para as seguintes perguntas:")
pergunta_a = input("Telefonou para a vítima? ").lower()
pergunta_b = input("Esteve no local do crime? ").lower()
pergunta_c = input("Mora perto da vítima? ").lower()
pergunta_d = input("Devia para a vítima? ").lower()
pergunta_e = input("Já trabalhou com a vítima? ").lower()

# Verificar as respostas e atualizar o contador de respostas positivas
if pergunta_a == 'sim':
    respostas_positivas += 1
if pergunta_b == 'sim':
    respostas_positivas += 1
if pergunta_c == 'sim':
    respostas_positivas += 1
if pergunta_d == 'sim':
    respostas_positivas += 1
if pergunta_e == 'sim':
    respostas_positivas += 1

# Emitir a classificação
if respostas_positivas == 2:
    print("Você é Suspeito(a).")
elif 3 <= respostas_positivas <= 4:
    print("Você é Cúmplice.")
elif respostas_positivas == 5:
    print("Você é o Assassino.")
else:
    print("Você é Inocente.")
