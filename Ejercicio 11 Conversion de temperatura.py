# Programa que conviertE grados Celsius a Fahrenheit o Fahrenheit a Celsius.

temperatura = float(input('Ingrese la temperatura : '))
escala = input('Ingrese la escala C o F : ')

match escala:
    case "c":
        print(f'La temperatura ingresada es {(temperatura * 9/5) + 32} en Fahrenheit')
    case "f":
        print(f'La temperatura ingresada es {(temperatura - 32) * 5/9} en Celsius')
