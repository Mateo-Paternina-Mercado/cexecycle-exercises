#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
#
#Altura: 5
#
# *
# **
# ***
# ****
# *****

# Solicitar al usuario que ingrese la altura del triángulo
altura = int(input("Altura: "))

# Dibujar el triángulo
for i in range(1, altura + 1):
    print('*' * i)