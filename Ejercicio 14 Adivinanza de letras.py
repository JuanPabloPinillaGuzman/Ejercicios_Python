# Programa que permite al usuario adivinar una letra 
import random


letraAleatoria = random.choice('abcde')


while True:
    letra = input('Ingrese una letra entre a y e :')
    if letra not in letraAleatoria:
        print('Ingrese una letra valida')
    match letra :
        case _ if letraAleatoria == letra:
            print(f'Felicidades adivinaste, la letra secreta era {letra}.')
            break
        case _ :
            print('Fallaste')