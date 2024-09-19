from tkinter import *
import tresenraya
import calculadora
import agenda
def principal():
    "Función que crea la pantalla inicial y que nos mostrará todas las opciones que podemos elegir mediante botones"
    main=Tk()   #Creamos la pantalla
    main.geometry("500x500")    
    main.title("Aplicaciones varias")   
    main.configure(bg="LightCyan2")
    titulo=Label(main,text="Bienvenido, selecciona una función",font=("Helvetica",17,"bold"),bg="navy",fg="gold")   
    titulo.place(x=40,y=30)
    tres_en_raya=Button(main,text="3 en raya",height=3,width=12,bg="navy",fg="gold",font=("Helvatica",10,"bold"),command=lambda:tresenraya.menu_tres_en_raya()) #boton de la opción tres en raya
    tres_en_raya.place(x=35,y=200)
    menu_calculadora=Button(main,text="Calculadora",height=3,width=12,bg="navy",fg="gold",font=("Helvatica",10,"bold"),command=lambda:calculadora.calculadora_menu())   #boton de la opción calculadora
    menu_calculadora.place(x=185,y=200)
    menu_agenda=Button(main,text="Agenda",height=3,width=12,bg="navy",fg="gold",font=("Helvatica",10,"bold"),command=lambda:agenda.menu_agenda())   #boton de la opción agenda
    menu_agenda.place(x=335,y=200)
    main.mainloop()  #mostramos la pantalla
principal()