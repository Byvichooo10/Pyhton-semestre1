##OPERADORES ARITMETICOS
a = 20
b = 4
c = 69
d = 3

#OPERACIONES COMUNES
print("Suma entre a + b es:",a + b)
print("Resta entre a - b es:",a - b)
print("Multiplicación entre a * b es:",a * b)
print("División entre a / b es:",a / b)
print("El módulo entre a y b es:",a % b)
print("El cociente entre b / c es:",b // c)
print("El resultado de b elevado a c (5^4):",b ** c,"\n")


#Declarando variables de tipo flotantes
t=5.19 #tiempo en segundos
g=9.81 #la aceleración de gravedad

v=g*t

print(f"la velocidad de el objeto en caida libre es de: {v} m/s")
print(f"la velocidad de el objeto en caida libre es de: {v:.2f}m/s") #ACORTAR DECIMALES
print("la velocidad de el objeto en caida libre es de: {:.2f}" .format(v), "m/s")
print("La velocidad del objeto en caida libre es de:","%.2f" % v)   

#VARIABLES TIPO COMPLEJAS
c1 = 4 + 3j
print(type(c1))

#Creando un número complejo con complex
c2=complex(3, -5)

print("el número complejo es:",c2)

print(c2.real)
print(c2.imag)

#A PROBAR
print("hola"*5) #funciona
#print("hola"*3.5*2) #ya no
print("hola" * 2)

##OPERADORES DE COMPARACIÓN
print("comparando números")
print(a == b) # IGUAL A "==" no es lo mismo que "="
print(b) # DESIGUAL A
print(a>b) # MAYOR QUE
print(a<b) # MENOR QUE
print(a>=b) # MAYOR O IGUAL QUE
print(a<=b) # MENOR O IGUAL QUE
print("\n")

#Comparar textos
animal_domestico = "gato"
animal_salvaje= "leopardo"
print(animal_domestico==animal_salvaje)   #igual a
print(animal_domestico!=animal_salvaje)   #desigual a
print(animal_domestico>animal_salvaje)    #mayor que
print(animal_domestico<animal_salvaje)    #menor que
print(animal_domestico>=animal_salvaje)   #mayor o igual que
print(animal_domestico<=animal_salvaje)   #menor o igual que


#03-OPERADORES LÓGICOS
print("#### 03-OPERADORES LÓGICOS ####")
#Trabajaremos con el siguiente ejemplo:
#Tenemos un vehiculo que tiene bencina (variable bencina) y una opcion 
#que dice si esta encendido o no (variable encendido). Dependiendo del 
#estado de cada variable, se irá cambiando por False o True

bencina = True
encendido = False
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("Utilizando NOT Y OR:  El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND y OR
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
