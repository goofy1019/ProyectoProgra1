import csv

def guardar_en_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(datos)

def main():
    while True:
        proveedor = input("Ingrese el nombre del proveedor (o 'salir' para terminar): ")
        if proveedor.lower() == "salir":
            break
        
        direccionProveedor = input("Ingrese la dirección del proveedor: ")
        telefonoProveedor = int(input("Ingrese el número de teléfono del proveedor: "))
        correoProveedor = input("Ingrese el correo electrónico del proveedor: ")
        empresa = input("Ingrese el nombre de la empresa: ")
        
        datos_proveedor = [proveedor, direccionProveedor, telefonoProveedor, correoProveedor, empresa]
        
        guardar_en_csv(datos_proveedor, 'proveedores.csv')
        
        print("Proveedor registrado exitosamente.")

if __name__ == "__main__":
    main()

