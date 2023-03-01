#EJERCICIO 07
#Pida una cadena de caracteres por teclado, sustituye la aparicion
#del primer caractere en la cadena por el segundo caracter
cade=str(input("Ingrese una cadena: "))
car1=str(input("Ingrese caracter 01: "))
car2=str(input("Ingrese caracter 02: "))

for x in range(len(cade)):
    cade1=cade.replace(car1,car2)
print(cade1)
