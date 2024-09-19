n=int(input("Introduzca el número: "))
quantity=0
suma=0

while n>=0:
    n=int(input("Introduzca el número: "))
    suma=suma+n
    quantity=quantity+1
    if n<0:
        print("La media es {}".format(suma/quantity))