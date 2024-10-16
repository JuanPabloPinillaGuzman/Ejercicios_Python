# Programa que asigna una calificacion basada en una nota numerica

nota = int(input('Ingrese la nota para saber la calificación :'))

if nota >= 90 and nota <= 100 :
    print(f'Su nota de {nota} tiene una calificación de A')
elif nota >= 80 and nota <= 89 :
    print(f'Su nota de {nota} tiene una calificación de B')
elif nota >= 70 and nota <= 79 :
    print(f'Su nota de {nota} tiene una calificación de C')
elif nota >= 60 and nota <= 69 :
    print(f'Su nota de {nota} tiene una calificación de D')
elif nota >= 0 and nota <= 59:
    print(f'Su nota de {nota} tiene una calificación de F')
else :
    print('Ingrese una nota valida entre 0 - 100')