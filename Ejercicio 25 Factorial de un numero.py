# Pragrama que solicite un entero positivo n y calcule el factorial de dicho numero

numero = int(input('Escriba un numero entero positivo : '))
factorial = int(1)

for i in range(1, numero + 1):
    factorial  *= i
    print(f'El factorial del {numero} es : {factorial}')