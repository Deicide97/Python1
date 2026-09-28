# explicacion. ciclo for repite cantidades de veces

# mostrar mensaje "hola mundo 10 veces"
mensaje = input("Que mensajes quieres mostrar: ")
cantidad = int(input("Cuantas veces quiere repetir el mensaje: "))

for i in range(cantidad):
    print(f"{mensaje}")

# Ejercicio 1: Tabla de multiplicar

numero = int(input("Ingrese un numero para ver su tabla de multiplicar"))

for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")

# Ejercicio 2: Suma numeros naturales

n = int(input("Ingrese un numero entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"la suma de los primeros {n} numeros naturales es: {suma}")

# ciclo for que se repita 3 veces con conocimiento del numero secreto
numero_secreto = 5 
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto: "))

    if numero == numero_secreto:
        print("¡FELICIDADES! Adivinaste el numero.")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"Te quedan {intentos - (i + 1)} intentos.")

        if intentos_restantes == 0 : 
           print(f"El numero secreto era {numero_secreto}") 

# ciclo for que se repita 3 veces sin saber el numero, es importado por random 
import random

numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto: "))

    if numero == numero_secreto:
        print("¡FELICIDADES! Adivinaste el numero.")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"Te quedan {intentos - (i + 1)} intentos.")

        if intentos_restantes == 0 : 
           print(f"El numero secreto era {numero_secreto}") 

# Adivina numero v2

import random

numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto: "))

    if numero == numero_secreto:
        print("¡FELICIDADES! Adivinaste el numero.")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"Te quedan {intentos - (i + 1)} intentos.")

        if intentos_restantes == 0 : 
           print(f"El numero secreto era {numero_secreto}") 

        if numero > numero_secreto:
           print(f"Muy alto")
        if numero < numero_secreto:
            print(f"Muy bajo.")

# Ejercicio 3: Contar pares con While
n = int(input("Ingrese un numero entero positivo: "))

contador =0
numero =1
while numero < = n:
    if numero % 2 == 0:
        contador = contador + 1

print(f"Hay {contador} numeros pares entre 1 y {n}") 

#Ejercicio 4: validar contraseña
clave_correcta = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")

#Ejercicio 5: factorial con for
n = int(input("Ingrese un numero entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")


