#EJERCICIO 13
#Escribir un programa que pregunte el correo electronico del usuario en la consola
#y muestre por pantalla otro correo electronico con el mismo nombre(la parte delante de la arroba)
#pero con dominio maristascomayagua.edu.hn
correo = input("Ingresa tu dirección de correo electrónico: ")
usuario, dominio = correo.split('@')
dom = '@maristascomayagua.edu.hn'
nuevocorreo = (usuario + dom)
print(nuevocorreo)
