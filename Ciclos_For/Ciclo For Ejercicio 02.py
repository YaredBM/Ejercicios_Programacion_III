#1
#12
#123
#1234
n=int(input("Ingrese valor para n: "))
x=1
for x in range(1,n+1):
    for y in range(1,x+1):
        print(y,end=" ")
    print("")
