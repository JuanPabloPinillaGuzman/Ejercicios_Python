# Programa que clasifique a la persona segun su edad
edad = int(input('Ingresa la edad de la persona :'))

if edad <= 12 :
    print('La persona es niñ@.')
elif edad >= 13 and edad <= 17 :
    print('La persona es adolecente.')
elif edad >= 18 and edad <= 64 :
    print('La persona es adulta.') 
else :
    print('La persona es anciona')
