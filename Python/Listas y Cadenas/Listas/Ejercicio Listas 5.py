def add(p,v):
    print("P antes", p, id(p))
##    p=p+[v]
    p.append(v)
    print("P despues", p, id(p))

a=[10,20,30]
print("a antes", a , id(a))
add(a,40)
print("a despues", a, id(a))