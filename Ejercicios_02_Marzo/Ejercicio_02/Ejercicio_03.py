cade=input("Ingrese una cadena: ")
cara=input("Ingrese un caracter: ")
cade1=""
for x in cade:
    if x in "0123456789":
        cade1+=cara
print(cade1)