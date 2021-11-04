from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


class Aplicacion():

    ventana = 0
    posx_y = 0

    def __init__(self):
     self.raiz = Tk()

     self.raiz.title("Gestor de Ingresos y Egresos")
     self.raiz.config(bg="white")
     self.raiz.geometry("325x450")
     self.raiz.resizable(0, 0)
     self.raiz.iconbitmap("D:/Descargas/viking.ico")

     miFrame = Frame()
     miFrame.pack()
     '''miFrame.config(bg="grey")'''
     miFrame.config(width="200", height="300")
     miFrame.pack(ipadx="20", ipady="30")
     miFrame.pack(padx="10", pady="20")
     miFrame.config(bd=5)
     miFrame.config(relief="groove")
     miFrame.config(cursor="hand2")

     '''visualizaremos la cantidad de dinero en la cuenta'''
     operacion=""
     reset_pantalla=False
     resultado=0

     imagen = PhotoImage(file="D:/caratula/c94e011def3a342e9d481a286f41ef91.png_wh860.png")
     Label(self.raiz, image=imagen, bd=0).pack()

     numeroPantalla=StringVar()

     pantalla=Entry(miFrame, textvariable=numeroPantalla, bg="grey", fg="black")
     pantalla.place(x=50, y=80)
     '''miLabel = Label(miFrame, text="$xxx.xxx", bg="grey", fg="black", font=("Calibri", 30))'''

     '''es solamente decorativo, ya que se planea reemplazar por una barra que marque el estado de la cuenta'''
     cuadroTexto = Entry(miFrame)
     cuadroTexto.place(x=50, y=150)

     boton = Button(self.raiz, text="+", command=self.abrir)
     boton.pack(side=RIGHT, padx=10)
     boton.config(bg="green")
     style = ttk.Style()
     style.theme_use("default")
     style.configure("block.Horizontal.TProgressbar", background="green")
     bar = Progressbar(self.raiz, length=200, style="block.Horizontal.TProgressbar")
     bar["value"] = 95
     bar.place(x=60, y=200)

     '''tendremos acceso a futuras opc extra como: estadisticas, egresos, ingresos, salir, entre otros'''
     barraMenu = Menu(self.raiz)
     self.raiz.config(menu=barraMenu, width=100, height=200)

     archivoMenu = Menu(barraMenu, tearoff=0)
     archivoMenu.add_command(label="opc1")
     archivoMenu.add_command(label="opc2")
     archivoMenu.add_command(label="opc3")
     archivoMenu.add_separator()
     archivoMenu.add_command(label="opc1")
     archivoMenu.add_command(label="opc2")

     archivoEdicion = Menu(barraMenu, tearoff=0)
     archivoEdicion.add_command(label="opc1")
     archivoEdicion.add_command(label="opc2")
     archivoEdicion.add_command(label="opc3")

     archivoHerramientas = Menu(barraMenu, tearoff=0)
     archivoHerramientas.add_command(label="opc1")
     archivoHerramientas.add_command(label="opc2")

     archivoAyuda = Menu(barraMenu, tearoff=0)
     archivoAyuda.add_command(label="opc1")
     archivoAyuda.add_command(label="Salir", command=self.salir)

     barraMenu.add_cascade(label="menu1", menu=archivoMenu)
     barraMenu.add_cascade(label="menu2", menu=archivoEdicion)
     barraMenu.add_cascade(label="menu3", menu=archivoHerramientas)
     barraMenu.add_cascade(label="menu4", menu=archivoAyuda)

     self.raiz.mainloop()

    def salir(self):
     self.raiz.destroy()

    def abrir(self):

     self.dialogo=Toplevel()

     Aplicacion.ventana=1

     Aplicacion.posx_y += 0
     tamypos = '300x200+'+str(Aplicacion.posx_y)+ \
     '+'+ str(Aplicacion.posx_y)
     self.dialogo.geometry(tamypos)
     self.dialogo.resizable(0,0)

     ident = self.dialogo.winfo_id()

     titulo = str(Aplicacion.ventana) + " solicitud: " + str(ident)
     self.dialogo.title(titulo)

     '''self.miLabel = Label(self.miFrame, text="$xxx.xxx", bg="grey", fg="black", font=("Calibri", 30))'''

     boton = Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
     boton.pack(side=BOTTOM, padx=20, pady=20)
     boton.config(bg="red")

     self.dialogo.grab_set()
     self.raiz.wait_window(self.dialogo)


def main():
 mi_app = Aplicacion()
 return (0)


if __name__ == '__main__':
 main()
