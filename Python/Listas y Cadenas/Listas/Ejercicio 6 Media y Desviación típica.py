from math import sqrt

def media(lista):
    promedio=0
    for i in range(len(lista)):
        promedio=sum(lista)/len(lista)
    return promedio

def desviación(lista):
    numerador=0
    suma=0
    for i in range(len(lista)):
        numerador=(lista[i]-media(lista))**2
        suma=suma+numerador
##        print(numerador)
    return sqrt(suma/len(lista))

n=int(input("Introduzca el tamaño de la lista: "))
lista=[]
for i in range(n):
    lista.append(int(input("Introduzca un número: ")))
print("La lista es",lista)
print("La media es: ", media(lista), " y su desviación típica es: ", desviación(lista))

