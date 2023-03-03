cade = input("Ingresa una cadena de caracteres: ").lower()
nuevacade = ""
for cara in cade:
    if cara in "aeiou":
        if cara == "a":
            nuevacade += "e"
        elif cara == "e":
            nuevacade += "i"
        elif cara == "i":
            nuevacade += "o"
        elif cara == "o":
            nuevacade += "u"
        elif cara == "u":
            nuevacade += "a"
    else:
        nuevacade += cara
print("La cadena con las vocales reemplazadas es:", nuevacade)
