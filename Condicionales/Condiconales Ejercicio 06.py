#Elaborar un programa que pida un número entero comprendido entre 10 y 99,
#si el primer dígito es menor que el segundo, sumarlos, signo, restarlos.
#Mostrar la operación obtenida.

num=int(input("Ingrese un número entre 10 y 99: "))
d2=num%10
num=num//10
d1=num%10
if d1<d2:
    r=d1+d2
else:
    r=d1-d2
print("El resultado es ",r)




















    
