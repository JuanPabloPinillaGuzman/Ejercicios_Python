# Programa que calcule el salario neto despues de descuentos

SalarioBruto = int(input('Ingrese su salario en burto : '))
pais = input('Ingrese su pais de residencia : ')
colombia = 0.80
venezuela = 0.85
ecuador = 0.90
otro = 0.75

if pais == 'colombia' :
    print(f'El salario neto despues de impuestos en {pais} es {SalarioBruto * colombia } ')
if pais == 'venezuela' :
    print(f'El salario neto despues de impuestos en {pais} es {SalarioBruto * venezuela } ')
if pais == 'ecuador' :
    print(f'El salario neto despues de impuestos en {pais} es {SalarioBruto * ecuador } ')
else :
    print(f'El salario neto despues de impuestos en {pais} es {SalarioBruto * otro } ')
