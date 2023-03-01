##Elabore un programa que sume los números comprendidos entre
##1 y Y. Validar que Y sea mayor que 1.
y=int(input("Ingrese un número: "))
suma=0
x=1
if y>1:
    while y>=x:
        suma+=x
        x+=1
    print("La suma de los números entre 1 y",y," es: ",suma)
else:
    print("Error")
