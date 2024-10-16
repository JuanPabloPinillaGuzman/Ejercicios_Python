# Programa que calcula el numero de creditos de estudiante segun sus materias y el puntaje obtenido se debe decir si aprovo o no

materias = int(input('Ingresa el numero de materias cursadas :'))
totalCreditos = 0

for i in range(materias):
    puntaje = float(input(f'Introduce el puntaje de la materia {i+1} : '))
    if puntaje >= 60 :
        print(f'Materia numero {i+1} : Aprovada')
        totalCreditos += 3
    else:
        print(f'Materia numero {i+1} : No aprobada')

print(f'El numero de creditos obtenidos es : {totalCreditos}')