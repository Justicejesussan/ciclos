cantidad = int(input("¿Cuántos números quieres introducir? "))

mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

for i in range(cantidad):
    numero = float(input(f"Ingresa el número {i + 1}: "))

    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

print(f"\nCantidad de números mayores que 0: {mayores_que_cero}")
print(f"Cantidad de números menores que 0: {menores_que_cero}")
print(f"Cantidad de números iguales a 0: {iguales_a_cero}")