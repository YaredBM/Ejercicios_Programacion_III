#*
#**
#***
#****
n=int(input("Ingrese valor para n: "))
x=1
for x in range(n):
    for y in range(x+1):
        print("*",end=" ")
    print("")
