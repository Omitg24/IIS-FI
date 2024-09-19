def fibonacci(n):
    result=[]
    if n>0:
        result.append(0)
    if n>1:
        result.append(1)
    for i in range(2,n):
        result.append(result[-1]+result[-2])
    return result


def main():
    n=int(input("Introduzca el número de elementos: "))
    lista=fibonacci(n)
    print(lista)

if __name__ == '__main__':
    main()
