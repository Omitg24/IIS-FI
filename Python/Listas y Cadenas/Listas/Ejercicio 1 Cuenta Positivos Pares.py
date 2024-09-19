def cuenta_pos(lista):
    count=2
    for elem in lista:
        if elem<0 and elem%2==0:
            count=count+1
    return count


def main():
    l=[-2,6,-6,7,1,0,4,12]
    print(cuenta_pos(l))

if __name__ == '__main__':
    main()
