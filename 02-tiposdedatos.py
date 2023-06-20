#01-DATOS DE TIPO NUMERICO
estatura = 1.73
peso = 60
complejo = 1 +4j

print("Impresion del numero complejo:",complejo)
print(f"mi estatura es de {estatura} y mi peso es de {peso}")

#TRANSFORMANDO DE REAL A ENTERO
print(peso)
print("Transformando un valor entero a real:",int(peso))

#TRANSFORMANDO ENTERO A REAL
print("transformando un valor entero a real:",float(peso))

#OPERACION ARITMETICA BASICA
imc = peso/estatura**2
print("Mi imc es de:" ,imc)

print("mi imc es de {:.2f}".format(imc)) #formatea el valor y lo puede hacer mas corto {:.2f} .format(imc)

#02- DATOS DE TIPO DE CADENA
asignatura = "Programacion" 
carrera = "Ingenieria civil en informatica"
print("Mi carrera es",carrera, "y estoy en la asignatura de",asignatura)

#03- VALORES BOOLEANOS
ampolleta = False
interruptor = True

#CON TYPE SABEMOS EL TIPO DE DATOS QUE ESTAMOS TRATANDO
print(type(ampolleta))

#Podemos transformar cualquier valor booleano
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("false"))
print(bool(1))
print("\n")

#04- DATOS DE TIPOS ARRAY (OBJETOS DE TIPO COLECCION)
estudiantes = ["Vicente", "Matias", "Carlos", "Andres", "Marcos"]
print(estudiantes)
num = [1,2,3,4,5,6,2]
print(num)
lenguaje = ["Pyhton"]
print("\n")

#DECLARANDO O INICIANDO LISTAS
nueva_lista = list()
print("Esta es una lista vacia:",nueva_lista)

otra_lista = []
print("Esta es otra lista vacia",otra_lista)
print(type(otra_lista))

print("Lista de numeros:", num)
print(len(num))
print(num.count(2))
print("\n")

#Como accedo a un elemento en especifico de la lista?
print(estudiantes[0]) #0 siempre es primer elemento de la lista
print(estudiantes[1])
print(estudiantes[3])
print(estudiantes[-2]) #Se invierten posiciones
print("\n")

#Sobreescribir otro dato
estudiantes[2] = "Benjamin"
print("Los estudiantes son:", estudiantes)

#INICIALIZANDO OTRA LISTA DE DATOS MIXTOS
data_asig = [10023,"Programacion",1,True]
#Que hace este codigo?
cod, ramo, semestre, estado = data_asig
print(ramo)
print(cod)

#Se pueden sumar listas?
print("Suma de listas", estudiantes + num)

print(list("Python"))
print(list(range(10)))
print(list(range(10,25)))
print("\n")

#05- TUPLAS - (NO SON MUTABLES)
grupo1 = ("Daniel" , "Cristian" , "Felipe" ,200,100, "Daniel")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite", grupo1.count("Daniel"))

#Muestra el indice del primer elemento buscado
print("indice del elemento", grupo1.index ("Daniel"))

#Reasignando el primer elemento de la tupla
#grupo1[0] = "Conztanza"

#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Diego",200,"Benjamin")
print("Trozo de la tupla", grupo2[0:3])

#Entonce como no puedo modificar una tupla, que puedo hacer?

grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#06- SETS (CONJUNTOS) - estructura fija
conjunto_vacio = set()
conjunto_vacio1 = {}
print(type(conjunto_vacio1))
conjunto_colores = ({"azul","rojo","verde"})
conjunto_animales = ["gato","perro","loro"]

print(type(conjunto_colores))
print(type(conjunto_animales))
print("El primer set contiene los siguientes colores", conjunto_colores)
print("El segundo set contiene los siguientes animales", conjunto_animales)

print(conjunto_animales[0])
conjunto_colores.add("celeste")
print("El set de colores lo conforman", conjunto_colores)

#7 DICCIONARIOS

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Vicente",
    "Institucion":"Ulagos",
    "Edad" : 18,
    "Asignaturas": {"Estructura de datos", "Programacion"}
}

print("Diccionario inicial:",datos_personales)

#Consulta cantidad de datos del diccionario
print(len(datos_personales))

#Es facilmente accesible a los elementos dentro de un diccionario
print(datos_personales["Institucion"])

#¿Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institucion"] = "USS"

#Como agregar nuevp valor de una clave
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)


#Como eliminar un valor de una clave
del datos_personales["Ciudad"]
print(datos_personales)