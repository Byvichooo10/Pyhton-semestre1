print("Hola")
#Este es un comentario

#Dclarando una variable
nombre = "Vicente"

#Impresion de una variable
print(nombre)
print("Hola soy", nombre)

#Declarando segundo variable
edad = 18

print("tengo", edad , "años")

#print("Hola mi nombre es" + nombre + "y tengo" + str(edad) + "años")
print("Hola mi nombre es" + " " + nombre + " " + "y tengo" + " " + str(edad) + " " + "años")

#nombre = "Vicho"
#print("Hola mi nuevo nombre es", nombre)

#Utilizando la instruccion input
nombre = input("¿Cual es tu nombre?\n")
print("Tu nombre es:",nombre)

print("Hola me llamo" + " " + nombre + " " + "Mi edad es de" + " " + str(edad) + " " + "Años")

#06- VARIABLES EN UNA SOLA LINEA
ciudad, region, pais, year = "Osorno", "Los lagos", "Chile", "2023"
print("Yo naci en ", ciudad, pais)