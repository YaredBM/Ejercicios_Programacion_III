# Solicitar un número al usuario
num = int(input("Ingrese un número: "))

# Generar la sucesión en forma de pirámide
for i in range(1, num+1):
    # Imprimir los números de la sucesión en cada fila de la pirámide
    for j in range(i):
        if j == i-1:
            print(i+j, end="")
        else:
            print(i+j, end=" ")
    print("")
##1
##2 
##3 4
##4 5 7
##5 6 8
