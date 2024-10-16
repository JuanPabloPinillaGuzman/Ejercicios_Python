# Programa que calcule el costo de estacionamiento segun las horas, con tarifas prograsivas

horas = int(input('Ingrese el numero de horas que de estacionamiento : '))

costoTotal = 5

if horas == 1 :
    print(f'El valor a pagar es $ 5. ')   
elif horas > 1 and horas >5 :
    costoTotal = 4*horas
    print(f'El valor a pagar es $ {costoTotal}. ')
else :
    costoTotal = 3*horas
    print(f'El valor a pagar es $ {costoTotal}. ')
    