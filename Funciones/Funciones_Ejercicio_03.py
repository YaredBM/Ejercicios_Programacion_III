#EJERCICIO 03
#Susponiendo que hemos introducido una cadena por teclado que representa una frase (palabras
#separadas por espacios) realice un programa que cuente cuantas las letras en frase
frase=input("Ingrese una frase: ")
let=0

for x in range(len(frase)):
    if frase[x]==" ":
        let-=1
    let+=1
print("La cantidad de letras en frase: ",let)

##Contar palabras en frase
##frase=input("Ingrese una frase: ")
##esp=frase.count(" ")
##print("Hay ",(esp+1),"palabras en la frase. ")
##
##Otra forma de resolver
##frase=input("Ingrese una frase: ")
##es=0
##for x in frase:
##    if x==" ":
##        es+=1
##print("Hay ",(es+1),"palabras en la frase. ")
