ladoA = float(input("Ingrese el primer lado: "))
ladoB = float(input("Ingrese el segundo lado: "))
precio = float(input("Ingrese el precio del alambre: "))

def calcularCosto(ladoUno, ladoDos, precioAlambre):
    perimetro = (ladoUno * 2 ) + (ladoDos * 2)
    return perimetro * precioAlambre

print(calcularCosto(ladoA, ladoB, precio))