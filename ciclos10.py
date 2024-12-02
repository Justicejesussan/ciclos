base = float(input("Introduce la base (número real): "))
exponente = int(input("Ingresa el exponente (entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1


    for _ in range(exponente):
        resultado *= base

    print(f"El resultado de {base} elevado a la {exponente} es: {resultado}")