def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact

def main():
    n=int(input("Introduce un número: "))
    while n<=0:
        n=int(input("El número debe ser mayor que 0, introduce otro número:  "))

    for i in range(0,n+1):
        print(i, "!=", factorial(i))

if __name__ == '__main__':
    main()
