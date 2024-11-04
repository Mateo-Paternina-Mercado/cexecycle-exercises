#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
#Altura: 3
#Ancho: 5
# *****
# *****
# *****

# Solicitar al usuario que ingrese la altura y el ancho del rectángulo
altura = int(input("Altura: "))
ancho = int(input("Ancho: "))

# Dibujar el rectángulo
for _ in range(altura):
    print('*' * ancho)
