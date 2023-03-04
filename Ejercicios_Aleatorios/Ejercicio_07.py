# Un programa que pide un numero aleatorio de 3 digitos, si el primer digito es mayor
# que el tercero, imprimir el caracter correspondiente del resultado de elevar al cuadrado
# el segundo dígito y ese resultado multiplicarlo por el digito tres, caso contrario
# solo imprima el segundo digito.
num=int(input("Ingrese número de tres dígitos: ")) #875
n3=num%10
n2=num%100//10
n1=num%1000//100
if n1>n3:
    nn2=(n2**2)
    r1=chr(nn2)
    nn3=(nn2*n3)
    print("El resultado de multiplicar ",nn2," por el digito tres es: ",nn3)
    print("El caracter correspondiente de elevar al cuadrado el segundo dígito es: ",r1)
else:
    print("El segundo dígito es: ",n2)