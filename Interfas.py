from tkinter import *

"""Las ventanas emegentes no vienen con la biblioteca de tkinter hay que importarlas por aparte"""
from tkinter import messagebox



raiz=Tk()
raiz.title("Datos del Usuario ")
raiz.geometry("720x650")
raiz.config(background="gray")

#---------------------funcion para crear una ventana emergente-----------------
def InfoAdicional():
          #Ventana emergente de informacion 
          #pide dos parametros el titulo y el cuerpo de la ventana 
          messagebox.showinfo("Venatana de prueba de ventanas emergentes", "Esta es una app de prueba para probar todo lo aprendido")


#Ventana Emergente de Error
def ErrorDesconocido():
          messagebox.showerror("Fatal Error","Lo sentimos algo salio mal intenta mas tarde")

#Ventana emergente de Advertencia
def Advertencia():
          messagebox.showwarning("Cuidado", "Vuelve a intentarlo")

#Ventana emergente con opciones multiples
def Salir_Aplicacion():
          #El valor askquestion devuelve un valor ya sea yes o no
          valor=messagebox.askquestion("salir", "¿ Desea salir de la aplicacion ?")
          
          #El valor askokcancel ademas de cambiar los botones de la ventana emergente el valor que devuelve es TRUE o FALSE
          #valor=messagebox.askokcancel("salir", "¿ Desea salir de la aplicacion ?")
          if valor=="yes":
                    raiz.destroy()


def Reintentar():
          #El valor askretrycancel ademas de cambiar los botones de la ventana emergente el valor que devuelve es TRUE o FALSE
          valor=messagebox.askretrycancel("Reintentar", "¿ No se pudo abrir el archivo, Desea reintentarlo ?")



#--------------------------------Mostrar datos en ventana emergente---------------------
def MostrarDatos():
          nombre.get()
          Apellido.get()
          Direccion.get()
          lista=[]
          lista.append(nombre.get())
          lista.append(Apellido.get())
          lista.append(Direccion.get())
          #listaLabel.set(lista)
          
          datos=messagebox.showinfo("Datos del usuario ",lista)



#-----------------------Crear menu de opciones ---------------------------------
barramenu=Menu(raiz)
raiz.config(menu=barramenu)

archivomenu=Menu(barramenu, tearoff=0)
archivoEdicion=Menu(barramenu, tearoff=0)#El tear siginifca lagriga y tearoff es para quitar como la linea punteada del submenu
archivotools=Menu(barramenu,tearoff=0)
archivoayuda=Menu(barramenu,tearoff=0)

#Para que se muestre el menu
barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Editar", menu=archivoEdicion)
barramenu.add_cascade(label="Herramientas", menu=archivotools)
barramenu.add_cascade(label="Ayuda", menu=archivoayuda)

#-----------------------------------------Sub opciones ó sub menus del menu principal----------------------------------------------------#

#----------Submenus de archivo menu
archivomenu.add_command(label="Nuevo archivo", command=ErrorDesconocido)                                                                                         #
archivomenu.add_command(label="Abrir Archivo", command=Reintentar)                                                                                           #
archivomenu.add_command(label="Guardar")                                                                                                 #
archivomenu.add_command(label="Guardar como")                                                                                            #
archivomenu.add_separator()#Sirve para que aparezca una linea para separar en bloques el submenu de un menu en este caso de archivomenu  #
archivomenu.add_command(label="Cerrar")                                                                                                  #
archivomenu.add_command(label="Exit", command=Salir_Aplicacion)                                                                                                    #

#-----submenus de archivo Edicion -----------------------                                                                                #
archivoEdicion.add_command(label="Cortar", command=Advertencia)                                                                                               #
archivoayuda.add_command(label="Buscar actualizaciones")                                                                                 #
archivoEdicion.add_command(label="Pegar")                                                                                                #


#-------------submenus de archivo ayuda------------------                                                                                #
archivoayuda.add_command(label="Version")                                                                                                #
archivoayuda.add_command(label="Acerca de", command=InfoAdicional)                                                                                              #


#----------------------------------------------------------------------------------------------------------------------------------------

nombre=StringVar()
Apellido=StringVar()
Direccion=StringVar()

nombrelabel=Label( text="Nombre " )#, font=("Itálica"))
nombrelabel.grid(row=0,column=0, pady=4, padx=2)
textname=Entry(raiz, textvariable=nombre )
textname.focus()#Sirve para decir donde quiero que aparezca por defecto el cursor para empezar a escribir
textname.grid(row=0,column=1, padx=8, pady=8)

apellidoLabel=Label(text="Apellido ")
apellidoLabel.grid(row=1,column=0,pady=4, padx=2)
textapellido=Entry(raiz,textvariable=Apellido)
textapellido.grid(row=1,column=1,padx=8, pady=8)

Direccionlabel=Label(text="Direccion")
Direccionlabel.grid(row=2,column=0,pady=4, padx=2)
Direccionrtext=Entry(raiz,textvariable=Direccion)
Direccionrtext.grid(row=2,column=1,padx=8, pady=8)


#----------------------------Boton enviar datos-------------------

# def obtenernombre():
#           nombre.get()
#           Apellido.get()
#           Direccion.get()
#           lista=[]
#           lista.append(nombre.get())
#           lista.append(Apellido.get())
#           lista.append(Direccion.get())
#           #listaLabel.set(lista)
#           Cuadrotexto.insert(END, lista)


Datos=Label(raiz,text="Datos a Mostrar ", width=30)
Datos.config(bg="blue",fg="#ffd700", font="cursiva")
Datos.grid(row=20, column=2,pady=20, columnspan=9)
Cuadrotexto=Text(raiz, width=35, height=8)#Una etiqueta no se puede empaquetar de una vez
Cuadrotexto.grid(row=24, column=2, pady=1, columnspan=22)



Enviarboton=Button(raiz,width=10, height=1, text="Mostrar", command=MostrarDatos)#crea un boton con texto dentro y se le pasa la funcion boton1
Enviarboton.config(bg="#008B8B", fg="#191970", font="cursiva")
Enviarboton.grid(row=26, column=2, pady=30, padx=30, columnspan=3)


#------------------------------Radio buttones--------------------
varOpcion=IntVar()

def imprimirOpcion():
          if varOpcion.get()==1:
                    etiqueta.config(text="Masculino")
          else:
                    etiqueta.config(text="Femenino")


Genero=Label(raiz, text="Seleccione su Genero ")
Genero.grid(row=3, column=0,columnspan=9)

masculino=Radiobutton(raiz,text="Masculino", variable=varOpcion, value=1, command=imprimirOpcion)
masculino.grid(row=4,column=0,sticky="w", padx=10, pady=8)
femenino=Radiobutton(raiz, text="Femenino", variable=varOpcion,value=2,command=imprimirOpcion)
femenino.grid(row=4, column=1,sticky="w",padx=8, pady=8)

etiqueta=Label(raiz,width=20)#Una etiqueta no se puede empaquetar de una vez
etiqueta.grid(row=5, column=0, columnspan=10,padx=20)


#------------------------Checkbox--------------------------


def opcionesDeportes():
          opcionescogida=""
          if Futbol.get()==1:
                    opcionescogida+="  Futbol"
          if Boxeo.get()==1:
                    opcionescogida+="  Boxeo"
          if Tenis.get()==1:
                    opcionescogida+="  Tenis"
          if Pin_Pon.get()==1:
                    opcionescogida+="  Pin Pon"
          Message.config(text=opcionescogida)#Se le pasa al label la opcion escogida

Futbol=IntVar()
Boxeo=IntVar()
Tenis=IntVar()
Pin_Pon=IntVar()

texto1=Label(raiz, text="Checkbuttons")
texto1.grid(row=6,column=0, pady=6)

#Con la opcion variable=Futbol o cualquier otra opcion se le esta pasando al checkbox la variable con valor entero ya sea cero o uno
#el metodo command se le pasa la funcion al boton en este caso al checkbox 
Button1=Checkbutton(raiz, text="Futbol", variable=Futbol, onvalue=1, offvalue=0, command=opcionesDeportes, width=10)
Button1.grid(row=7,column=0, padx=4,pady=4)
Button2=Checkbutton(raiz, text="Boxeo", variable=Boxeo, onvalue=1, offvalue=0, command=opcionesDeportes, width=10)
Button2.grid(row=7,column=1,padx=4, pady=4)
Button3=Checkbutton(raiz, text="Tenis", variable=Tenis, onvalue=1, offvalue=0, command=opcionesDeportes, width=10)
Button3.grid(row=7,column=2, padx=1,pady=4)
Button4=Checkbutton(raiz, text="Pin Pon", variable=Pin_Pon, onvalue=1, offvalue=0, command=opcionesDeportes, width=10)
Button4.grid(row=7,column=3, padx=4,pady=4)
#La opcion onvalue=1 le dice al checkbox que esta marcada, y la opcion offvalue=0 le dice que no esta seleccionado, y cuando llega al if
#Hace la validacion si el checkbox esta seleccionado

Message=Label(raiz,width=50)#Label para mostrar lo que el usuario ha seleccionado
Message.grid(row=11, column=0, padx=10, columnspan=10)


raiz.mainloop()
