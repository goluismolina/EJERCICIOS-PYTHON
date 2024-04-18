#En carretera el limite de velocidad es de 50km/h
#Ingrese la velocidad registrada por cada vehiculo
#Y se determinara si excede el limite, en este caso se cursa una multa.
# si excede en 60km/h el limite de velocidad, se debe detener al conductor.
from math import *

velocidad_maxima=50
velocidad_detencion=110
velocidad= int(input("Ingrese la velocidad registrada -->"))
if velocidad<=velocidad_maxima:
    print("Todo bien, puede continuar")
elif velocidad>velocidad_maxima and velocidad < velocidad_detencion:
    print("Cursar multa")
elif velocidad>=velocidad_detencion:
    print("Se debe llevar detenido el conductor")
else:
    print("Datos erroneos, vuelva a intentar")
