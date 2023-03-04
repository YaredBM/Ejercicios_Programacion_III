# Elaborar un programa que genere 100 elementos, comprendidos entre 10 y 200, muestre o imprima
# el cuadrado de los pies y el cubo de los impares.
import random
for x in range(100):
    n=random.randint(10,200)
    if n%10==0:
        print("El cuadrado de: ",n," es de ",(n**2))
    else:
        print("El cubo de: ",n," es de ",(n**3))