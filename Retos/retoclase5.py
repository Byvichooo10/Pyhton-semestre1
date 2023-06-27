#RETO CLASE 5

def num_par(numero):
 if numero % 2 == 0:
  print("El numero es par")
 else:
  print("El numero es impar")

def num_primo(numero):
 if numero < 2:
  print("El numero no es primo")
 else:
  for i in range(2, int(numero ** 0.5) + 1):
   if numero % i == 0:
    print("El numero no es primo")
    return  
   print("El numero es primo")

def mayor_menor(numero):
 if numero > 50:
  print("El nuumero es mayor que 50")
 elif numero < 50:
  print("El numero es menor a 50")   
 else:
  print("El numero es igual a 50")

numero = int(input("Ingrese un numero: "))
num_par(numero)
num_primo(numero)
mayor_menor(numero)