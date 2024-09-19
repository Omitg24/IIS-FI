def añade(p,q):
    print("p antes", p, id(p))
##    p=p+q

##    for i in reange(len(q)):
##        p.append(q[i])

##    for elem in q:
##        p.append(elem)

    p[:]=p+q
    print("p después", p, id(p))

a=[10,20,30]
b=[40,50]
print(a, id(a), b)

añade(a,b)

print(a, id(a), b)