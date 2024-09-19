## Escriba un programa en Python que imprima todos los números de 4 cifras
## tales que la suma de sus cifras es 10 y ninguna de ellas es 7.


for i in range(1000,10000):
    count=0
    suma=0
    for j in str(i):
        ji = int(j)
        if(ji==7):
            count=count+1
    if(count==0):
        c=0
        for d in str(i):
            dig=int(d)
            suma=suma+dig
            c=c+1
            if(c==1):
                d1=dig
            elif(c==2):
                d2=dig
            elif(c==3):
                d3=dig
            elif(c==4):
                d4=dig
        if(suma==10):
            print(f"{i} : {d1} + {d2} + {d3} + {d4} = {suma}")




