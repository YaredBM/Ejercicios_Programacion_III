#EJERCICIO 05
#Si tenemos una cadena con un nombre y apellidos realizar un programa que muestre las dos
#primeras letras de cada uno. La primera en mayusculas y la segunda en minúscula
nombre_completo = input("Ingresa tu nombre completo: ")
partes_nombre = nombre_completo.split()
iniciales = ""
for parte in partes_nombre:
    inicial = (parte[0].upper() + parte[1].lower())
    iniciales += inicial
print(iniciales)

