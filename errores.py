#Ejercicio 1: try/except basico
try:
    numero = int(input("Ingrese un numero entero: "))
    print(f"El numero ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un numero entero valido")

menu = 0

while menu != 3: 
    try:
        menu = int(input("""
    seleccione una opcion:
    1. Sumar
    2. Restar
    3. Salir del sistema

    : """))

        if menu == 1:
            n1=int(input("Ingrese el primer numero: "))
            n2=int(input("Ingrese el segundo numero: "))
            print(f"Resultado{n1+n2}: ")
        elif menu == 2:
                n1=int(input("Ingrese el primer numero: "))
                n2=int(input("Ingrese el segundo numero: "))
                print(f"Resultado{n1-n2}: ")
        else:
            print("Opcion Invalida")
    except ValueError:
         print("Inserte un numero valido")
print("Saliendo del Sistema")


# Ejercicio 2: division segura
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: Ingrese unicamente valores.")

# Ejercicio 3: else y finally
try:
     edad = int(input("Ingrese su edad: "))
except ValueError:
     print("Error: la edad debe ser un numero entero.")
else:
     if edad >= 18:
          print("Acceso permitido.")
     else:
          print("Acceso denegado: debe ser mayor de edad.")
finally:
     print("Verificacion finalizada.")

# Ejercicio 4: multiples excepciones y bucle de reintento
while True:
     try:
          nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
          if nota < 0.0 or nota > 5.0:
               raise ValueError("La nota debe estar entre 0.0 y 5.0.")
          break
     except ValueError as e:
          print(f"Entrada invalida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

# Ejercicio 5: raise, lanzar errores personalizados
def calcular_promedio(notas):
     if len(notas) == 0:
          raise ValueError("la lista de notas no puede estar vacia.")
     return sum(notas) / len(notas)

try:
     n = int(input("¿cuantas notas va a ingresar?"))
     notas = ´[]
     for i in range(n):
          nota = float(input(f"Nota {i+1}: "))
          notas.append(nota)
    promedio = calcular_promedio(notas)
print(f"promedio: {round(promedio, 2)}")
except ValueError as e:
print(f"Error:{e}")
