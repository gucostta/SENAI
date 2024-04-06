"""
4.Faça um programa que solicite o preço de uma mercadoria e o percentual de
desconto. Exiba o valor do desconto e o preço a pagar.
"""

preco = float(input("Digite o preço da mercadoria:"))
percentual = float(input("Digite o valor de desconto:"))

desconto = preco / percentual

valor = preco - desconto 

print("Seu desconto foi de:", valor)
