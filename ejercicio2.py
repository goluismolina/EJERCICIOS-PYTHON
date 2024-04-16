#Describir en phyton la siguiente decision para pagar una compra en el exterior para una empresa logistica ubicada en la granja, Chile. Se considera lo siguiente:
#Si la compra es menos a 60 millones de dolares se realiza una transaccion directa al banco en el exterior.
#si la compra se encuentra entre 60 y 120  se paga con un impuesto del 15% a la transaccion directa al Banco 
#si la compra se encuentra entre 120 y 300 , se paga con un interes del 20% al valor de la compra.
#pero si es mayor a 300, se gana un beneficio de descuento del 11%
# se solicita el monto de la compra
monto_compra = float(input("Ingrese el valor de la compra en dólares: "))

#en la siguiente funcion se evalua cada caso con las condicionales para definir el pago
def compra(monto_compra):
    if monto_compra < 60e6:
        print("Se realiza una transacción directa al banco en el exterior.")
    elif 60e6 <= monto_compra <= 120e6:
        impuesto = monto_compra * 0.15
        total_pago = monto_compra + impuesto
        print(f"Se paga con un impuesto del 15% a la transacción directa al banco. Total a pagar: ${total_pago}")
    elif 120e6 < monto_compra <= 300e6:
        interes = monto_compra * 0.20
        total_pago = monto_compra + interes
        print(f"Se paga con un interés del 20% al valor de la compra. Total a pagar: ${total_pago}")
    else:
        descuento = monto_compra * 0.11
        total_pago = monto_compra - descuento
        print(f"Se gana un beneficio de descuento del 11%. Total a pagar: ${total_pago}")


#se expresa la respuesta de cada caso
compra(monto_compra)