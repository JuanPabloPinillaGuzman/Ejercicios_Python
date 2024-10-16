#Programa que solicite ingresar numeros enteros, y los suma hasta que se ingresa un numero impar

numerosPares = 0

while True :
    numero = int(input('Ingrese un numero : '))
    if numero % 2 == 0:
        numerosPares = numero + numerosPares
    else :
        False
        print(f'La suma de los numeros enteros ingresados es : {numerosPares}. ')
        exit()
        
