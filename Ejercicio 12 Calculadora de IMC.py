# Programa que calcula el IMC y determina el estado del peso

peso = int(input('Ingresa el peso en Kilogramos : '))
altura = float(input('Ingresa la altura en Metros : '))

imc = float(round(peso / (altura ** 2),1))

if imc < 18.5 :
    print(f'Su peso es {imc} Tiene peso bajo')
elif imc >= 18.5 and imc <= 24.9 :
    print(f'Su peso es {imc} Tiene peso normal')
else :
    print(f'Su peso es {imc} Tiene obesidad')