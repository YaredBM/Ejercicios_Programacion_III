#EJERCICIO 16
#Leer una cadena de caracteres y dar como opciones:}
#-Imprimir la cadena solo vocales
#-Imprimir la cadena solo consonantes
frase=input("Ingrese una cadena de caracteres: ").lower()
op=input("Escriba vocales o consonantes: ")
if op=="consonantes":
    nuevafrase = frase
    vocales = ("aeiou")
    for x in frase:
        if x in vocales:
            nuevafrase = nuevafrase.replace(x,"")
    print(nuevafrase)
elif op=="vocales":
    nuevafrase = frase
    conso = ("bcdfghjklmnpqrstvwxyz")
    for x in frase:
        if x in conso:
            nuevafrase = nuevafrase.replace(x,"")
    print(nuevafrase)
else:
    print("Error")
