#EJERCICIO 3

temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}

#A
if 9 in temp_min and 9 in temp_max:
    print("La temperatura 9°C está en los ambos sets")
else:
    print("La temperatura 9°C no está en los ambos sets")

#B
if 6 in temp_min or 6 in temp_max or 17 in temp_min or 17 in temp_max:
    print("Una de las temperaturas 6°C o 17°C se encuentra en alguno de los sets")
else:
    print("Las temperaturas 6°C o 17°C no estan en alguno de los dos sets")

#C
temp_min = {temp**4 for temp in temp_min}
temp_max = {temp**4 for temp in temp_max}

print("Asi quedarian las temperaturas mínimas elevadas a 4:", temp_min)
print("Asi quedarian las temperaturas máximas elevadas a 4:", temp_max)

#D
todaslas_temperaturas = temp_min.union(temp_max)
print(todaslas_temperaturas)