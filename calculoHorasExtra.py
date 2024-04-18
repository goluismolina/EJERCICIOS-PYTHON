from math import*
nombre= input("Nombre del trabajador:  ")
horas= int(input("Ingrese horas laboradas durante la semana: "))
tarifa= float(input("Ingrese el valor de la tarifa a pagar por hora: "))
if horas>40:
    hora_extra=horas-40
    valor_hora_extra=tarifa*1.5*hora_extra
    valor_bruto=tarifa*(horas-hora_extra)+valor_hora_extra
    descuento_legal= valor_bruto*0.07
    sueldo_extra=valor_bruto-descuento_legal
    print("Valor total a pagar es de: ",sueldo_extra,"Y el descuento legal es de: ", descuento_legal)
else:
    valor_bruto=(tarifa*40)
    descuento_legal= valor_bruto*0.07
    sueldo=valor_bruto-descuento_legal
    print("Valor total a pagar a ", nombre, "es de: ", sueldo,"Y el descuento legal es de: ", descuento_legal)

    
