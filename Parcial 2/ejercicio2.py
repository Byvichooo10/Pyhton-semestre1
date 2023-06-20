altura = 10
ancho_base = 19
numero = 1
incremento = 1

# Calcular el número de espacios en la primera línea
espacios = (ancho_base - 1) // 2

# Imprimir la pirámide
for i in range(1, altura+1):
    # Imprimir espacios en blanco
    for j in range(espacios):
        print(" ", end="")
    
    # Imprimir números
    for k in range(2*i - 1):
        print(numero, end="")
        numero = (numero + incremento) % 10
    
    # Imprimir espacios en blanco
    for j in range(espacios):
        print(" ", end="")
    
    # Cambiar de línea
    print()
    
    # Actualizar el número de espacios para la siguiente línea
    espacios -= 1
    
    # Actualizar el número y dirección del incremento
    numero = 9 if incremento == 1 else 0
    incremento = -1 if incremento == 1 else 1













  