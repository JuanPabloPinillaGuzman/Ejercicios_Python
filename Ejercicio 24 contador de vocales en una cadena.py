# Programa que solicita una cadena de texto y cuenta el numero de vocales (a,e,i,o,u) contiene

texto = input('Ingrese una cadena de texto : ')
vocales = 'aeiou'
numeroVocales = 0

for i in texto :
    if i.lower()in vocales :
        numeroVocales += 1

print(f'El numero de vocales es : {numeroVocales}.')