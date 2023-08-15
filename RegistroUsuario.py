import csv

# Definir el nombre del archivo CSV
archivo_csv = "usuarios.csv"

# Abrir el archivo en modo de escritura
with open(archivo_csv, mode="a", newline="") as file:
    writer = csv.writer(file)

    # Encabezados del CSV (si es la primera vez que se crea el archivo)
    if file.tell() == 0:
        writer.writerow(["Nombre de Usuario", "Dirección", "Teléfono", "Correo Electrónico"])

    # Registrar usuarios
    while True:
        usuario = input("Ingrese el nombre de usuario (o 'salir' para terminar): ")
        if usuario.lower() == "salir":
            break

        direccion = input("Ingrese su dirección: ")
        telefono = int(input("Ingrese su número de teléfono: "))
        correo = input("Ingrese su correo electrónico: ")

        # Escribir los datos en el archivo CSV
        writer.writerow([usuario, direccion, telefono, correo])

print("Los usuarios han sido registrados en", archivo_csv)

