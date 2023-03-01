#EJERICIO 04
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que
#muestre las iniciales en mayusculas.
nom=input("Ingrese nombre y apellido: ").lower()
nom1=nom.title()
print(nom1)

#Otra forma de resolver
##nom=input("Ingrese nombre y apellido: ").lower()
##cade=nom[0].upper()
##x=1
##while x<len(nom):
##    cade+=nom[0]
##    if nom[x]==" ":
##        cade+=nom[x+1].upper()
##        x+=1
##    x+=1
##print(cade)
