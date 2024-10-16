# Programa que solicita dos numeros enteros, un valor de inicio y un valor final. debe imprimir todos los numeros pares, incluyendo los limites.

numero1 = int(input('Ingrese el valor de inicio : '))
numero2 = int(input('Ingrese el valor final : '))

if numero1 > numero2:
    print('El valor inicial tiene que ser menor al final ')
else :
    print(f'Numeros pares entre {numero1} y {numero2}')

for i in range(numero1,numero2):
    if i % 2 == 0:
        print(i)
