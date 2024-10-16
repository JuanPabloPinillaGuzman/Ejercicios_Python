#Calculadora Basica
num1 = int(input('Ingrese el primer numero : '))
num2 = int(input('Ingrese el segundo numero : '))
operacion = int(input('Seleccione que operacion desea realizar:\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n '))

match operacion:
    case 1:
        print(f'El resultado de la suma es {num1 + num2}')
    case 2:
        print(f'El resultado de la suma es {num1 - num2}')    
    case 3:
        print(f'El resultado de la multiplicacion es {num1 * num2}') 
    case 4:
        print(f'El resultado de la division es {num1 / num2}')