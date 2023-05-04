##OPERADORES ARITMETICOS
a = 20
b = 4
c = 69
d = 3
print("suma", a+b)
print("resta",c-a)
print("exponente",b**d)
#faltan

#GRAVEDAD
t=5.19
g=9.81
v=g*t
print(f"la velocidad de el objeto en caida libre es de: {v} m/s")
print(f"la velocidad de el objeto en caida libre es de: {v:.2f}m/s") #ACORTAR DECIMALES
print("la velocidad de el objeto en caida libre es de: {:.2f}" .format(v), "m/s")

#COMPLEJOS
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
print(a == b) # "==" no es lo mismo que "="
print(b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("\n")

#Comparar textos
animal_domestico="gato"
animal_salvaje="leopardo"
print(animal_domestico==animal_salvaje)
print(animal_domestico>animal_salvaje)
print(animal_domestico<animal_salvaje)