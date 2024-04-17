"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o preço a pagar, de acordo
com a tabela a seguir:

"""

qtde_kwh = float(input("Digite a quantidade de KWH consumida: "))

R = qtde_kwh * 0.40
R1 = qtde_kwh * 0.65

C = qtde_kwh * 0.55
C1 = qtde_kwh * 0.60

I = qtde_kwh * 0.55
I1 = qtde_kwh * 0.60

if qtde_kwh <= 500:
    print("Deve pagar: ", R)
else:
    if qtde_kwh <= 1000:
        print("Deve pagar: ", R1)
    else:
        if qtde_kwh <= 2500:
            print("Deve pagar: ", C)
        else:
            if qtde_kwh <= 5000:
                print("Deve pagar: ", C1)
            else:
                if qtde_kwh <= 10000:
                    print("Deve pagar: ", I)
                else:
                    if qtde_kwh <= 15000:
                        print("Deve pagar: ", I1)
    
    