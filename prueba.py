import random
id=[]
listaids=[]
cant=int(input("Ingrese la cantidad de ids para generar"))
cont=0

while cont < cant:
    for i in range(10):
        digito= random.randint(1,999)
        id.append(digito)
    cont+=1
    listaids.append(id)

print(id)