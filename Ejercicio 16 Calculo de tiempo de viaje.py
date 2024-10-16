# Programa que calcula el tiempo que tarda en llegar un automovil a su destino

distancia = float(input('Ingrese la distancia a recorrer en Km : '))
velocidadPromedio = float(input('Ingrese la velocidad promedio en km/h : '))

tiempoHoras = float(round(distancia / velocidadPromedio,3))
tiempoMinutos = float(tiempoHoras * 60)

if velocidadPromedio >= 120 :
    print('Advertencia : Esta excediendo el limite de velocidad')
else :
    print(f'El tiempo que tardara en llegar a su destino en {tiempoHoras} horas. Lo que quiere decir que le tomara {tiempoMinutos} minutos.')