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
        boton.pack(padx="20", pady="30")
        boton.place(x=270, y=366)

        imagen = PhotoImage(file="")
        Label(self.master, image=imagen, bd=0).pack()

        '''cuadroTexto = Entry(tab_datos)
        cuadroTexto.place(x=100, y=150)'''

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("block.Horizontal.TProgressbar", background="green")
        bar = Progressbar(tab_datos, length=200, style="block.Horizontal.TProgressbar")
        bar["value"] = 100
        bar.place(x=60, y=200)

        tab_ingreso = ttk.Frame(contenedor)
        contenedor.add(tab_ingreso, text='Ingreso')

        '''lbl_ingreso = tk.Label(tab_ingreso, text='Ingreso')
        lbl_ingreso.grid(row=0, column=0)'''

        '''txt_nombre = tk.Entry(tab_ingreso)
        txt_nombre.grid(row=1, column=0)'''


        monto = 0
        total = "$" + str(monto)
        texto_pantalla = StringVar()

        pantalla = Entry(tab_datos, textvariable="texto_pantalla", bg="grey", fg="black")
        pantalla.insert(0, total)
        pantalla.place(x=100, y=100)

        color_boton = "grey80"
        ancho_boton = 6
        alto_boton = 3

        operador0 = ""
        operador1 = ""

        texto_pantalla0 = StringVar()
        texto_pantalla1 = StringVar()

        def clear0():
            global operador0
            operador0 = ""
            texto_pantalla0.set("0")

        def click0(b):
            global operador0
            operador0 += str(b)
            texto_pantalla0.set(operador0)

        def resultado0():
            global operador0
            try:
                r = str(eval(operador0))
            except:
                r = "ERROR"
            texto_pantalla0.set(r)

        def clear1():
            global operador1
            operador1 = ""
            texto_pantalla1.set("0")

        def click1(b):
            global operador1
            operador1 += str(b)
            texto_pantalla1.set(operador1)

        def resultado1():
            global operador1
            try:
                r = str(eval(operador1))
            except:
                r = "ERROR"
            texto_pantalla1.set(r)

        clear0()
        clear1()
#ingreso

        Boton0 = Button(tab_ingreso, text="0", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(0)).grid(row=5, column=0, pady=10)
        Boton1 = Button(tab_ingreso, text="1", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(1)).grid(row=4, column=0, pady=10)
        Boton2 = Button(tab_ingreso, text="2", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(2)).grid(row=4, column=1, pady=10)
        Boton3 = Button(tab_ingreso, text="3", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(3)).grid(row=4, column=2, pady=10)
        Boton4 = Button(tab_ingreso, text="4", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(4)).grid(row=3, column=0, pady=10)
        Boton5 = Button(tab_ingreso, text="5", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(5)).grid(row=3, column=1, pady=10)
        Boton6 = Button(tab_ingreso, text="6", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(6)).grid(row=3, column=2, pady=10)
        Boton7 = Button(tab_ingreso, text="7", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(7)).grid(row=2, column=0, pady=10)
        Boton8 = Button(tab_ingreso, text="8", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(8)).grid(row=2, column=1, pady=10)
        Boton9 = Button(tab_ingreso, text="9", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click0(9)).grid(row=2, column=2, pady=10)
        '''BotonSuma = Button(tab_ingreso, text="+", bg=color_boton, width=ancho_boton,
                           height=alto_boton, command=lambda: click("+")).grid(row=6, column=0, pady=10)
        BotonResta = Button(tab_ingreso, text="-", bg=color_boton, width=ancho_boton,
                            height=alto_boton, command=lambda: click("-")).grid(row=6, column=1, pady=10)'''
        BotonClear = Button(tab_ingreso, text="Clear", bg=color_boton, width=5,
                            height=1, command=clear0).grid(row=1, column=0, pady=10)
        BotonIgual = Button(tab_ingreso, text="Enter", bg=color_boton, width=ancho_boton,
                            height=alto_boton, command=resultado0).grid(row=5, column=2, pady=10)

        Pantalla = Entry(tab_ingreso, font=("arial", 20, "bold"), width=20,
                         borderwidth=10, background="green", textvariable=texto_pantalla0)
        Pantalla.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

#egreso

        tab_egreso = ttk.Frame(contenedor)
        contenedor.add(tab_egreso, text='Egreso')

        '''lbl_egreso = tk.Label(tab_egreso, text='Egreso')
        lbl_egreso.grid(row=0, column=0)

        txt_nombre = tk.Entry(tab_egreso)
        txt_nombre.grid(row=1, column=0)'''

        Boton0 = Button(tab_egreso, text="0", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(0)).grid(row=5, column=0, pady=10)
        Boton1 = Button(tab_egreso, text="1", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(1)).grid(row=4, column=0, pady=10)
        Boton2 = Button(tab_egreso, text="2", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(2)).grid(row=4, column=1, pady=10)
        Boton3 = Button(tab_egreso, text="3", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(3)).grid(row=4, column=2, pady=10)
        Boton4 = Button(tab_egreso, text="4", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(4)).grid(row=3, column=0, pady=10)
        Boton5 = Button(tab_egreso, text="5", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(5)).grid(row=3, column=1, pady=10)
        Boton6 = Button(tab_egreso, text="6", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(6)).grid(row=3, column=2, pady=10)
        Boton7 = Button(tab_egreso, text="7", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(7)).grid(row=2, column=0, pady=10)
        Boton8 = Button(tab_egreso, text="8", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(8)).grid(row=2, column=1, pady=10)
        Boton9 = Button(tab_egreso, text="9", bg=color_boton, width=ancho_boton,
                        height=alto_boton, command=lambda: click1(9)).grid(row=2, column=2, pady=10)
        '''BotonSuma = Button(tab_egreso, text="+", bg=color_boton, width=ancho_boton,
                           height=alto_boton, command=lambda: click1("+")).grid(row=6, column=0, pady=10)
        BotonResta = Button(tab_egreso, text="-", bg=color_boton, width=ancho_boton,
                            height=alto_boton, command=lambda: click1("-")).grid(row=6, column=1, pady=10)'''
        BotonClear = Button(tab_egreso, text="Clear", bg=color_boton, width=5,
                            height=1, command=clear1).grid(row=1, column=0, pady=10)
        BotonIgual = Button(tab_egreso, text="=", bg=color_boton, width=ancho_boton,
                            height=alto_boton, command=resultado1).grid(row=5, column=2, pady=10)

        Pantalla = Entry(tab_egreso, font=("arial", 20, "bold"), width=20,
                         borderwidth=10, background="red", textvariable=texto_pantalla1)
        Pantalla.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


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