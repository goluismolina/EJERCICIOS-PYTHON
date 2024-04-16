from math import *
valor_compra=0
valor_iva=0
valor_total=0

valor_compra=int(input("Ingrese el valor de su compra "))
valor_iva=(valor_compra*0.19)
valor_total=(valor_compra + valor_iva)
print("El valor de su compra incluyendo IVA es de ---> ", valor_total)

