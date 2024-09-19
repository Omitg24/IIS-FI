def mostrarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()

def simetrica(m):
    for i in range(len(m)):
        for j in range(i+1,len(m[i])):
            if m[i][j]!=m[j][i]:
                return False
    return True

def main():
    m=[[0,1,2],[1,3,4],[2,4,5]]
    mostrarMatriz(m)
    if simetrica(m):
        print("Es simetrica")
    else:
        print("No es simetrica")

if __name__ == '__main__':
    main()
