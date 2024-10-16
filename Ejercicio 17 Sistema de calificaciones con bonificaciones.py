# programa que calcula la calificación final de un estudiante segun su calificación y tareas adicionales.

calificacionEstudiante = int(input("Ingrese la calificación del estudiante : "))
numeroTareas = int(input('Cuantas tareas adicionales realizo ? : '))
notaExtra = ((calificacionEstudiante * 0.05)*(numeroTareas))
notaFinal = calificacionEstudiante + notaExtra
if numeroTareas == 0 :
    print(f'La nota del estudiante {calificacionEstudiante}')
elif notaFinal >= 100: 
    print(f'La nota del estudiante es 100')
else :
    print(f'La nota final del estudiante es {notaFinal}')
    
    