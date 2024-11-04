#Escriba un programa que entregue todos los divisores del número entero ingresado:
#Ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200

# Solicitar al usuario que ingrese un número entero
numero = int(input("Enter number: "))

# Inicializar una lista para los divisores
divisores = []

# Encontrar los divisores
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Mostrar los divisores
print(" ".join(map(str, divisores)))
