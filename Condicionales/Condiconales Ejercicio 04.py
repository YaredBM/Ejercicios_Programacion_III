#Escribe un programa que pida el ingreso de un número de 4 dígitos
#e imprima el tercer dígito junto imprimir un mensaje de error si
#el número ingresado no es de 4 dígitos.

num=int(input("Ingresar numero de 4 digitos: "))
if (len(str(num)))<4:
    print("Error")
else:
    d4=num%10
    num=num//10
    d3=num%10
    print("El tercer dígito es ",d3)
















    
