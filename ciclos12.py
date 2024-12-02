ahorro_total = 0
for mes in range(1, 13):

    deposito_mes = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))

    ahorro_total += deposito_mes

    print(f"Ahorro acumulado hasta el mes {mes}: {ahorro_total:.2f} unidades monetarias")


print(f"\nTotal ahorrado al final del año: {ahorro_total:.2f} unidades monetarias")