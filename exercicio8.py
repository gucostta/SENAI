def calcular_area_quadrado(lado):
    area = lado * lado
    return area


def main():
    lado = float(input("Digite o comprimento do lado do quadrado: "))

    area = calcular_area_quadrado(lado)
    area_dobro = area * 2

    print(f"A área do quadrado é: {area} unidades quadradas.")
    print(f"O dobro da área do quadrado é: {area_dobro} unidades quadradas.")


if __name__ == "__main__":
    main()
