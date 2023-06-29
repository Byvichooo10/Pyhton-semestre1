altura = 10
ancho_base = 19
numero = 1
incremento = 1

espacios = (ancho_base - 1) // 2

for i in range(1, altura+1):
    
    for j in range(espacios):
        print(" ", end="")
   
    for k in range(2*i - 1):
        print(numero, end="")
        numero = (numero + incremento) % 10
    
    for j in range(espacios):
        print(" ", end="")

    print()
 
    espacios -= 1
    numero = 9 if incremento == 1 else 0
    incremento = -1 if incremento == 1 else 1













  