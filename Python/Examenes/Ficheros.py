3.#Se trata de hacer un programa que cuente diversos tipos de instrucciones
#De un fichero que contiene un programa python
#Contará asignaciones, condicionales simples,condicionales compuestos, bucles, y otros tipos de instrucciones

def main():
    f=open("Funciones.txt","r")
    datos=f.readlines()
    count_a=0
    count_is=0
    count_ic=0
    count_b=0
    for i in range(len(datos)):
        if "=" in datos[i] and "==" not in datos[i]:
            count_a=count_a+1
        if "if" in datos[i] and "elif" not in datos[i]:
            count_is=count_is+1
        if "elif" in datos[i] or "else" in datos[i]:
            count_ic=count_ic+1
        if "for" in datos[i] or "while" in datos[i]:
            count_b=count_b+1
    f.close()
    print(f"El número de asignaciones es {count_a}, el de condicionales simples es {count_is}, el de condicionales compuestas es {count_ic} y el de bucles es {count_b}")

if __name__ == '__main__':
    main()