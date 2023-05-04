#EJERCICIO DECIMAS PARCIAL 2

estudiante = []

estudiante["nombre"] = input("Ingrese el nombre del estudiante")
estudiante["asignatura"] = input("Ingrese el nombre de la asignatura")
estudiante["Nota laboratorio 1"] = float(input("Ingrese la primera nota"))
estudiante["Nota laboratorio 2"] = float(input("ingrese la segunda nota"))

promedio = (estudiante["Nota laboratorio 1"] * 0.3) + (estudiante["Nota laboratorio 2"] * 0.7)

estudiante["promedio"] = round(promedio,1)

print("Informacion del estudiante")
print(f"Nombre",(estudiante["nombre"]))
print(f"Asignatura",(estudiante["asignatura"]))
print(f"Nota laboratorio 1",(estudiante["Nota laboratorio 1"]))
print(f"Nota laboratorio 2",(estudiante["Nota laboratorio 2"]))
print("Promedio final",(estudiante["promedio"]))
