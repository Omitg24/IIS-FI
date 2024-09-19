## Haga un programa en Python que pida un número real v y un entero n y que sin
## emplear el operador ** ni las funciones matemáticas permita obtener una raíz
## n-sima entera de v. Se supondrá que todos los números son positivos.
##
## Es decir, hallar el mayor entero r tal que r**n<=v:
##
## Omar Teixeira González, UO281847

v=int(input("Introduzca el número real, debe ser mayor que 0: "))
n=int(input("Introduzca el índice de la raíz, debe ser mayor que 0: "))

for j in range(int(v),1,-1):
    r=j
    for k in range(2,n+1):
        j=j*r
    if j<=v and j*r>n:
        break

print(f"La raíz n-sima de índice {n} del número real {v} es {r}")