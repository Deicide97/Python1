"""
# repaso clase pasada, ejercicio2:
var_nombre = input("Por favor ingrese su nombre: ")

#variable numerica( int= numero entero, float =para decimales)
var_edad = int(input(f"{var_nombre} Por favor ingresa tu edad: "))

# Validar si la edad es > = 18 y mostrar un mensaje que diga que es mayor
if var_edad >= 18 :
    print(f"{var_nombre} usted es mayor de edad")

else:
    print(f"{var_nombre} usted es menor de edad")


# Ejercio1: Determinar si un numero es positivo, negativo cero
numero = float(input("por favor ingrese un numero: "))

# validar 3 opciones . positivo, negativo o cero
if numero > 0: # opcion 1: validar si es positivo
    print(f"el numero : {numero} es positivo")

elif numero < 0 : # opcion 2: validar si es negativo
    print(f"el numero : {numero} es negativo")   

else:
     print(f"el numero : {numero} es cero")     


# Ejercicio3: determinar si un numero es par o impar
numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:  # si el residuo es 0 es par 
    print(f"{numero} es par")

elif numero % 2 != 0: # si el residuo es diferente es impar
    print(f"el numero {numero} es impar")

else:
    print(f"{numero} es impar")    

# ejercicio4: clasificar una nota academica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota > 5:
    print("Nota invalida")
elif nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño basico")
elif nota >= 0:
    print("Desempeño bajo")
else:
    print("Nota invalida")

"""
# Ejercicio5: Determinar el mayor de tres numeros
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n1 == n2 and n1 == n3:
    mayor = "numeros iguales"
elif n2 >= n1 and n2 >= n3:
    mayor = n2
elif n1 >= n2 and n1 >= n3:
    mayor = n1
else: 
    mayor = n3