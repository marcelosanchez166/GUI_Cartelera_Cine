from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Sized
import Detalles_Movies

from tkcalendar import Calendar


"""Las ventanas emegentes no vienen con la biblioteca de tkinter hay que importarlas por aparte"""
from tkinter import messagebox

raiz = Tk()
raiz.title(" Cartelera de Cine ")
raiz.geometry("750x750")
raiz.config(bg="#A9A9A9")

selected_movie = StringVar()


# ---------------------funcion para crear una ventana emergente-----------------
Descuento = 0.10
Entrada = 2.50


def MostrarDatos():
    Nclientes = 0
    Nclientes = float(Cantidad_Cliente.get())
    #diccionario={"peli":pelicula.get(), "cancliente":Cantidad_Cliente.get() }
    #dato=messagebox.showinfo("Cartelera", diccionario)
    lista = []
    lista.append(pelicula.get())
    # print(type(Cantidad_Cliente.get()))
    lista.append(Cantidad_Cliente.get())
    frec = lista.append(frecuente.get())
    Message.insert(END, "\n")
    Message.insert(END, "-----------------------------")
    Message.insert(END, "\n")
    Message.insert(END, "Pelicula: ")
    # Se le pasa al label la opcion escogida
    Message.insert(END, lista[0]+"\n")
    Message.insert(END, "Clientes: ")
    Message.insert(END, lista[1]+"\n")
    Message.insert(END, "Cliente Frecuente: ")
    Message.insert(END, lista[2]+"\n")
    Message.insert(END, "Fecha de funcion: ")
    Message.insert(END, cal.get_date()+"\n")
    Message.insert(END, "Idioma: ")
    Message.insert(END, SelecIdioma.get() + "\n")

    if frecuente.get() == "Si":
        Message.insert(END, "Se aplicara descuento del 10% "+"\n")
        # print(type(Nclientes))
        desc = Descuento*Entrada
        Preciototal = Entrada*Nclientes
        total = Preciototal-desc
        Message.insert(END, "Total a pagar: ")
        Message.insert(END, total, "\n")
    else:
        Message.insert(END, "No se aplicara descuentos "+"\n")
        Preciototal = Entrada*Nclientes
        Message.insert(END, "Total a pagar: ")
        Message.insert(END, Preciototal, " \n ")


# Label para mostrar lo que el usuario ha seleccionado
Message = Text(raiz, width=50, height=10)
Message.grid(row=9, column=0, padx=10, columnspan=10)


Personas = Label(raiz, text="Personas ", padx=29)
Personas.grid(row=0, column=0)
Personas.config(bg="#8A2BE2", fg="#000000", font="italic")
Cantidad_Cliente = ttk.Combobox(raiz)
Cantidad_Cliente["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cantidad_Cliente.current(0)
Cantidad_Cliente.grid(row=0, column=1)


PeliLabel = Label(raiz, text="Peliculas ", padx=31)
PeliLabel.grid(row=3, column=0)
PeliLabel.config(bg="#8A2BE2", fg="#000000", font="italic")
pelicula = ttk.Combobox(raiz, textvariable=selected_movie)
pelicula["values"] = ["Harry potter",
                      "Donde estan las rubias", "Jurasic World"]
# sirve para que aparezca una opcion por defecto en el combobox, se le pone la posicion del valor que quiero que salga
pelicula.current(0)
pelicula.grid(row=3, column=1)


Clientefrecuente = Label(raiz, text="Cliente Frecuente ")
Clientefrecuente.config(bg="#8A2BE2", fg="#000000", font="italic")
Clientefrecuente.grid(row=6, column=0)
frecuente = ttk.Combobox(raiz)
frecuente["values"] = ["Si", "No"]
frecuente.current(0)
frecuente.grid(row=6, column=1)


# ------------------------Seleccion de Idioma----------------------------------
IdiomaLB = Label(raiz, text="Idioma ", padx=39)
IdiomaLB.config(bg="#8A2BE2", fg="#000000", font="italic")
IdiomaLB.grid(row=7, column=0)
SelecIdioma = ttk.Combobox(raiz)
SelecIdioma["values"] = ["Español DOB", "English", "Eng sub Español"]
SelecIdioma.current(0)
SelecIdioma.grid(row=7, column=1)


# ------------------Calendario Horario------------------------------------------------------

cal = Calendar(raiz, selectmode='day', year=2021, month=5, day=22)
cal.grid(row=9, column=10, pady=5)


# --------------------------------------------------------------------------------------------


# crea un boton con texto dentro y se le pasa la funcion boton1
Enviarboton = Button(raiz, width=10, text="Mostrar", command=MostrarDatos)
Enviarboton.config(bg="#008B8B", fg="#191970", font="cursiva")
Enviarboton.grid(row=12, column=0, pady=10)


# -----------------------------Boton y funcion borrar contenido de un cuadro grande de texto-------------
def Borrar():
    Message.delete(1.0, END)


botondelete = Button(raiz, text="Eliminar Datos",
                     width=12, command=lambda: Borrar())
botondelete.config(bg="#008B8B", fg="#191970", font="cursiva")
botondelete.grid(row=12, column=1, columnspan=8)


raiz.mainloop()
