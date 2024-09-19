f=open('Fichero.csv','r')
datos=f.read()
f.close()

count_a=0
count_e=0
count_i=0
count_o=0
count_u=0

for i in range(len(datos)):
    if "a" in datos[i]:
        count_a=count_a+1
    if "e" in datos[i]:
        count_e=count_e+1
    if "i" in datos[i]:
        count_i=count_i+1
    if "o" in datos[i]:
        count_o=count_o+1
    if "u" in datos[i]:
        count_u=count_u+1

print(count_a)
print(count_e)
print(count_i)
print(count_o)
print(count_u)