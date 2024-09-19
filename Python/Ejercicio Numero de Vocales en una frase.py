frase=str(input("Ingrese una frase: "))
count=0
for i in frase:
    if i in "aeiou":
        count=count+1
print(count)

