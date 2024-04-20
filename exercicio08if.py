"""
Escreva um programa que leia um número inteiro de 1 a 12 e informe o nome do
mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe mês com este número.

"""

# Solicitar ao usuário um número inteiro de 1 a 12
numero_mes = int(input("Digite um número de 1 a 12: "))

# Verificar se o número está dentro do intervalo válido
if 1 <= numero_mes <= 12:
    # Associar o número do mês ao seu nome
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Imprimir o nome do mês correspondente ao número digitado pelo usuário
    nome_mes = meses[numero_mes - 1]
    print("O mês correspondente ao número", numero_mes, "é", nome_mes + ".")
else:
    # Informar ao usuário que o número está fora do intervalo válido
    print("Não existe um mês correspondente ao número", numero_mes)
