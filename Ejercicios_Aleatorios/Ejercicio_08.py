#Un programa que pida una frase y de manera aleatoria, seleccione
#un caracter, obtenga su valor numérico e imprima la nueva cadena.
import random
frase=input("Ingrese una frase: ")

for x in range(len(frase)):
    let1=random.choice(frase)
    let2=str(ord(let1))
    frasen=frase.replace(let1,let2)
print(frasen)

#Otra forma de resolverlo
import random
frase = input("Ingresa una frase: ")
cara = random.choice(frase)
valorlet = ord(cara)
posicion = frase.find(cara)
nueva_frase = (frase[:posicion] + str(valorlet) + frase[posicion:])
print("La nueva frase es:", nueva_frase)