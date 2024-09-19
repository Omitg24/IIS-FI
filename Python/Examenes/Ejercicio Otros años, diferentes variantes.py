for numero in range(1000,10000):
    cifra1=numero//1000
    cifra2=numero//100%10
    cifra3=numero//10%10
    cifra4=numero%10
    suma=cifra1+cifra2+cifra3+cifra4
    if suma==10 and cifra1!=7 and cifra2!=7 and cifra3!=7 and cifra4!=7:
        print(numero)

for cifra1 in range(1,10):
    for cifra2 in range(10):
        for cifra3 in range(1):
            for cifra4 in range(10):
                suma=cifra1+cifra2+cifra3+cifra4
                if suma==10 and cifra1!=7 and cifra2!=7 and cifra3!=7 and cifra4!=7:
                    numero=cifra1*1000+cifra2*100+cifra3*10+cifra4
                    print(numero)

