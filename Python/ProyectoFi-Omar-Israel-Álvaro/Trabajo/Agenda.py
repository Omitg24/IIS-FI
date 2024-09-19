def note():
    note=str(input("Introduzca la nota a añadir o eliminar: "))    #Entrada de la nota a añadir o eliminar
    return note    #Devuelve la nota introducida
    """Función que pide por teclado una nota, su uso es para añadir o eliminar dicha nota,
    a traves de otras funciones"""

def add_note():
    f=open('agenda.csv','a')    #Abre el fichero
    n=int(input("Introduzca el número de notas a añadir: "))    #Entrada del número de notas a añadir
    for i in range(n):  #Bucle for que añade al fichero las notas escritas, siendo las notas tantas como el valor de n
        f.write(note())     #Escribe la nota introducida con note() en el fichero
        f.write("\n")   #Escribe un salto de linea para darle formato de lista al fichero
    f.close()       #Cierra el fichero
    """Función que añade una o varias notas (en función del valor añadido),
    y posteriormente solicita que añadas X notas, a través de la funcion note(),
    escribiendolas todas en el fichero previamente abierto"""

def remove_note():
    f=open('agenda.csv','r')    #Abre el fichero
    lineas=f.readlines()    #Lee el fichero y lo convierte en una lista
    lista=[item.strip('\n') for item in lineas]    #Transforma la lista con: '\n' a una común
    lista.remove(note())    #Elimina la nota introducida con note() de la lista
    f.close()   #Cierra el fichero
    n=open('agenda.csv','w')    #Abre de nuevo el fichero
    for i in range(len(lista)):     #Bucle for para reescribir la nueva lista con la nota eliminada sobre el fichero
        n.write(lista[i])   #Escribe la lista sin la nota a traves del indice dado en el bucle
        n.write('\n')   #Escribe un salto de linea para darle formato de lista al fichero
    n.close()   #Cierra el fichero
    """Función que elimina una nota introducida por teclado (función note())
    del fichero convertido en lista y después lo reescribe sobre el fichero,
    haciendo que haya una nueva lista sin que esa nota forme parte de ella"""

def remove_allNotes():
    f=open('agenda.csv','r')    #Abre el fichero
    lineas=f.readlines()    #Lee el fichero y lo convierte en una lista
    lista=[item.strip('\n') for item in lineas]     #Transforma la lista con: '\n' a una común
    lista.clear()   #Vacía la lista
    f.close()   #Cierra el fichero
    nueva="".join(lista)    #Hace que la lista no sea nada, elimina los corchetes []
    n=open('agenda.csv','w')    #Abre de nuevo el fichero
    n.write(str(nueva))     #Sobrescribe lo que habia anteriormente haciendo que el fichero este vació
    n.close()   #Cierra el fichero
    """Función que abre la agenda y elimina todos los elementos de la lista formada por esa agenda,
    para posteriormente sobrescribir la lista resultante (nula) sobre la agenda original,
    haciendo así que se elimine su contenido"""
a=str(input("¿Quiere añadir o eliminar notas? "))   #Entrada de que debe hacer el programa
if a=="Añadir" or a=="añadir":  #Condicional que si lo introducido es Añadir, ejecuta la función add_note() e imprime que se han añadido las notas
    add_note()  #llamada a la función add_note()
    print("Se han añadido las anteriores notas")    #Imprime "Se han añadido las anteriores notas"
elif a=="Eliminar" or a=="eliminar":    #Condicional que si lo introducido es Eliminar, solicita la entrada por teclado de otro variable para llamar a otra condicional
    b=str(input("¿Quiere eliminar una o todas las notas? "))    #Entrada de que debe eliminar el programa
    if b=="Una" or b=="una":    #Condicional que si lo introducido es Una, ejecuta la función remove_note() e imprime que se ha eliminado la anterior nota
        remove_note()   #Llamada a la función remove_note()
        print("Se ha eliminado la anterior nota")   #Imprime "Se ha eliminado la anterior nota"
    elif b=="Todas" or b=="todas":  #Condicional que si lo introducico es Todas, ejecuta la funcion remove_allNotes() e imprime que se han eliminado todas las notas
        remove_allNotes()   #Llamada a la funcion remove_allNotes()
    print("Se han eliminado todas las notas")   #Imprime "Se han eliminado todas las notas"
else:   #Condicional que si no se ha introducido la opción correcta imprime que no se han introducido las dos unicas opciones
    print("No se han introducido las dos opciones posibles")    #Imprime que no se han introducido las dos unicas opciónes posibles
"""Función principal que ejecuta el programa llamando al resto de funciones creadas"""

