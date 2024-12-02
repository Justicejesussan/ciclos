contador = 0
acumulador = 0


while True:
    numero = int(input("Introduce un número (0 para terminar): "))


    if numero == 0:
        break


    acumulador += numero


    contador += 1

if contador > 0:

    media = acumulador / contador
    # Imprimimos la suma y la media
    print(f"La suma de los números introducidos es: {acumulador}")
    print(f"La media de los números introducidos es: {media}")
else:
    print("No se han introducido números válidos.")