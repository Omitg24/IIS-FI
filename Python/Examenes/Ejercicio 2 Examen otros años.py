# Escriba un programa Python que descubra todos los números de cuatro cifras,
# es decir, en el rango 1000 a 9999, que son capicúas. La salida debe mostrar
# en la misma línea (si caben) los números del mismo millar. Tras mostrar los
# números de cada millar que cumplan la propiedad, debe imprimir una línea de
# 80 asteriscos y continuar. Así, por ejemplo

count=0
for i in range(1000,10000):
    ai=""
    for j in str(i):
        js=str(j)
        ai=js+ai
    if(str(i)==ai):
        print(i, end=" ")
        count=count+1
    if(count==10):
        print()
        print("*"*80)
        count=0
