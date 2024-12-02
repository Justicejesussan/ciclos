inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))


if inicio > fin:
    inicio, fin = fin, inicio

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print( "El numero par es:" + str(numero))