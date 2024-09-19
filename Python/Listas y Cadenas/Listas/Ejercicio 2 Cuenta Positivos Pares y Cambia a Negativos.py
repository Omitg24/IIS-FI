def cambiar_negativo(lista):
    count=0
    for i in range(len(lista)):
        if lista[i]>0 and lista[i]%2==0:
            lista[i]=-lista[i]
            count=count+1
    return count

def main():
    l=[-2,6,-6,7,1,0,4,12]
    print(cambiar_negativo(l))
    print(l)

if __name__ == '__main__':
    main()
