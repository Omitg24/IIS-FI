import tkinter      #Importar el tkinter
from tkinter import Entry       #Importar la clase Entry
from tkinter import END     #Importar la clase END

def crearVentana():

    ventana2 = tkinter.Tk()     #Creación de la ventana
    ventana2.geometry("500x500")    #Formato de la ventana, medidas
    ventana2.configure(bg="LightCyan2") #Formato de la ventana, color de fondo

    def remove_note():

        etiqueta_espacio=tkinter.Label(ventana2, bg="LightCyan2")
        etiqueta_espacio.pack(fill=tkinter.X)

        etiqueta4=tkinter.Label(ventana2, text = "Introduzca la nota a eliminar: ", bg="royal blue", fg="CadetBlue1", font=25)      #Etiqueta de texto de la funcion remove, con color, fondo y fuente
        etiqueta4.pack(fill=tkinter.X)       #Cubrir todo el eje X en el que esta la etiqueta

        etiqueta_espacio2=tkinter.Label(ventana2, bg="LightCyan2")
        etiqueta_espacio2.pack(fill=tkinter.X)

        entrada2=Entry(ventana2, width=50)
        entrada2.pack()

        etiqueta_espacio3=tkinter.Label(ventana2, bg="LightCyan2")
        etiqueta_espacio3.pack(fill=tkinter.X)

        f=open('agenda.csv','r')    #Abre el fichero
        lineas=f.readlines()    #Lee el fichero y lo convierte en una lista
        lista=[item.strip('\n') for item in lineas]    #Transforma la lista con: '\n' a una común
        f.close()   #Cierra el fichero

        def remove():

            lista.remove(str(entrada2.get()))    #Elimina la nota introducida con note() de la lista

            n=open('agenda.csv','w')    #Abre de nuevo el fichero
            for i in range(len(lista)):     #Bucle for para reescribir la nueva lista con la nota eliminada sobre el fichero
                n.write(lista[i])   #Escribe la lista sin la nota a traves del indice dado en el bucle
                n.write('\n')   #Escribe un salto de linea para darle formato de lista al fichero
            n.close()   #Cierra el fichero

            entrada2.delete(0,END)      #Eliminar el contenido de la ventana

            """Función que elimina de la lista obtenida anteriormente el elemento
            introducido en la entrada del tkinter y despues lo sobrescribe sobre
            el fichero agenda.csv, eliminado así, dicho arcivo del fichero"""

        boton_remove=tkinter.Button(ventana2, text = "Eliminar", bg="steel blue", fg="DarkSlateGray1", font=20, command=remove)     #Boton Eliminar, llamada a funcion remove(), con color, fondo y fuente
        boton_remove.pack()

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

    etiqueta2=tkinter.Label(ventana2, text = "¿Quiere eliminar una o todas las notas?", bg="navy", fg="gold", font=15)      #Etiqueta de texto de la ventana, con color, fondo y fuente
    etiqueta2.pack(fill=tkinter.X)      #Cubrir todo el eje X en el que esta la etiqueta

    boton3=tkinter.Button(ventana2, text = "Una", bg="blue", fg="aquamarine", padx=25, pady=15, command=remove_note, font=10)   #Boton Una, llamada a funcion remove_note(), con color, fondo y fuente
    boton3.place(x=100,y=250)      #Situar el boton en la ventana (en este caso, izquierda)

    boton4=tkinter.Button(ventana2, text = "Todas", bg="blue", fg="aquamarine", padx=25, pady=15, command=remove_allNotes, font=10)     #Boton Todas, llamada a funcion remove_allNotes(), con color, fondo y fuente
    boton4.place(x=300,y=250)     #Situar el boton en la ventana (en este caso, derecha)

    ventana2.mainloop()     #Mostrar la ventana

    """"Función que crea una nueva ventana en la que estás las funciones enfocadas
    a eliminar notas del fichero, si se pulsa Una, se eliminara la nota introducida por teclado,
    si se pulsan todas, desaparecen todas"""

def main():

    ventana = tkinter.Tk()      #Creación de la ventana
    ventana.geometry("500x500")     #Formato de la ventana, medidas
    ventana.configure(bg="LightCyan2")      #Formato de la ventana, color de fondo

    etiqueta=tkinter.Label(ventana, text = "¿Quiere añadir o eliminar notas?", bg="midnight blue", fg="gold", font=20)
    etiqueta.pack(fill=tkinter.X)

    def add_note():
        etiqueta_espacio=tkinter.Label(ventana, bg="LightCyan2")
        etiqueta_espacio.pack(fill=tkinter.X)

        etiqueta4=tkinter.Label(ventana, text = "Introduzca la nota a añadir: ", bg="royal blue", fg="CadetBlue1", font=25)
        etiqueta4.pack(fill=tkinter.X)

        etiqueta_espacio2=tkinter.Label(ventana, bg="LightCyan2")
        etiqueta_espacio2.pack(fill=tkinter.X)

        entrada2=Entry(ventana, width=50)
        entrada2.pack()

        etiqueta_espacio3=tkinter.Label(ventana, bg="LightCyan2")
        etiqueta_espacio3.pack(fill=tkinter.X)

        def add():

            f=open('agenda.csv','a')    #Abre el fichero
            f.write(str(entrada2.get()))    #Escribe la nota introducida con note() en el fichero
            f.write("\n")   #Escribe un salto de linea para darle formato de lista al fichero
            f.close()       #Cierra el fichero

            entrada2.delete(0,END)      #Eliminar el contenido de la entrada

            """Función que añade una o varias notas (en función de las que queramos) al archivo agenda.csv"""

        boton_add=tkinter.Button(ventana, text = "Añadir", bg="steel blue", fg="DarkSlateGray1", font=20,command=add)
        boton_add.pack()

    """Función que crea unas etiquetas y una entrada para añadir el contenido de
    esta ultima al fichero agenda.csv, su llamada se produce mediante el boton
    "Añadir" en la ventana de tkinter"""

    boton1=tkinter.Button(ventana, text = "Añadir", bg="blue", fg="aquamarine", padx=25, pady=15, command=add_note, font=15)        #Boton Añadir, llamada a funcion remove_note(), con color, fondo y fuente
    boton1.place(x=100,y=250)      #Situar el boton en la ventana (en este caso, izquierda)

    boton2=tkinter.Button(ventana, text = "Eliminar", bg="blue", fg="aquamarine", padx=25, pady=15, command=crearVentana, font=15)      #Boton Eliminar, llamada a funcion crearVentana(), que crea la ventana con las dos posibilidades de eliminar notas; con color, fondo y fuente
    boton2.place(x=300,y=250)     #Situar el boton en la ventana (en este caso, derecha)

    ventana.mainloop()      #Impresión de la ventana

    """Función principal que recoge todas las funciones anteriores, haciendo que se ejecuten
    de una manera visual, mediante el tkinter, consta de dos botones, al pulsar añadir,
    llama a la función add_note, y al pulsar eliminar crea otra ventana que contiene las dos opciones posibles, remove_note y remove_allNotes"""

if __name__ == '__main__':
    main()