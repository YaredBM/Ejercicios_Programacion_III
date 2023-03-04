#Elaborar un programa que genere 10 caracteres de manera aleatorio e 
#imprima cuantas veces se generaron vocales.
import random
vocan=0
for x in range(10):
    r=random.randint(65,122)
    l=chr(r)
    print(l)
    if l in "AEIOUaeiou":
        vocan+=1
print("Se generaron ",vocan," vocales.")