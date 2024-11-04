#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
#
#π=4(1−13+15−17+…)
#La entrada del programa debe ser un número entero n
# que indique cuántos términos de la suma se utilizará.
#
#n: 3
#3.466666666666667
#n: 1000
#3.140592653839794

# Solicitar al usuario que ingrese el número de términos
n = int(input("n: "))

# Inicializar la suma
suma = 0.0

# Calcular la suma utilizando la fórmula
for i in range(n):
    termino = (-1)**i / (2 * i + 1)  # Fórmula para cada término
    suma += termino

# Calcular el valor estimado de π
pi_estimado = 4 * suma

# Mostrar el resultado
print(pi_estimado)
