def mostrarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()

def generarIdentidad(tam):
    result=[]
    for i in range(tam):
        fila=[0]*tam
        fila[i]=1
        result.append(fila)
    return result
def main():
    tam=int(input("Introduce el tamaño"))
    m=generarIdentidad(tam)
    mostrarMatriz(m)

if __name__ == '__main__':
    main()
