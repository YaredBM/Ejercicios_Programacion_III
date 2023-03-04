#Considerar que un jugador lanza 2 dados, gana si obtiene 11 puntos. Generar el proceso de lanzamiento de los dados
#hasta que el jugador gana. Mostrar por pantalla el número de lanzamientos realizados por el jugador.
import random
x=d1=d2=suma=0
while x!=11:
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    x=d1+d2
    suma+=1
    print(d1,d2)
print("Gana con: ",suma," lanzamientos.")