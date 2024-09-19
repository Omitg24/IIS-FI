n=int(input("Introduzca el número: "))
suma1=0
suma2=0
quantity1=0
quantity2=0
while n>=0:
    n=int(input("Introduzca el número: "))
    if n<0:
        print("La media de los pares es {}".format(suma1/quantity1))
        print("La media de los impares es {}".format(suma2/quantity2))
    if n%2==0:
        suma1=suma1+n
        quantity1=quantity1+1
    if n%2!=0:
        suma2=suma2+n
        quantity2=quantity2+1
