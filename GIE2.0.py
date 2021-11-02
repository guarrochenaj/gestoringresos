import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import messagebox


class Aplicacion(tk.Frame):
    ventana = 0
    posx_y = 0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Gestor de Ingresos y Egresos")
        self.master.config(bg="white")
        self.master.geometry("325x450")
        self.master.resizable(0, 0)
        self.master.iconbitmap("D:/Descargas/viking.ico")
        self.inicializar_gui()

    def inicializar_gui(self):
        contenedor = ttk.Notebook(self.master)
        tab_datos = ttk.Frame(contenedor)
        contenedor.add(tab_datos, text='Informacion')
        lbl_python = tk.Label(tab_datos)
        lbl_python.pack()
        lbl_python.config(bg="grey")
        lbl_python.config(width="200", height="300")
        lbl_python.pack(ipadx="20", ipady="30")
        lbl_python.pack(padx="10", pady="20")
        lbl_python.config(bd=5)
        lbl_python.config(relief="groove")
        lbl_python.config(cursor="hand2")

        boton = Button(tab_datos, text="EXIT", command=self.salir)
        boton.config(bg="red")
        boton.pack(ipadx="20", ipady="30")
        boton.pack(padx="10", pady="20")
        boton.place(x=270, y=370)

        numeroPantalla = StringVar()

        pantalla = Entry(tab_datos, textvariable=numeroPantalla, bg="grey", fg="black")
        pantalla.place(x=100, y=100)

        cuadroTexto = Entry(tab_datos)
        cuadroTexto.place(x=100, y=150)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("block.Horizontal.TProgressbar", background="green")
        bar = Progressbar(tab_datos, length=200, style="block.Horizontal.TProgressbar")
        bar["value"] = 95
        bar.place(x=60, y=200)

        tab_ingreso = ttk.Frame(contenedor)
        contenedor.add(tab_ingreso, text='Ingreso')

        lbl_ingreso = tk.Label(tab_ingreso, text='Ingreso')
        lbl_ingreso.grid(row=0, column=0)

        txt_nombre = tk.Entry(tab_ingreso)
        txt_nombre.grid(row=1, column=0)

        tab_egreso = ttk.Frame(contenedor)
        contenedor.add(tab_egreso, text='Egreso')

        lbl_egreso = tk.Label(tab_egreso, text='Egreso')
        lbl_egreso.grid(row=0, column=0)

        txt_nombre = tk.Entry(tab_egreso)
        txt_nombre.grid(row=1, column=0)

        contenedor.pack(expand=1, fill='both')

    def salir(self):
        self.master.destroy()

    def salirApp(self):
        valor = messagebox.askquestion("Gestor de Ingresos y Egresos", "Desea salir de la aplicacion")
        if valor == "True":
            self.master.destroy()

    '''def abrir(self):

     self.dialogo=Toplevel()

     Aplicacion.ventana=1

     Aplicacion.posx_y += 0
     tamypos = '300x200+'+str(Aplicacion.posx_y)+ \
     '+'+ str(Aplicacion.posx_y)
     self.dialogo.geometry(tamypos)
     self.dialogo.resizable(1,1)

     ident = self.dialogo.winfo_id()

     titulo = str(Aplicacion.ventana) + " solicitud: " + str(ident)
     self.dialogo.title(titulo)

     boton = Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
     boton.pack(side=BOTTOM, padx=20, pady=20)
     boton.config(bg="red")

     self.dialogo.grab_set()
     self.master.wait_window(self.dialogo)'''


def main():
    app = tk.Tk()
    app.geometry('325x450')
    app.title('Gestor de Ingresos y Egresos')

    ventana = Aplicacion(app)
    ventana.mainloop()


if __name__ == "__main__":
    main()