import csv

# Registrar clientes
while True:
    cliente = input("Ingrese el nombre del cliente (o 'salir' para terminar): ")
    if cliente.lower() == "salir":
        break

    direccionCliente = input("Ingrese la dirección del cliente: ")
    telefonoCliente = int(input("Ingrese el número de teléfono del cliente: "))
    correoCliente = input("Ingrese el correo electrónico del cliente: ")

    # Guardar los datos en un archivo CSV
    with open("clientes.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([cliente, direccionCliente, telefonoCliente, correoCliente])

print("¡Clientes registrados exitosamente!")

