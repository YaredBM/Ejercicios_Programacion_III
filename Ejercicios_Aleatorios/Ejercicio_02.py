#Elaborar un programa que permita listar 6 números aleatorios entre límite a y límite b
import random
a=int(input("Ingrese valor para a: "))
b=int(input("Ingrese valor para b: "))
if a<b:
    for x in range(5):
        print(random.randint(a,b))
else:
    print("Error de valores agregados.")


#Reoecticion de ciclo si a es mayor a b
import random
while True:
    a=int(input("Ingrese valor para a: "))
    b=int(input("Ingrese valor para b: "))
    if a<b:
        for x in range(6):
            print(random.randint(a,b))
            
    else:
        print("Error de valores agregados.")
        #continue
    r=int(input("¿Desea continuar? 1.Si 2.No: "))
    if r==2:
        break
