#Reto clase 3

ciudades = ["Santiago", "Temuco", "Osorno", "Punta arenas"]
indice_calidad_deaire = [134,99,245,50]

indice_minimo = min(indice_calidad_deaire)
ciudad_minima = ciudades[indice_calidad_deaire.index(indice_minimo)]

indice_maximo = max(indice_calidad_deaire)
ciudad_maxima = ciudades[indice_calidad_deaire.index(indice_maximo)]

print("La ciudad con indice mas bajo de calidad de aire es", ciudad_minima, indice_minimo)
print("La ciudad con indice mas alto de calidad de aire es", ciudad_maxima, indice_maximo)

for i in range(len(ciudades)):
    if indice_minimo >= 0 and indice_maximo <= 50:
        print(ciudades[indice_calidad_deaire.index(indice_maximo)],"Tiene un indice de calidad del aire BUENA")
    elif indice_minimo >= 51 and indice_maximo <= 100:
        print(ciudades[i],"Tiene un indice de calidad del aire MODERADO")
    elif indice_minimo >= 101 and indice_maximo <= 150:
        print(ciudades[i],"Tiene un indice de calidad del aire DAÑINA PARA LA SALUD A GRUPOS SENSIBLES")
    elif indice_minimo >= 151 and indice_maximo <= 200:
        print(ciudades[i],"Tiene un indice de calidad del aire DAÑINA PARA LA SALUD")    
    elif indice_minimo >= 201 and indice_maximo <= 300:
        print(ciudades[i],"Tiene un indice de calidad del aire MUY DAÑINA PARA LA SALUD")
    else :
        print(ciudades[i],"Tiene un indice de calidad del aire PELIGROSA")        