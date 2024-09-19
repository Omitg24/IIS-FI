# Cálculo del logaritmo entero de un valor real "v" en base "base"
# sin emplear ** ni funciones matemáticas
# José A. Corrales 19-nov-2020

from math import * # solo para la verificación del final

v=float(input("número a calcular su logaritmo: "))
base=int(input("base del logaritmo: "))

# se busca el mayor logaritmo entero que cumple base**logaritmo<=v
logaritmo=0   # se irá incrementando de uno en uno
potencia=1    # debe estar definida para entrar en el bucle la primera vez

# cálculo de potencia como base**logaritmo
while potencia<=v:
    potencia=potencia*base
    # por si se desea ver cómo evoluciona
    #print(v,potencia,logaritmo)
    # se prueba el siguiente valor del logaritmo
    logaritmo=logaritmo+1

# con el último valor nos habíamos pasado ya pues se cumple potencia>v
logaritmo=logaritmo-1

# resultado y comprobación
print("el logaritmo en base",base,"de",v,"es {} ".format(logaritmo))
print("cálculo con reales: {}".format(log(v,base)))