#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
#Duracion tramo: 15
#Duracion tramo: 30
#Duracion tramo: 87
#Duracion tramo: 0
#Tiempo total de viaje: 2:12 horas
#Duracion tramo: 51
#Duracion tramo: 17
#Duracion tramo: 0
#Tiempo total de viaje: 1:08 horas

# Función para calcular el tiempo total en horas y minutos
def calcular_tiempo_total():
    total_minutos = 0

    while True:
        # Solicitar al usuario que ingrese la duración del tramo
        tramo = int(input("Section duration: "))
        if tramo == 0:
            break
        total_minutos += tramo

    # Calcular horas y minutos
    horas = total_minutos // 60
    minutos = total_minutos % 60

    # Mostrar el tiempo total de viaje
    print(f"Total travel time: {horas}:{minutos:02d} hours")

# Llamar a la función
calcular_tiempo_total()
