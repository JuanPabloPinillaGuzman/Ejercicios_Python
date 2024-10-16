# Programa genera un numero aleatorio entre 1 y 100 y permite al usuario adivinarlo
import random

numeroAleatorio = random.randint(1,100)

while True:
    numero = int(input('Ingrese un numero : '))
    if numero < numeroAleatorio :
        print('El numero es menor')
    elif numero > numeroAleatorio :
        print('El numero es mayor')
    else :
        print('Felicidades, adivinaste el numero')
    exit()