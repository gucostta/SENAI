"""
Escreva um programa, com uma função que imprima o conceito de um
aluno, dada a sua nota. Supor, apenas, notas inteiras. O critério para
conceitos é o seguinte:

Nota

Conceito

Notas inferiores a 3

Conceito E

Notas de 3 a 5

Conceito D

Notas de 6 a 7

Conceito C

Notas de 8 a 9

Conceito B

Nota 10

Conceito A

"""

def imprimir_conceito(nota):
    if nota < 3:
        print("Conceito: E")
    elif nota <= 5:
        print("Conceito: D")
    elif nota <= 7:
        print("Conceito: C")
    elif nota <= 9:
        print("Conceito: B")
    else:
        print("Conceito: A")

# Função para ler a nota do aluno
def ler_nota():
    while True:
        try:
            nota = int(input("Digite a nota do aluno (de 0 a 10): "))
            if nota < 0 or nota > 10:
                print("Por favor, digite uma nota válida entre 0 e 10.")
            else:
                return nota
        except ValueError:
            print("Por favor, digite uma nota válida.")

# Programa principal
nota_aluno = ler_nota()
imprimir_conceito(nota_aluno)
