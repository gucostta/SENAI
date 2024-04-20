"""
Para doar sangue é necessário:

Ter entre 16 e 69 anos.

Pesar mais de 50 kg.

Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).

Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 horas para uma pessoa e
diga se ela por ou não doar sangue.


"""

print("Bem-vindo ao programa de verificação de doação de sangue!")

# Obter idade da pessoa
idade = int(input("Qual é a sua idade? "))

# Obter peso da pessoa
peso = float(input("Qual é o seu peso em kg? "))

# Obter horas de sono da pessoa
horas_sono = int(input("Quantas horas você dormiu nas últimas 24 horas? "))

# Verificar se a pessoa pode doar sangue
if 16 <= idade <= 69 and peso > 50 and horas_sono >= 6:
    print("Você está apto para doar sangue. Obrigado por sua disposição em ajudar!")
else:
    print("Desculpe, você não está apto para doar sangue.")
