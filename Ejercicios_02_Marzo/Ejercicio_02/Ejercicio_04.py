cade=input("Ingrese una cadena: ")
cara=input("Ingrese un caracter: ")
#abc=("abcdefghijklmnopqrstuvwxyz")
cade1=0
#for x in cade:
 #   if x==cara:
  #      cade1+=1
#print(cade1)
for x in cade:
    if x in cara:
        cade1+=1
print(cade1)