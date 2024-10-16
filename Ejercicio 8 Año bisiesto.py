# Programa que determine si un año es bisiesto o no
año = int(input('Ingresa el año : '))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0 :
    print(f'El ano {año}, es bisiesto')
else :
    print(f'El ano {año}, no es bisiesto')



