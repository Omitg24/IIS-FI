def pedir_entero():
    n=int(input())
    while n<0:
        n=int(input())
    return n
def main():
    n=pedir_entero()
    l=[]
    while n!=0:
        l.append(n)
        n=pedir_entero()
    print(l)
    q=sorted((l))
    print(q)
    print(q[len(q)-1],q[len(q)-2],q[len(q)-3])


if __name__ == '__main__':
    main()
