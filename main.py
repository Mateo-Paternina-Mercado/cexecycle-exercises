#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:
#
#e=10!+11!+12!+13!+14!+…
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
#
#Recuerde que el factorial n! es el producto de los números de 1 a n.

# Función para calcular el factorial de un número de manera iterativa
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Inicializar variables
n = 10  # Comenzar desde 10!
suma_e = 0.0
ultimo_termino = 1.0  # Para el primer término (1/10!)
diferencia = float('inf')  # Inicializar con infinito

# Calcular la suma de 1/n! hasta que la diferencia sea menor que 0.0001
while diferencia >= 0.0001:
    nuevo_termino = 1 / factorial(n)
    suma_e += nuevo_termino
    
    # Calcular la diferencia entre términos
    if n > 10:  # Para evitar la diferencia inicial
        diferencia = abs(nuevo_termino - ultimo_termino)
    
    ultimo_termino = nuevo_termino
    n += 1  # Incrementar n para calcular el siguiente factorial

# Mostrar el resultado aproximado de e
print(f"Valor aproximado de e: {suma_e + 1}")  # Agregar el 1 por el término 1/0!
