def calcular_peso_ideal(sexo, altura):
    if sexo.lower() == "masculino":
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == "feminino":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None
        print("Sexo não reconhecido.")
    return peso_ideal


def main():
    nome = input("Digite o nome da pessoa: ")
    altura = float(input("Digite a altura da pessoa (em metros): "))
    sexo = input("Digite o sexo da pessoa (Masculino/Feminino): ")

    peso_ideal = calcular_peso_ideal(sexo, altura)

    if peso_ideal is not None:
        print(f"O peso ideal para {nome} é: {peso_ideal:.2f} kg.")


if __name__ == "__main__":
    main()
