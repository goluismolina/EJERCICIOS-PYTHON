from math import *

cuenta=float(input("Ingrese el valor de la cuneta "))
if cuenta < 50000:
    pago= print("Se paga con efectivo")
else:
    if cuenta >= 50000 and cuenta <= 100000:
        pago= print("Se paga con debito")
    else:
        pago= print("Se paga con credito")