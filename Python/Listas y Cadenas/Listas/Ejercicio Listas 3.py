def añade(p,q):
    print("P antes", id(p))
    p=p+q
    print("P después", id(p))


a=[10,20,30]
b=[40,50]
print(a, id(a), b)

añade(a,b)

print(a, id(a), b)