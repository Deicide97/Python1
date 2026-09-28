print("======== Tienda Merca+====\n")

#solicitar varibles
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad a comprar: "))
precio = float(input("Ingrese el precio unitario del producto: "))

#Crear variabble para calcular
subtotal = cantidad * precio
iva = subtotal * 0.19
total = subtotal + iva

print("\n=== Resumen de compra ===\n")

print(f"""
-producto..........{producto}
-cantidad..........{cantidad}
-precio unitario...{precio}
-subtotal..........{subtotal}
-iva (19%).........{iva}
-total pagar.......{total}

""")

#preguntar si quiere incluir la propina
propina = input("¿Desea incluir propina?: ")
if propina == "si" or propina == "SI" or propina == "Si" : 
    valor_propina = subtotal * 0.10
    total_final = total + valor_propina
    print("\n=== Resumen de compra ===\n")

    print(f"""
    -subtotal..........{subtotal}
    -valor propina.....{valor_propina}
    -iva (19%).........{iva}
    -total pagar.......{total_final}

""")
elif propina == "no" or propina == "NO" or propina == "No": 
    print("Gracias por su compra TACAÑO")
else:
    print("Gracias por su compra")

#===========TALLER========
#EJERCICIO 1:
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error, fallido")
elif edad >=18:
    print("Es mayor de edad")
else:
    faltan =18 - edad
    print("Es menor de edad")
    print(f"Le faltan {faltan} años para ser mayor de edad")

print(f"nombre: {nombre}")
print(f"Edad: {edad}")

#EJERCICIO 2:
print("Notas finales de los estudiantes")

variable_nombre = input("Por favore ingrese su nombre: ")
var_calificacion = float(input("Ingrese su calificacion: "))

if var_calificacion >=4.5 and var_calificacion <=5.0:
    resultado = "Aprobo"
    desempeño = "Excelente"
    print(f"Estudiante: {variable_nombre} | Calificacion: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >=3.5 and var_calificacion <4.5:
    resultado = "Aprobo"
    desempeño = "Bueno"
    print(f"Estudiante: {variable_nombre} | Calificacion: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >=3.0 and var_calificacion <3.5:
    resultado = "Aprobo"
    desempeño = "Aceptable"
    print(f"Estudiante: {variable_nombre} | Calificacion: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >=0.0 and var_calificacion <3.0:
    resultado = "Aprobo"
    desempeño = "Insuficiente"
    print(f"Estudiante: {variable_nombre} | Calificacion: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
else:
    print(f"{var_calificacion} es invalida")

#EJERCICIO 3:
nombre = input("Ingrese su nombre: ")
valor_compra = float(input("Ingrese el valor de su compra: "))

if valor_compra <=0:
    print("\n Error: El valor de la compra debe ser mayor a cero")
else:
    if valor_compra <100000:
        porcentaje_descuento =0
    elif valor_compra <300000:
        porcentaje_descuento =10
    elif valor_compra <500000:
        porcentaje_descuento =15
    else:
        porcentaje_descuento =20

valor_descontado = valor_compra * (porcentaje_descuento / 100)
total_pagar = valor_compra - valor_descontado

print(f"\n === Resumen de la factura para {nombre} ===")
print(f"Valor original de la compra: $ {valor_compra:,.2f}")
print(f"Porcentaje de descuento: {porcentaje_descuento}%")
print(f"Valor descontado: $ {valor_descontado:,.2f}")
print(f"Total a pagar: $ {total_pagar:,.2f}")

#EJERCICIO 4:
var_ciudad = input("\n Ingrese la ciudad: ") 
var_grados = float(input("\n Ingrese grados celsius: "))

if var_grados >32:
    print(f"{var_ciudad} Esta muy caliente, la temperatura es de {var_grados}° grados celsius")
elif var_grados >=26 and var_grados <=32:
    print(f"{var_ciudad} Esta caliente, la temperatura es de{var_grados}° grados celsius")
elif var_grados >= 18 and var_grados <=25:
    print(f"{var_ciudad} Esta templado, la temperatura es de {var_grados}° grados celsius")
elif var_grados >=10 and var_grados <=17:
    print(f"{var_ciudad} Esta fria, se recomienda usar abrigo, la temperatura es de {var_grados}° grados celsius")
else:
    var_grados <10:
    print(f"{var_ciudad} Esta muy frio, se recomienda usar abrigo, la temperatura es de {var_grados}° grados celsius")

#EJERCICIO 5

nombre = input("Ingrese el nombre del empleado: ")
horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

if horas <=0 or valor_hora <=0:
    print("Los valores deben ser positivos")
else:
    if horas <=160:
        horas_normales = horas
        horas_extras = 0
    else:
        horas_normales = 160
        horas_extras = horas - 160

pago_normal = horas_normales * valor_hora
pago_extra = horas_extras * valor_hora * 1.25
salario_bruto = pago_normal + pago_extra
descuento = salario_bruto * 0.08
salario_neto =salario_bruto - descuento

print(f"""
Empleado...........{nombre}
Horas normales.....{horas_normales}
Horas extras.......{horas_extras}
Pago hora normal...{valor_hora}
Pago hora extra....{valor_hora*1.25}
Salario bruto......{salario_bruto}
Descuento..........{descuento}
Salario neto.......{salario_neto}
""")

