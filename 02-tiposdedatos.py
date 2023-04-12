#01-DATOS DE TIPO NUMERICO
estatura = 1.73
peso = 60
complejo = 1 +4j

print("Impresion del numero complejo:",complejo)

#OPERACION ARITMETICA BASICA
imc = peso/estatura**2
print("Mi imc es de:" ,imc)

print("mi imc es de {:.2f}".format(imc))

#02- DATOS DE TIPO DE CADENA
asignatura = "Programacion" 
carrera = "Ingenieria civil en informatica"
print("Mi carrera es",carrera, "y estoy en la asignatura de",asignatura)

#03- VALORES BOOLEANOS
ampolleta = False
interruptor = True

#CON TYPE SABEMOS EL TIPO DE DATOS QUE ESTAMOS TRATANDO
print(type(ampolleta))

#04- DATOS DE TIPOS ARRAY (OBJETOS DE TIPO COLECCION)
estudiantes = ["Vicente", "Matias", "Carlos", "Andres"]
print(estudiantes)
num = [1,2,3,4,5,6,2]
print(num)
lenguaje = ["Pyhton"]

#DECLARANDO O INICIANDO LISTAS
nueva_lista = list()
print("Esta es una lista vacia:",nueva_lista)

otra_lista = []
print("Esta es otra lista vacia",otra_lista)
print(type(otra_lista))

print("Lista de numeros:", num)
print(len(num))
print(num.count(2))

#Como accedo a un elemento en especifico de la lista?
print(estudiantes[0]) #0 siempre es primer elemento de la lista
print(estudiantes[1])
print(estudiantes[3])
print(estudiantes[-2]) #Se invierten posiciones

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