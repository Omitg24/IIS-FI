def mcd(a,b):
    for i in range(min(a,b),1,-1):
        if a%i==0 and b&i == 0:
            return i
    return i

def main():
    a=int(input("Introduzca el primer número: "))
    while a<=0:
        a=int(input("Introduzca el primer número, debe ser mayor que 0: "))

    b=int(input("Introduzca el segundo número: "))
    while b<=0:
        b=int(input("Introduzca el segundo número, debe ser mayor que 0: "))

    print(mcd(a,b))

if __name__ == '__main__':
    main()
