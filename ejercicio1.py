#Realice un codigo en python que identifique si el numero ingresado por el usuario es primo o no.
#importamos la biblioteca con las funciones matematicas
import math

#definimos un input de numeros enteros los cuales son utiles para la verificacion que necesitamos realizar
n=int(input("Ingrese un numero ---> "))

#Creamos una funcion con la variable a evaluar, que en este caso seria n, con el numero que ingresara el usuario
def primos(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#En esta funcion se evalua el numero ingresado, con un bucle para la verificacion por nuemros a partir del dos

#Aqui se crea una condicional considerando la funcion y variable para imprimir si el numero es primo o no.
if primos(n):
    print("El numero ", n, "es primo")
else:
    print("El numero ", n, "no es primo")