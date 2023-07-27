def calcular_precio_con_iva():
    while True:
        precio = float(input("Ingrese el precio (ingrese 0 para salir): "))
        if precio == 0:
            break
        iva = precio * 0.13
        precio_con_iva = precio + iva
        print(f"El precio con IVA es: {precio_con_iva}")
calcular_precio_con_iva()