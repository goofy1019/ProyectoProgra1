#Registrar clientes
while True:
    cliente=input("Ingrese el nombre del cliente:  (o 'salir' para terminar): ")
    if cliente.lower() == "salir":
        break
    cliente=input("Ingrese el nombre del cliente:  ")
    direccionCliente=input("Ingrese la direccion del cliente:   ")
    telefonoCliente=int (input("Ingrese el numero de telefono del cliente:   "))
    correoCliente=input("Ingrese el correo electronico del cliente:   ")
