'''lista1=[10,5,3]
lista2=[1.78,2.66,1.55,89,4]
lista3=["lunes","martes","miercoles","jueves"]
lista4=["juan",45,1.92]
print(len(lista3))
print(lista3[:])
print(lista3[2])
print(lista3[-2])
print(lista3[0:2])
print(lista3[:2])
print(lista3[2:])


lista=["Ana","Luis","Martin","Lucia","Adrian"]
print(lista.index("Martin"))
print("Jorge" in lista)
print("Ana" in lista)

lista=[10,20,30]
lista.append(100)
print(lista[:])

lista=[1,2,3,4]
for x in range(5):
    valor=int(input("ingrese un valor entero:"))
    lista.extend([valor])

print(lista)

lista1=[10,20,30]
lista2=["ana","luis","martin","lucia","adrian"]
lista3=lista1 + lista2

print(lista3)

tupla1=("jose",[2],)
tupla1[1].append((3))
print(tupla1)


nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

personas=int(input("ingrese comensales: "))

if personas > 300:
    costo=75
elif personas > 200:
    costo=85
else:
    costo=95
total=costo*personas
print("el costo por plato sera ", costo)
print("el costo sera", total)

for i in ("uno","dos"):
    print(i)
for i in ("unodos"):
    print(i)

def calcu_interes (c,r,t):
    interes=(c*r*t)/(100*365)
    comision= interes*0.03
    total=interes+comision


capital=float(input("ingrese capital:"))
tasa=float(input("ingrese tasa:"))
plazo=float(input("ingrese plazo:"))

calcu_interes(capital,tasa,plazo)'''

listadeinvitados = "franco,andres,julio,gregorio,jorge"
coma = ","
separado = listadeinvitados.split(coma)
print("Separado por espacios es:", separado)

