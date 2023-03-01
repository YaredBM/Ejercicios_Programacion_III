#Se pide el ingreso de las notas parciales (0-10) promediar e indicar
#si el alumno fue promocionado (>7), si su promedio es regular
#(>=5) y (<=7) o si está reprobado (<5).
nota1=int(input("Ingrese la nota 1: "))
nota2=int(input("Ingrese la nota 2: "))
nota3=int(input("Ingrese la nota 3: "))
notaf=(nota1+nota2+nota3)/3
if notaf>7:
    print("Ha sido promocionado.")
elif notaf>=5 and notaf<=7:
    print("Su nota es regular.")
elif notaf<5:
    print("Ha sido reprobado")







    
