#Reto clase 3

ciudades = ["Santiago", "Temuco", "Osorno", "Punta arenas"]
indice_calidad_deaire = [134,99,245,50]

indice_minimo = min(indice_calidad_deaire)
ciudad_minima = ciudades[indice_calidad_deaire.index(indice_minimo)]

indice_maximo = max(indice_calidad_deaire)
ciudad_maxima = ciudades[indice_calidad_deaire.index(indice_maximo)]

print("La ciudad con indice mas bajo de calidad de aire es", ciudad_minima, indice_minimo)
print("La ciudad con indice mas alto de calidad de aire es", ciudad_maxima, indice_maximo)  