n=0
while n<3:
    n=n+1
    m=0
    while m<3:
        m=m+1
        if n%2==m%2:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()