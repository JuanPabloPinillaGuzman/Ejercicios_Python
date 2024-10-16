# Programa que identifica el dia de la semana segun su numero
dia = int(input('Los dias de la semana van del 1 - 7.\nIngresa un numero para saber a que dia pertenece : '))

match dia :
    case 1 :
        print('El dia seleccionado es el lunes.')
    case 2 :
        print('El dia seleccionado es el Martes.')
    case 3 :
        print('El dia seleccionado es el Miercoles.')
    case 4 :
        print('El dia seleccionado es el Jueves.')
    case 5 :
        print('El dia seleccionado es el Viernes.')
    case 6 :
        print('El dia seleccionado es el Sabado.')
    case 7 :
        print('El dia seleccionado es el Domingo.')