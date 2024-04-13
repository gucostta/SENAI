"""

03. Escreva um programa que leia dois números e que pergunte qual a operação você
deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação realizada.

"""

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

operacao = print("Qual operação deseja realizar? SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO OU DIVISÃO")
if operacao == soma:
    n1 + n2
else:
    if operacao == subtracao:
        n1 - n2
        else:
            if operacao == multiplicacao:
                n1 * n2
                else:
                    if operacao == divisao:
                        n1 / n2
                        else:
                            print("Operação não existe, digite uma operação valida!")
                            operacao = 0
            print("O resultado é: ", operacao)
    

