from math import *
print("Ingrese el numero de articulos a comprar")
a=0
if a==0:
    a= int(input("Ingrese numero--> "))
elif a==4:
    a=print(int(input("Numero erroneo, ingrese de nuevo--> "))) 

b = int(input("Ingrese numero 2--> "))
c = int(input("Ingrese numero 3--> "))
d=0
d=(a+b+c)+1
print("Resultado = ", d)
