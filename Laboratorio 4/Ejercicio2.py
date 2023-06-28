a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

# A) Crear una función para encontrar los valores en común de las tres listas

def valores_comunes():
    valores_comun = set(a) & set(b) & set (c)
    return list(valores_comun)

print(valores_comunes)