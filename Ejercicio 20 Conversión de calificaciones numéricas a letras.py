# Programa que convierte una calificación numerica en una letra 

CalificacionNumerica = int(input('Ingresa una calificación entre 1 - 100 : '))

match CalificacionNumerica:
    case CalificacionNumerica if 90 <= CalificacionNumerica <= 100:
        print('La calificación es A. ')
    case CalificacionNumerica if 80 <= CalificacionNumerica <= 89:
        print('La calificación es A. ')
    case CalificacionNumerica if 70 <= CalificacionNumerica <= 79:
        print('La calificación es A. ')
    case CalificacionNumerica if 60 <= CalificacionNumerica <= 69:
        print('La calificación es A. ')
    case CalificacionNumerica if 0 <= CalificacionNumerica <= 59:
        print('La calificación es A. ')
    case _ :
        print('Ingresa una calificación valida')