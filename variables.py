#ejercicio 1: suma de dos numeros
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))


suma = numero1 + numero2
print("La suma es: {suma}")


#ejercicio 2: area de un rectangulo
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))


area = base * altura
print(f"El area del rectangulo es: {area}")


#ejercicio 3: conversion de minutos a horas y minutos
minutos_totales = int(input("Ingrese la cantidad de minutos: "))
horas = minutos_totales // 60  #division entera: horas completas
minutos = minutos_totales % 60  #modulo: minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")


#ejercicio 4: calculo del precio con descuento
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje del descuento: "))

valor_descuento = precio * (descuento / 100) # valor que se descuenta
precio_final = precio - valor_descuento  #precio con descuento aplicado

print("El precio final a pagar es: {precio_final}")


#ejercicio 5: intercambio de variables
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
auxiliar = a  #guarda temporalmente el valor de a
a = b  #a toma el valor de b
b = auxiliar  #b toma el valor original de a 

print(f"Despues del intercambio: a = {a} , b = {b}")


#__________ taller-ejercicio 1:
largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))
perimetro = largo * ancho

print("El perimetro es: ", perimetro)


#__________ taller-ejercicio 2:
numero1 = float(input("Ingrese su primer numero: "))
numero2 = float(input("Ingrese su segundo numero: "))
numero3 = float(input("Ingrese su tercer numero: "))
total = numero1 + numero2 + numero3
promedio = total / 3

print("Su promedio es: ", promedio)


#__________ taller-ejercicio 3:
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad:"))
print(f"\n Hola, mi nombre es {nombre} y mi edad es {edad} años")


#__________ taller-ejercicio 4:
peso_colombiano = float(input("Ingrese el valor en peso colombiano: "))
tasa_cambio = 4000
dolares = peso_colombiano / tasa_cambio
print(f"El valor equivalente a dolares es: {dolares:.2f}")


#__________ taller-ejercicio 5:
segundos = int(input("Ingrese la cantidad de segundos:"))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos")