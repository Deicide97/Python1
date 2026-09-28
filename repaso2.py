# empresa de bus. venta de tiquetes
"""
Empresa de bus. Vende tiquetes de bus

Medellin -> Bogota = 120.000
Medellin -> Cali = 100.000
Medellin -> Barranquilla = 150.000
Medellin -> Cartagena = 200.000

Proceso de compra:
Solicitar.
Destino.
Cantidad de tiquetes.
Segun la cantidad de tiquetes pedir los nombres de los pasajeros.
Calcular total a pagar.
Mostrar destino, los nombres de los pasajeros, total a pagar.
"""

# Ciclo infinito para que se repita todo el proceso
while True:
    print("=== TIQUETE DE BUS === \n")

    try:
        menu =int(input("""
        Seleccion ruta de compra:
        1. Medellin - Bogota
        2. Medellin - cali
        3. Medellin - Barranquilla
        4. Medellin - Cartagena
        5.salir """))

        if menu in range (1,5):
            valor_tiquete = 0
            if menu ==1:
                valor_tiquete =120000
                ruta = "Medellin - Bogota"
            elif menu ==2:
                valor_tiquete =100000
                ruta = "Medellin - Cali"
            elif menu ==3:
                valor_tiquete =150000
                ruta = "Medellin - Barranquilla"
            elif menu ==4:
                valor_tiquete =200000
                ruta = "Medellin - Cartagena"

            try:
                cantidad = int(input("Cantidad de tiquetes a comprar"))
                lista_pasajeros = []
                for i in range(cantidad):
                    pasajero = input(f"Ingrese el nombre del pasajero {i+1} ")
                    #guardar el valor de la variable en la lista
                    lista_pasajeros.append(pasajero)
                print(f"""
                === RESUMEN DE COMPRA ===
                -Ruta = {ruta}
                -Cantidad de pasajeros = {cantidad}
                -Valor tiquete = {valor_tiquete}
                -Total = {cantidad * valor_tiquete}
                -Pasajeros = {lista_pasajeros}
                """)
            except ValueError:
                print("Ingrese una cantidad valida")
        
        elif menu ==5:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalida")
            break

    except ValueError:
        print("Ingrese una opcion valida")

        

