##Dados  dos  números  naturales my n,  escribe  un  programa  que  muestre  en
##pantalla  la siguiente matriz de mfilas y ncolumnas

n=int(input("Introduzca el número de columnas: "))
m=int(input("Introduzca el número de filas: "))

for i in range(1,m+1):
    print()
    for j in range(1,n+1):
        print(f"A{i}x{j}", end=" ")
