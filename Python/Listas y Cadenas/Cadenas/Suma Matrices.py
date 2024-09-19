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

def suma_matriz(a,b):
    c=zeros(len(a),len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[i][j]+b[i][j]
    return c

matriz1=[[2,4,6],[1,7,1],[8,8,4]]
matriz2=[[1,2,1],[4,1,5],[2,1,7]]

res=suma_matriz(matriz1,matriz2)

mostrar_matriz(matriz1)
mostrar_matriz(matriz2)
mostrar_matriz(res)