def main():
    v=float(input())
    suma=0
    i=0
    while suma<v:
        i=i+1
        suma=suma+(1.0/i)
    n=i-1
    print(n)
if __name__ == '__main__':
    main()
