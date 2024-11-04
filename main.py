#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
#
#12,14,18,116,132,164,…
#en forma decimal:
#
#0.5,0.25,0.125,0.0625,0.03125,0.015625,…
#El programa debe mostrar tres columnas que contengan la siguiente información:
#
#Potencia  Fraccion  Suma
#1         0.5       0.5
#2         0.25      0.75
#3         0.125     0.875
#4         0.0625    0.9375
#...       ...       ...
#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.

# Inicializar variables
potencia = 1
fraccion = 0.5
suma_acumulada = 0.0

# Imprimir encabezado
print(f"{'Potencia':<10} {'Fraccion':<10} {'Suma':<10}")

# Calcular potencias fraccionales de dos
while fraccion > 0.000001:
    suma_acumulada += fraccion
    print(f"{potencia:<10} {fraccion:<10.6f} {suma_acumulada:<10.6f}")
    
    # Incrementar la potencia y calcular la siguiente fracción
    potencia += 1
    fraccion /= 2  # Cada fracción es la mitad de la anterior
