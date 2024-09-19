import tkinter      #Importar el tkinter
from tkinter import Entry

def note():
    note=str(input("Introduzca la nota a añadir o eliminar: "))    #Entrada de la nota a añadir o eliminar
    return note    #Devuelve la nota introducida
    """Función que pide por teclado una nota, su uso es para añadir o eliminar dicha nota,
    a traves de otras funciones"""

def add_note():
    print()
    f=open('agenda.csv','a')    #Abre el fichero
    n=int(input("Introduzca el número de notas a añadir: "))    #Entrada del número de notas a añadir
    for i in range(n):  #Bucle for que añade al fichero las notas escritas, siendo las notas tantas como el valor de n
        f.write(note())     #Escribe la nota introducida con note() en el fichero
        f.write("\n")   #Escribe un salto de linea para darle formato de lista al fichero
    f.close()       #Cierra el fichero
    print("Se han añadido las anteriores notas")
    """Función que añade una o varias notas (en función del valor añadido),
    y posteriormente solicita que añadas X notas, a través de la funcion note(),
    escribiendolas todas en el fichero previamente abierto"""

def remove_note():
    print()
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
    print("Se ha eliminado la anterior nota")
    """Función que elimina una nota introducida por teclado (función note())
    del fichero convertido en lista y después lo reescribe sobre el fichero,
    haciendo que haya una nueva lista sin que esa nota forme parte de ella"""

def remove_allNotes():
    print()
    f=open('agenda.csv','r')    #Abre el fichero
    lineas=f.readlines()    #Lee el fichero y lo convierte en una lista
    lista=[item.strip('\n') for item in lineas]     #Transforma la lista con: '\n' a una común
    lista.clear()   #Vacía la lista
    f.close()   #Cierra el fichero
    nueva="".join(lista)    #Hace que la lista no sea nada, elimina los corchetes []
    n=open('agenda.csv','w')    #Abre de nuevo el fichero
    n.write(str(nueva))     #Sobrescribe lo que habia anteriormente haciendo que el fichero este vació
    n.close()   #Cierra el fichero
    print("Se eliminaron todas las notas")
    """Función que abre la agenda y elimina todos los elementos de la lista formada por esa agenda,
    para posteriormente sobrescribir la lista resultante (nula) sobre la agenda original,
    haciendo así que se elimine su contenido"""

##Implementación de la parte grafica (tkinter)

def crearVentana():
    ventana2 = tkinter.Tk()     #Creación de la ventana
    ventana2.geometry("275x300")    #Formato de la ventana, medidas
    ventana2.configure(bg="LightCyan2") #Formato de la ventana, color de fondo

    etiqueta2=tkinter.Label(ventana2, text = "¿Quiere eliminar una o todas las notas?", bg="navy", fg="gold", font=15)      #Etiqueta de texto de la ventana, con color, fondo y fuente
    etiqueta2.pack(fill=tkinter.X)      #Cubrir todo el eje X en el que esta la etiqueta

    boton3=tkinter.Button(ventana2, text = "Una", bg="blue", fg="aquamarine", padx=25, pady=15, command=remove_note, font=10)   #Boton Una, llamada a funcion remove_note(), con color, fondo y fuente
    boton3.pack(side=tkinter.LEFT)      #Situar el boton en la ventana (en este caso, izquierda)

    boton4=tkinter.Button(ventana2, text = "Todas", bg="blue", fg="aquamarine", padx=25, pady=15, command=remove_allNotes, font=10)     #Boton Todas, llamada a funcion remove_allNotes(), con color, fondo y fuente
    boton4.pack(side=tkinter.RIGHT)     #Situar el boton en la ventana (en este caso, derecha)

    ventana2.mainloop()     #Impresion de la ventana
    """"Función que crea una nueva ventana en la que estás las funciones enfocadas
    a eliminar notas del fichero, si se pulsa Una, se eliminara la nota introducida por teclado,
    si se pulsan todas, desaparecen todas"""

def main():

    ventana = tkinter.Tk()      #Creación de la ventana
    ventana.geometry("250x300")     #Formato de la ventana, medidas
    ventana.configure(bg="LightCyan2")      #Formato de la ventana, color de fondo

    etiqueta=tkinter.Label(ventana, text = "¿Quiere añadir o eliminar notas?", bg="midnight blue", fg="gold", font=20)      #Etiqueta de texto de la ventana, con color, fondo y fuente
    etiqueta.pack(fill=tkinter.X)       #Cubrir todo el eje X en el que esta la etiqueta

    boton1=tkinter.Button(ventana, text = "Añadir", bg="blue", fg="aquamarine", padx=25, pady=15, command=add_note, font=15)        #Boton Añadir, llamada a funcion remove_note(), con color, fondo y fuente
    boton1.pack(side=tkinter.LEFT)      #Situar el boton en la ventana (en este caso, izquierda)

    boton2=tkinter.Button(ventana, text = "Eliminar", bg="blue", fg="aquamarine", padx=25, pady=15, command=crearVentana, font=15)      #Boton Eliminar, llamada a funcion crearVentana(), que crea la ventana con las dos posibilidades de eliminar notas; con color, fondo y fuente
    boton2.pack(side=tkinter.RIGHT)     #Situar el boton en la ventana (en este caso, derecha)

    ventana.mainloop()      #Impresión de la ventana
    """Función principal que recoge todas las funciones anteriores, haciendo que se ejecuten
    de una manera visual, mediante el tkinter, consta de dos botones, al pulsar añadir,
    llama a la función add_note, y al pulsar eliminar crea otra ventana que contiene las dos opciones posibles"""

if __name__ == '__main__':
    main()