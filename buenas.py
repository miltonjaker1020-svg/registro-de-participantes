cantidad=int(input("ingresar la cantidad de personas que se desean registrar"))
lista=[]
def aprob():
    if edad>=15 and conocimiento.lower()=="si":
     print("puede participar en el taller")
    else:
       print("no puede participar")


for i in range(cantidad):
    nombre=input("favor ingresar su nombre:  ")
    edad=int(input("favor agregar su edad:  "))
    if edad<=0:
        print("se a detectado un error en la edad")
        print("la edad no puede ser igual o menor a 0")
        continue
    
    conocimiento=input("¿tiene el usuario conocimiento basico de computo")
    resultado = aprob(edad, conocimiento)
    
    dicc={"nombre":nombre,
          "edad":edad,
          "aprobado":resultado}
    lista.append(dicc)
print(f"\n, el historial es el siguiente")
for i in lista:
   print(f"--{i["nombre"]}---{i["edad"]}--{i["aprobado"]}")
