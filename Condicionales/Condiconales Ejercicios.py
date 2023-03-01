#EJERCICIO 1
##num=int(input("Ingrese el numero entre -99 y 99: "))
##if num>=-99 and num<=-1:
##    cant=(len(str(num)))
##    print("Tu número es negativo y tiene",str(cant),"dígitos")
##elif num>=1 and num<=99:
##    cant=(len(str(num)))
##    print("Tu número es positivo y tiene",str(cant),"dígitos")
##elif num==0:
##    print("Es neutral")



#EJERCICIO 2
##nota1=int(input("Ingrese la nota 1: "))
##nota2=int(input("Ingrese la nota 2: "))
##nota3=int(input("Ingrese la nota 3: "))
##notaf=(nota1+nota2+nota3)/3
##if notaf>7:
##    print("Ha sido promocionado.")
##elif notaf>=5 and notaf<=7:
##    print("Su nota es regular.")
##elif notaf<5:
##    print("Ha sido reprobado")



#EJERCICIO 3
##art=int(input("Ingrese el precio del producto: "))
##cant=int(input("Ingrese la cantidad del producto: "))
##sub=art*cant
##if cant<10:
##    desc=0
##    total=sub-desc
##    print("El total es de",total,"sin descuento.")
##elif cant>=10 and cant<=20:
##    desc=sub*0.10
##    total=sub-desc
##    print("El total es de",total,"con 10% de descuento.")
##elif cant>=21 and cant<=30:
##    desc=sub*0.20
##    total=sub-desc
##    print("El total es de",total,"con 20% de descuento")
##elif cant>30:
##    desc=sub*0.30
##    total=sub-desc
##    print("El total es de",total,"con 30% de descuento.")

#EJERCICIO 04
##num=int(input("Ingresar numero de 4 digitos: "))
##if (len(str(num)))<4:
##    print("Error")
##else:
##    d4=num%10
##    num=num//10
##    d3=num%10
##    print("El tercer dígito es ",d3)

#EJERCICIO 05
##vdesc=pre=mdc=uni=tp=0
##pre=int(input("Ingrese el precio de docenas: "))
##doc=int(input("Ingrese el numero de docenas: "))
##if doc>3:
##    vdesc=0.15
##    uni=doc-3
##else:
##    vdesc=0.10
##mdc=pre*doc
##de=mdc*vdesc
##tp=mdc-de
##print("Monto de compra: L", mdc)
##print("Monto de descuento: L", de)
##print("Monto a pagar: L", tp)
##print("Unidades de obsequio: ", uni)

###EJERCICIO 06
##num=int(input("Ingrese un número entre 10 y 99: "))
##d2=num%10
##num=num//10
##d1=num%10
##if d1<d2:
##    r=d1+d2
##else:
##    r=d1-d2
##print("El resultado es ",r)
##
##
###EJERCICIO 07
##alt=float(input("Ingrese su altura (cm): "))
##if alt<=150:
##    print("Persona de baja estatura.")
##elif alt>=151 and alt<=170:
##    print("Persona de estatura media")
##elif alt>=171:
##    print("Persona de estatura alta.")





















    
