#100 personas realizan el lanzamiento del dado.Determinar cuantas personas obtubieron los siguentes caras:
#cara1...a la cara 6
import random
c1=c2=c3=c4=c5=c6=0
for x in range(100):
    c=random.randint(1,6)
    if c==1:
        c1+=1
    elif c==2:
        c2+=1
    elif c==3:
        c3+=1
    elif c==4:
        c4+=1
    elif c==5:
        c5+=1
    else:
        c6+=1
print("Cara 1: ",c1)
print("Cara 2: ",c2)
print("Cara 3: ",c3)
print("Cara 4: ",c4)
print("Cara 5: ",c5)
print("Cara 6: ",c6)