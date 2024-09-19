n=int(input("Introduzca un número: "))

if n<=0:
    print("Número mayor que cero")
else:
    print("Los divisores son: ", end=" ")
    for i in range(1, n+1):
        if n%i==0:
            print(i, end=" ")