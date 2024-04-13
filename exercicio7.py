def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_bruto = salario_por_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato

    return salario_bruto, ir, inss, sindicato, salario_liquido


def main():
    salario_por_hora = float(input("Digite o valor do salário por hora: "))
    horas_trabalhadas = float(
        input("Digite o número de horas trabalhadas no mês: "))

    salario_bruto, ir, inss, sindicato, salario_liquido = calcular_salario(
        salario_por_hora, horas_trabalhadas)

    print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
    print(f"IR (11%): R$ {ir:.2f}")
    print(f"INSS (8%): R$ {inss:.2f}")
    print(f"Sindicato (5%): R$ {sindicato:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")


if __name__ == "__main__":
    main()
