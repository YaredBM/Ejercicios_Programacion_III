#Un supermercado ha puesto en oferta la venta al por mayor de
#cierto producto ofreciendo un descuento del 15% por la compra de más
#de 3 docenas y 10% en caso contrario. Además, por la compra de más de
#3 docenas se obsequia una unidad del producto por docena en exceso sobre 3.}
#Diseñe un programa que Determine el monto de la compra con el monto de descuento,
#el monto a pagar y el número de unidades de obsequio por la compra de cierta
#cantidad de docenas del producto

vdesc=pre=mdc=uni=tp=0
pre=int(input("Ingrese el precio de docenas: "))
doc=int(input("Ingrese el numero de docenas: "))
if doc>3:
    vdesc=0.15
    uni=doc-3
else:
    vdesc=0.10
mdc=pre*doc
de=mdc*vdesc
tp=mdc-de
print("Monto de compra: L", mdc)
print("Monto de descuento: L", de)
print("Monto a pagar: L", tp)
print("Unidades de obsequio: ", uni)





















    
