import random

intentos = 3
minimo = int(input("Cuál quieres que sea el mínimo: "))
maximo = int(input("Cuál quieres que sea el máximo: "))

numero = int(random.randint(minimo, maximo))

for i in range (0, 3):
    print(f"Tienes {intentos} intentos restantes para adivinar el número.")
    numeroadivinado = int(input("Cuál crees que es el número? "))

    if(numeroadivinado == numero):
        print("¡Felcidades, has adivinado el número!")
    else:
        print("¡Has fallado!")
        intentos = intentos - 1
    if(intentos == 0):
        print(f"El número correcto era el {numero}.")