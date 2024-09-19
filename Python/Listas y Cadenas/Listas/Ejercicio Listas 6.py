def quita_ultimo(p):
    print("P antes", p, id(p))
##  p=p[:-1]
    p.pop()
    print("P despues", p, id(p))

a=[10,20,30]
print("a antes", a , id(a))
quita_ultimo(a)
print("a despues", a, id(a))