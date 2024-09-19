i=100
contador1=0
contador3=0
contador5=0
contador7=0

while i<=1000:
    for j in range(i-1,2,-1):
        if(i%j!=0):
            continue
        else:
            break
    else:
        print(i)
        if i%10==1:
            contador1=contador1+1
        elif i%10==3:
            contador3=contador3+1
        elif i%10==5:
            contador5=contador5+1
        elif i%10==7:
            contador7=contador7+1
    i=i+1
if(contador1>contador3 and contador1>contador5 and contador1>contador7):
    print(f"La cifra que más se acaba es en 1 y se repite un total de {contador1}")
if(contador3>contador1 and contador3>contador5 and contador3>contador7):
    print(f"La cifra que más se acaba es en 3 y se repite un total de {contador3}")
if(contador5>contador1 and contador5>contador3 and contador5>contador7):
    print(f"La cifra que más se acaba es en 5 y se repite un total de {contador5}")
else:
    print(f"La cifra que más se acaba es en 7 y se repite un total de {contador7}")

