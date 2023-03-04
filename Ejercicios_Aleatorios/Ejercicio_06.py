import random
vocan=0
for x in range(10):
    r=random.randint(67,122)
    l=chr(r)
    print(l)
    if l in "AEIOUaeiou":
        vocan+=1
print("El numero de veces que se generaron vocales es de :",vocan)
