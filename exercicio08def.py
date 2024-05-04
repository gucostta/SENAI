"""
Escreva um programa, com uma função para ler a idade de uma pessoa e
informar a sua classe eleitoral, conforme:

Não-eleitor – abaixo de 16 anos;

Eleitor obrigatório – entre 18 e 65 anos;

Eleitor facultativo – entre 16 e 18 ou maior de 65 anos.

"""

def classe_eleitoral(idade):
    if idade < 16:
        return "Não-eleitor"
    elif 18 <= idade <= 65:
        return "Eleitor obrigatório"
    else:
        return "Eleitor facultativo"

# Função para ler a idade da pessoa
def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade da pessoa: "))
            if idade < 0:
                print("Por favor, digite uma idade válida.")
            else:
                return idade
        except ValueError:
            print("Por favor, digite uma idade válida.")

# Programa principal
idade_pessoa = ler_idade()
classe = classe_eleitoral(idade_pessoa)
print("A classe eleitoral da pessoa é:", classe)
