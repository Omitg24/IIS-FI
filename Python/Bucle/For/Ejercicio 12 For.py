n=int(input("Introduzca un número: "))
suma=0

if n<=0:
    print("Número mayor que cero")
else:
    print("Los divisores son: ", end=" ")
    for i in range(1, n+1):
        if n%i==0:
            print(i,end=" ")
        suma=suma+i
        if (suma==n):
            print(f"El número {n} es perfecto (ya que {suma}={n})", end="")
        elif(suma>n):
            print(f"El número {n} es abundante (ya que {suma}>{n})", end="")
        else:
            print(f"El número {n} es defectivo y primo (ya que {suma}<{n})", end=" ")

