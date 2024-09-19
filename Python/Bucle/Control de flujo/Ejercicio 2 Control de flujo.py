##Dado un número natural n, escribe un programa para mostrar en pantalla un
##rectángulo de nfilas y, en cada fila, nasteriscos.

n=int(input("Introduzca el lado del rectangulo"))

for j in range(n):
    print()
    for i in range(n):
        print("*",end=" ")