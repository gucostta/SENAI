"""
01.Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.

"""

velocidade = float(input("Qual a velocidade do carro? "))
multa = 5


if velocidade > 80:
    exedente = velocidade - 80
    valor = exedente * multa
    print("Você foi multado em: R$%6.2f" % valor)
    
