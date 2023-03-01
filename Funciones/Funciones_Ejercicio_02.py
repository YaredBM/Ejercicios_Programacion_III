#EJERCICIO 02
#Pide una cadena y un caracter por teclado y muestra cuantas veces aparece
#el caracter en la cadena
frase=str(input("Ingrese una frase: "))
caracter=str(input("Ingrese un caracter: "))
con=frase.count(caracter)
print("El caracter",caracter,"aparece",con,"veces en frase.")


#Otra forma
co=0
for x in frase:
    if x==caracter:
        co+=1
print("El caracter",caracter,"aparece",co,"veces en frase.")

#Otra forma
co=0
for x in range(len(frase)):
    if x==caracter:
        co+=1
print("El caracter",caracter,"aparece",co,"veces en frase.")
