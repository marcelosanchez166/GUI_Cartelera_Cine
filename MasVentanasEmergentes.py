from tkinter import *

"""Las ventanas emegentes no vienen con la biblioteca de tkinter hay que importarlas por aparte"""
from tkinter import messagebox


from tkinter import colorchooser
from tkinter import filedialog

raiz = Tk()
raiz.title("Datos del Usuario ")
raiz.geometry("720x650")
raiz.config(background="gray")


def Abrir():
    # el parametro askopenfilename devuelve la ruta del archivo cuando le damos abrir
    valor = filedialog.askopenfilename(title="Abrir archivo ")
    print(valor)


# --------------------------------Funcion para guardar archivo-------------------
def guardar():
    # El parametro filetypes sirve para decir que tipo de ficheros quiero que muestre se le pasan dos valores la descripcion y extencion
    # El Parametro asksaveasfilename devuelve la ruta donde se guardo el archivo
    valor2 = filedialog.asksaveasfilename(title="Guardar Archivo ", initialdir="D:", filetypes=(("Ficheros de excel ", "*.xlsx"),
    ("ficheros de texto", "*.txt"), ("Todos los ficheros ", "*.*")))
    print(valor2)


# ------------Funcion para guardar un archivo como---------------
def guardar_como():
    # El initial le dice la ruta que estableci para que se guarde por defecto los archivos
    # El Parametro asksaveasfile devuelve la ruta donde se guardo el archivo
    valor3 = filedialog.asksaveasfile(
        title="Guardar Archivo ", initialdir="D:\Docker BO")
    print(valor3)


# -----------------------Crear menu de opciones ---------------------------------
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

archivomenu = Menu(barramenu, tearoff=0)
# El tear siginifca lagriga y tearoff es para quitar como la linea punteada del submenu
archivoEdicion = Menu(barramenu, tearoff=0)
archivotools = Menu(barramenu, tearoff=0)
archivoayuda = Menu(barramenu, tearoff=0)

# Para que se muestre el menu
barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Editar", menu=archivoEdicion)
barramenu.add_cascade(label="Herramientas", menu=archivotools)
barramenu.add_cascade(label="Ayuda", menu=archivoayuda)

#-----------------------------------------Sub opciones ó sub menus del menu principal----------------------------------------------------#

# ----------Submenus de archivo menu
#
archivomenu.add_command(label="Nuevo archivo")
#
archivomenu.add_command(label="Abrir Archivo", command=Abrir)
#
archivomenu.add_command(label="Guardar", command=guardar)
#
archivomenu.add_command(label="Guardar como", command=guardar_como)
# Sirve para que aparezca una linea para separar en bloques el submenu de un menu en este caso de archivomenu  #
archivomenu.add_separator()
#
archivomenu.add_command(label="Cerrar")
#
archivomenu.add_command(label="Exit")

#-----submenus de archivo Edicion -----------------------                                                                                #
#
archivoEdicion.add_command(label="Cortar")
#
archivoayuda.add_command(label="Buscar actualizaciones")
#
archivoEdicion.add_command(label="Pegar")


#-------------submenus de archivo ayuda------------------                                                                                #
#
archivoayuda.add_command(label="Version")
#
archivoayuda.add_command(label="Acerca de")


raiz.mainloop()
