def mostrarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()

def trasponerMatriz(m):
    result=[]
    for j in range(len(m[0])):
        fila=[]
        for i in range(len(m)):
            fila.append(m[i][j])
        result.append(fila)
    m.clear()
    m.extend(result)

def main():
    mat=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    trasponerMatriz(mat)
    print("La matriz traspuesta es: ")
    mostrarMatriz(mat)

if __name__ == '__main__':
    main()
