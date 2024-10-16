#Programa que solicite un numero entero positivo y calcule la suma de los primeros numeros enteros.

numero = int(input('Introduce un numero entero positivo : '))
bucle = int(0)

for i in range(1, numero + 1):
    bucle += 1

print(f'La suma de los primeros {numero} numeros enteros es {bucle}. ')