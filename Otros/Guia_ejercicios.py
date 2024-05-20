#divisible por 3 y 5 al mismo tiempo, o ninguno de los anteriores.

numero = int(input("Ingresa un numero entero: "))
if numero %2 == 0:
    print(numero, "es un numero par")
else:
    print(numero, "es un numero impar")

if numero %3 == 0 and numero %5 == 0:
    print(numero, "es divisible por 3 y 5 al mismo tiempo.")
else:
    print(numero, "no es divisible por 3 y 5 al mismo tiempo.")

if numero %2 != 0 and (numero %3 != 0 or numero %5 != 0):
    print(numero, "no es par ni divisible por 3 y 5 al mismo tiempo.")




















