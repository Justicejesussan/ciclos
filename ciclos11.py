import math

numero = int(input("Introduce un número entero: "))

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limite = int(math.sqrt(num)) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            return False
    return True

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")