while True:

    caracter = input("Ingresa un carácter: ")

    if caracter == ' ':
        break

    if caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")