# El programa genera un número aleatorio entre 1 y 10. El usuario debe 
# adivinar el número, y el programa indica si el número ingresado es 
# mayor, menor o igual al número generado.

import random
numero = int(input('Ingrese un numero del 1-10 para identificar si es mayor, menos o igual al numero generado :'))
numeroAleatorio = random.randint(1,10)

if numero > numeroAleatorio :
    print(f'El numero que ingreso es {numero} y el numero aleatorio es {numeroAleatorio}, su numero es mayor ')
elif numero < numeroAleatorio :
    print(f'El numero que ingreso es {numero} y el numero aleatorio es {numeroAleatorio}, su numero es menor ')
else :
    print(f'Ganaste, ambos numeros son {numero}')