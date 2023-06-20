# EJERCICIO 1

pal = input("Ingrese una palabra por favor")

if pal == pal[::-1]:
    print("La palabra que ha sido ingresada es un palíndromo.")
else:
    print("La palabra que ha sido ingresada no es un palíndromo.")