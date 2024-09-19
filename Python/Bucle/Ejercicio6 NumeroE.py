# El número real e, con valor 2,718281828459045235..., puede calcularse de
# manera aproximada, donde nes  un  número  entero  no  negativo  cualquiera.
# A  mayor  valor  de n,  mayor  precisión  de  la aproximación.  Se  pide
# escribir  un  programa  en  Python  que  calcule  el  valor  del  número
# e utilizando para ello tantos términos de la suma anterior como sea necesario
# hasta que se cumpla que la diferencia entre el término para iy para i –1sea
# inferior a un umbral en el intervalo (0, 1] tomado por entrada.Nota: el valor
# del factorial lo puedes mantener acumulado en una variable auxiliar, de  modo
# que la incrementes (realices el producto consigo misma) en cada iteración del
# bucle

def main():
    pass

e_last=0.0
e_curr=0.0
count=0
factorial=1

threshold = float(input("Especicifa el umbral para el cálculo de e: "))
while threshold <=0.0 or threshold > 1.0:
    print("El umbral debe estar en el intervalo (0.0,1.0]")
    threshold= float(input("Especifica el umbral para el cáclculo de e: "))

finished=False
while not finished:
    e_last = e_curr
    e_curr = e_curr + 1 / factorial
    count = count+1
    factorial = factorial*count

    if e_curr - e_last <= threshold:
        finished = True
print("La aproximación de e tras {} iteraciones es {}".format(count,e_curr))

if __name__ == '__main__':
    main()
