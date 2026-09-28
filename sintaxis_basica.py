# introduccion a las variables en python

nombre = "daisy" #variable tipo string (cadena de texto)
documento = 32244732 #variable tipo int (numero entero)
direccion = "medellin" #variable tipo string (cadena de texto)
tiene_deudas = True #variable tipo bool(booleano)

# mostrar contenido de una variable
print("daisy")

# concatenacion usando +
print("concatenacion usando +")
print("=" * 30)

# el operador + permite unir textos.
print("mi nombre es: " + nombre + "y mi documento es: " + str(documento))

# concatenacion usando ,
print("\nconcatenacion usando ,")
print("=" * 30)
print("Mi nombre es: ", nombre, "y mi documento es: ", documento)

#concatenacion usando f-strings
print("\nconcatenacion usando f-strings")
print("=" * 30)
print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

#f-strings con varias variables y varias lineas
print("\nmostrar varias variables con f-strings")
print("=" * 30)
print(f"""
Nombre:         {nombre}
Documento:      {documento}
Direccion:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")

#salto de linea en python(\n)
print(f"\n Hola, {nombre}!")   #salto al inicio
print(f"Bienvenida {nombre} a Python. \n")   #salto al final

#operadores aritmeticos en python
numero1 = 10
numero2 = 3

#suma
suma = numero1 + numero2
print(f"Suma: {suma}")

#resta
resta = numero1 - numero2
print(f"Resta: {resta}")

#multiplicacion
multiplicacion = numero1 * numero2
print(f"Multiplicacion: {multiplicacion}")

#division
division = numero1 / numero2
print(f"Division: {division}")

#division entera
division_entera = numero1 // numero2
print(f"Division entera: {division_entera}")

#residuo
residuo = numero1 % numero2
print(f"Residuo: {residuo}")

#potencia
potencia = numero1 ** numero2
print(f"Potencia: {potencia}")

#resumen de operadores aritmeticos
print(f"""
Resultado de Operaciones Aritmeticas:
Suma: {numero1} + {numero2} = {suma}
Resta: {numero1} - {numero2} = {resta}
Multiplicacion: {numero1} * {numero2} = {multiplicacion}
Division: {numero1} / {numero2} = {division:.4f}
Division entera: {numero1} // {numero2} = {division_entera}
Residuo: {numero1} % {numero2} = {residuo}
Potencia: {numero1} ** {numero2} = {potencia}
""")























































