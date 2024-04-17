"""
Desenvolva um programa que leia um número inteiro e mostre na tela se ele é par
ou se ele é ímpar.

"""

n1 = int(input("Digite um numero inteiro: "))

impar = n1 % 2

if impar:
    print("Seu número é Impar!")
else:
    print("Seu número é Par!")

