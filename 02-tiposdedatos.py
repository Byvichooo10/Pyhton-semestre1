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
print(list("Benjamin"))