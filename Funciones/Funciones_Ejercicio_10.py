#EJERCICIO 10
##Escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre
##por pantalla el nombre completo del usuario tres veces:
##1-Una con todas las letras minusculas
##2-Otra con la inicial,la segunda y
##3-Otra que muestre opcion en mayusculas solo vocales o consonantes

nom=str(input("Ingrese nombre completo: ")).lower()

#IMPRESIÓN 01
print(nom)

#IMPRESIÓN 02
nuevo=" "
if len(nom) >= 2:
    nuevo+= nom[:2].upper()
else:
    nuevo += nom.upper()
if len(nom) > 2:
    nuevo += nom[2:]
if len(nom) >= 4:
    nuevo = nuevo[:-2] + nuevo[-2:].upper()
print("Su nuevo nombre es:", nuevo)

#IMPRESIÓN 03
op = input("Ingrese 'vocales' o 'consonantes': ")

if op == "vocales":
    nuevonom = ""
    for letra in nom:
        if letra in "AEIOUaeiou":
            nuevonom += letra.upper()
        else:
            nuevonom += letra
    print("Vocales en mayúsculas:", nuevonom)
elif op == "consonantes":
    nuevonom= ""
    for letra in nom:
        if letra not in "AEIOUaeiou" and letra.isalpha():
            nuevonom += letra.upper()
        else:
            nuevonom += letra
    print("Consonantes en mayúsculas:", nuevonom)
else:
    print("Opción no válida.")
