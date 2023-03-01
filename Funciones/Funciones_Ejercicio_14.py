#EJERCICIO 14
#Escribir un programa que pregunte por consola por los productos
#de una cesta de compra, separados por comas y muestre por pantalla
#cada uno de los productos en una linea diferente
prod = input("Ingresa los productos separados por coma: ")
prodlist = prod.split(",")
for prod in prodlist:
    print(prod.strip())
