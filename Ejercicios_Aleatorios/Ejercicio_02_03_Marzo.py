import random
num=str(input("Ingrese un numero aleatorio de 3 digitos: "))
ca1=int()
ca2=int()
ca3=int()
ca1,ca2,ca3=list(num)
if ca1>ca3:
    print(int(ca1**2))
else:
    print("Error")
