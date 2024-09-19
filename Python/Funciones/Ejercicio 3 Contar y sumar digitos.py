def suma_digitos(n):
    suma=0
    while n!=0:
        suma=suma+n%10
        n=n//10
    return suma

def cuenta_digitos(n):
    c=0
    while n!=0:
        c=c+1
        n=n//10
    return c

def main():
    n=int(input("Introduce un número (>=0) "))
    while n<0:
        n=int(input("Introduce un número (>=0) "))
    print (cuenta_digitos(n))
    print (suma_digitos(n))

if __name__ == '__main__':
    main()
