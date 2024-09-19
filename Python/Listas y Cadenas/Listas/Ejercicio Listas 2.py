def incr(p):
    print(id(p))
    for i in range(len(p)):
        p[i]=p[i]+1

a=[10,20,30]
print(a)
incr(a)
print(a)