def calcular_multa(peso):
    limite_peso = 50  # limite estabelecido pelo regulamento de pesca
    excesso = 0
    multa = 0

    if peso > limite_peso:
        excesso = peso - limite_peso
        multa = excesso * 4

    return excesso, multa


def main():
    peso = float(input("Digite o peso de peixes (em quilos): "))

    excesso, multa = calcular_multa(peso)

    if excesso > 0:
        print(f"Peso de peixes excedeu o limite em {excesso:.2f} quilos.")
        print(f"Valor da multa a ser paga: R$ {multa:.2f}")
    else:
        print("Peso de peixes dentro do limite. Nenhuma multa é aplicável.")


if __name__ == "__main__":
    main()
