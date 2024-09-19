def cambiar_negativo(lista):
    l2=[]
    for i in range(len(lista)):
        if lista[i]>0 and lista[i]%2==0:
            l2.append(lista[i])
            lista[i]=-lista[i]
    return l2


def main():
    l=[-2,6,-6,7,1,0,4,12]
    l_result=cambiar_negativo(l)
    print(len(l_result))
    print(l_result)


if __name__ == '__main__':
    main()
