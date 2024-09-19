def sucesion(b,c,d,k):
    if k==0:
        return b
    elif k>0:
        return c*(k-1)+d

def main():
    b=int(input("Introduce el primer término: "))
    c=int(input("Introduce el parámetro: "))
    d=int(input("Introduce el segundo parámetro: "))
    k=int(input("Introduce el número de repeticiones: "))
    print(sucesion(b,c,d,k))

if __name__ == '__main__':
    main()
