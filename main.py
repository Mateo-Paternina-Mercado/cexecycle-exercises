# Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
# 
# Lado: 4
# 
#    ****
#   ******
#  ********
# **********
#  ********
#   ******
#    ****

# Solicitar al usuario que ingrese el tamaño del lado del hexágono
lado = int(input("Lado: "))

# Dibujar la parte superior del hexágono
for i in range(lado):
    espacios = ' ' * (lado - i - 1)
    asteriscos = '*' * (2 * i + 4)  # Ajustar el número de asteriscos
    print(espacios + asteriscos)

# Dibujar la parte inferior del hexágono
for i in range(lado - 1):
    espacios = ' ' * (i + 1)
    asteriscos = '*' * (2 * (lado - i - 1) + 4)  # Ajustar el número de asteriscos
    print(espacios + asteriscos)