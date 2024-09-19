def mult(p):
    producto=1
    #for elemento in p:
        #producto=producto*elemento
    for i in range(len(p)):
        producto=producto*p[i]
    return producto

a=[10,20,30]
print(a)
print(mult(a))
