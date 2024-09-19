# Cálculo aproximado de la raíz n-sima entera de un número v,
# sin emplear ** ni funciones matemáticas
# José A. Corrales 19-nov-2020

v=float(input("número cuya raíz n-sima se desea calcular: "))
n=int(input("valor n de la raíz: "))

# se busca la mayor raíz entera que cumple raiz**n<=v
raiz=0        # se irá incrementando de uno en uno
potencia=0    # debe estar definida para entrar en el bucle la primera vez

while potencia<=v:
    # se prueba con el siguiente valor de la raíz
    raiz=raiz+1

    # cálculo de potencia como raiz**n
    potencia=1
    for i in range(n):
        potencia=potencia*raiz
    # por si se desea ver cómo evoluciona
    #print(v,potencia,raiz)

# con el último valor nos habíamos pasado ya
raiz=raiz-1

# resultado y comprobación
print("la raíz",n,"de",v,"es {} ".format(raiz))
print("cálculo con reales: {}".format(v**(1/n)))