#Se ingresa un número por teclado se ingresa un número por teclado entre –99 y 99,
#mostrar un mensaje indicando si el número es negativo o si es positivo
#y tiene uno o 2 dígitos.

num=int(input("Ingrese el numero entre -99 y 99: "))
if num>=-99 and num<=-1:
    cant=(len(str(abs(num))))
    print("Tu número es negativo y tiene",str(cant),"dígitos")
elif num>=1 and num<=99:
    cant=(len(str(abs(num))))
    print("Tu número es positivo y tiene",str(cant),"dígitos")
elif num==0:
    print("Es neutral")
