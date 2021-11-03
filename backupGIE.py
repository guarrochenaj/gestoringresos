from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora Casio FX-9750")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.configure(background="gray42")

color_boton = "gray99"
ancho_boton = 10
alto_boton = 3
operador = ""
texto_pantalla = StringVar()


def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")


def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)


def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR"
    texto_pantalla.set(r)


clear()
# BOTONES DE LA PRIMERA FILA
Boton0 = Button(tab_ingreso, text="0", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(0)).grid(row=5, column=0, pady=10)
Boton1 = Button(tab_ingreso, text="1", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(1)).grid(row=4, column=0, pady=10)
Boton2 = Button(tab_ingreso, text="2", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(2)).grid(row=4, column=1, pady=10)
Boton3 = Button(tab_ingreso, text="3", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(3)).grid(row=4, column=2, pady=10)
# BOTONES DE LA SEGUNDA FILA
Boton4 = Button(tab_ingreso, text="4", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(4)).grid(row=3, column=0, pady=10)
Boton5 = Button(tab_ingreso, text="5", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(5)).grid(row=3, column=1, pady=10)
Boton6 = Button(tab_ingreso, text="6", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(6)).grid(row=3, column=2, pady=10)
Boton7 = Button(tab_ingreso, text="7", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(7)).grid(row=2, column=0, pady=10)
# BOTONES DE LA TERCERA FILA
Boton8 = Button(tab_ingreso, text="8", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(8)).grid(row=2, column=1, pady=10)
Boton9 = Button(tab_ingreso, text="9", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(9)).grid(row=2, column=2, pady=10)
# BOTONES DE LA CUARTA FILA
BotonSuma = Button(tab_ingreso, text="+", bg=color_boton, width=ancho_boton,
                   height=alto_boton, command=lambda: click("+")).grid(row=6, column=0, pady=10)
BotonResta = Button(tab_ingreso, text="-", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=lambda: click("-")).grid(row=6, column=1, pady=10)
# BOTONES DE LA QUINTA FILA
BotonClear = Button(tab_ingreso, text="Clear", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=clear).grid(row=1, column=0, pady=10)
BotonIgual = Button(tab_ingreso, text="=", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=resultado).grid(row=5, column=1, pady=10)

Pantalla = Entry(tab_ingreso, font=("arial", 20, "bold"), width=22,
                 borderwidth=10, background="CadetBlue1", textvariable=texto_pantalla)
Pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

ventana.mainloop()