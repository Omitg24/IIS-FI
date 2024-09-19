##a=list(input("Introduce la lista: "))
##b=list(input("Introduce la lista: "))
##
##if len(a)>len(b):
##    distanica=len(a)-len(b)
##elif len(a)<len(b):
##    distancia=len(b)-len(a)
##elif len(a)==len(b):
##    distancia=len(a)-len(b)
##
##print("La distancia entre ", a, " y ", b, " es ", distancia)

def distancia(a,b):
    dist1=abs(len(a)-len(b))

    dist2=0
    for i in range(min(len(a),len(b))):
        if a[i]!=b[i]:
            diost2=dist2+1

    return dist1+dist2

print(distancia([1,2,3,4],[10,20,3]))