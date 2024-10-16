# Programa que identifique el tipo de triangulo en funcion de sus lados
long1 = float(input('Ingrese la primera longitud del triangulo : '))
long2 = float(input('Ingrese la segunda longitud del triangulo : '))
long3 = float(input('Ingrese la tercera longitud del triangulo : '))

if long1 == long2 and long2 == long3:
    print('El tipo de triangulo segun sus logitudes es Equilatero ')
elif long1 != long2 and long1 != long3 and long2 != long3:
    print('El tipo de triangulo segun sus logitudes es Escaleno ')
else :
    print('El tipo de triangulo segun sus logitudes es Isosceles ')
