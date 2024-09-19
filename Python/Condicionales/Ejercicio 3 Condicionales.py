a=int(input("Número entero 1: "))
b=int(input("Número entero 2: "))
c=int(input("Número entero 3: "))
d=int(input("Número entero 4: "))
e=int(input("Número entero 5: "))

if a>b and a>c and a>d and a>e:
    print("El mayor de los cinco es {}".format(a))
elif b>a and b>c and b>d and b>e:
    print("El mayor de los cinco es {}".format(b))
elif c>a and c>b and c>d and c>e:
    print("El mayor de los cinco es {}".format(c))
elif d>a and d>b and d>c and d>e:
    print("El mayor de los cinco es {}".format(d))
elif e>a and e>b and e>c and e>d:
    print("El mayor de los cinco es {}".format(e))
