def main():
    n=int(input("Introduce un número (>=0) "))
    while n<0:
        n=int(input("Introduce un número (>=0)"))
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma=suma+i

    if suma==n:
        print("Es perfecto")
    elif suma>n:
        print("Es abundante")
    else:
        print("Es negativo")

if __name__ == '__main__':
    main()
