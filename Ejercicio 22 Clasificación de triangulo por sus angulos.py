# Programa que clasifica un triangulo en agudo, obtuso o rectangulo segun sus angulos internos

angulo1 = int(input('Ingresa el primer angulo :'))
angulo2 = int(input('Ingresa el segundo angulo :'))
angulo3 = int(input('Ingresa el tercero angulo :'))

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print('El triangulo es agudo')
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print('El triangulo es rectangulo')
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print('El triangulo es obtuso')
