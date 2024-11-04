#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
#Ingrese num: 1
#Ingrese num: 7
#La suma es 20

# Solicitar al usuario que ingrese dos números enteros
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

# Determinar el rango entre los dos números
inicio = min(num1, num2) + 1
fin = max(num1, num2)

# Calcular la suma de los números entre ellos
suma = sum(range(inicio, fin))

# Mostrar el resultado
print(f"The sum is: {suma}")
