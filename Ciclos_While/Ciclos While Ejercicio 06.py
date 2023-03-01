#Realiza un programa que pida números mientras no se ingrese uno negativo. Al final
#se debe mostrar la suma de los números positivos ingresados y la cantidad total
#de ingresos.
x=0
suma=0
cant=0
num=0
while x>=0:
    num=int(input("Ingrese un número: "))
    x+=1
    if num>=0:
        suma+=num
        cant+=1
    else:
        print("Has ingresado un número negativo.")
        break
print("La suma total es de: ",suma);
print("La cantidad total ingresada es de: ",cant)
