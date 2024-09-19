def suma_divisores(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma=suma+i
    return suma

def main():
    n=int(input("Introduzca el número: "))
    print(suma_divisores(n))
    if n==suma_divisores(n):
        print("Es perfecto")
    else:
        print("No lo es")

if __name__ == '__main__':
    main()
