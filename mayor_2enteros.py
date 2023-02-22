# Pedir al usuario que ingrese dos números enteros
x = int(input("Ingrese el primer número entero: "))
y= int(input("Ingrese el segundo número entero: "))

# Verificar cuál número es mayor y mostrar el resultado
if x > y:
    print("El primer número ingresado (>) es mayor que el segundo número ingresado (<).".format(x, y))
elif y > x:
    print("El segundo número ingresado (<) es mayor que el primer número ingresado (>).".format(y, x))
else:
    print("Los dos números ingresados (=) son iguales.".format(x))