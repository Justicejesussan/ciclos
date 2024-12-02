suma = 0
contador = 0

while contador < 10:

    numero = float(input("Ingresa un número: "))

    suma += numero

    contador += 1

promedio = suma / 10

print(f"El promedio de los 10 números es: {promedio}")