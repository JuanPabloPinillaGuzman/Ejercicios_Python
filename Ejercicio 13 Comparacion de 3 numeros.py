# Programa que determina el mayor de 3 numeros

num1 = int(input('Ingrese el primer numero : '))
num2 = int(input('Ingrese el segundo numero : '))
num3 = int(input('Ingrese el tercer numero : '))

if num1 >= num2 and num1 >= num3 :
    print(f'El numero {num1} es el mayor. ')
elif num2 >= num1 and num2 >= num3 :
    print(f'El numero {num2} es el mayor. ')
else :
    print(f'El numero {num3} es el mayor. ')

