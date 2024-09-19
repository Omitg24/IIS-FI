def mostrar_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=" ")
        print()

def zeros(filas,columnas):
    a=[]
    for i in range(filas):
        a.append([0]*columnas)
    return a


lista=zeros(5,5)
mostrar_matriz(lista)
