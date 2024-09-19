a=int(input("Introduzca el primer límite: "))
b=int(input("Introduzca el segundo límite:"))

for i in range(a,b,1):
    if i%2==0:
        print(i, "(par)")
    else:
        print(i,"(impar)")
print()