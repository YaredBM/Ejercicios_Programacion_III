#Escribir un programa que solicite el ingreso de notas de 10 alumnos y nos informen
##cuantos tienen arriba de 70 y por debajo de 70.
x=0
cant1=0
cant2=0
nota=0
while x<10:
    nota=int(input("ingrese nota: "))
    x+=1
    if nota>=70:
        cant1=cant1+1
    else:
        cant2=cant2+1
print("Notas mayores 70:",cant1);
print("Notas menores a 70:",cant2)
