#EJERCICIO 08
#Introducir una cadena de caracteres e indicar si es un palindromo. Una palabra que se escribe
#se lee igual al derecho y al revés
cade=str(input("Ingrese una cadena: "))
cade1=cade[::-1]
if cade==cade1:
    print("Es un palindromo")
else:
    print("No es un palindromo")



























