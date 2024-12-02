import random

numero_aleatorio = random.randint(1, 100)

intentos_maximos = 10
intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He generado un número aleatorio entre 1 y 100. Tienes 10 intentos para adivinarlo.")

while intentos < intentos_maximos:

    intentos += 1
    intento_usuario = int(input(f"Intento {intentos}/{intentos_maximos}: Introduce un número: "))

    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor. ¡Intenta de nuevo!")
    else:
        print("El número es menor. ¡Intenta de nuevo!")

    if intentos == intentos_maximos:
        print(f"Lo siento, has agotado todos tus intentos. El número era {numero_aleatorio}.")