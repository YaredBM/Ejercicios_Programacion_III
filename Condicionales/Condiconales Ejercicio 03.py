# La tienda de variedades maneja la siguiente política de descuentos:
#si lleva menos de 10 artículos no tiene descuentos, si lleva entre 10 y 20 artículos se le dará un 10% de descuento,
#si lleva entre 21 y 30 artículos tiene un 20% de descuento
#y si lleva más de 30 artículos tiene el 30% de descuento

art=int(input("Ingrese el precio del producto: "))
cant=int(input("Ingrese la cantidad del producto: "))
sub=art*cant
if cant<10:
    desc=0
    total=sub-desc
    print("El total es de",total,"sin descuento.")
elif cant>=10 and cant<=20:
    desc=sub*0.10
    total=sub-desc
    print("El total es de",total,"con 10% de descuento.")
elif cant>=21 and cant<=30:
    desc=sub*0.20
    total=sub-desc
    print("El total es de",total,"con 20% de descuento")
elif cant>30:
    desc=sub*0.30
    total=sub-desc
    print("El total es de",total,"con 30% de descuento.")
