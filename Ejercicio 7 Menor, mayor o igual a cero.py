# Programa que determina si un numero es positivo, negativo o cero

numero = float(input('Ingrese un numero para determinar si, es positivo, negativo o cero : '))

if numero == 0 :
    print('El numero ingresado es igual a cero')
elif numero < 0 :
    print(f'El numero ingresado {numero}, es menor a cero')
else :
    print(f'El numero ingresado {numero}, es mayor a cero')