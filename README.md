#Registrar usuarios
while True:
    usuario=input("Igrese el nombre de usuario:   (o 'salir' para terminar): ")
    if usuario.lower() == "salir":
        break
    direccion=input("Ingrese su direccion:   ")
    telefono=int (input("Ingrese su numero de telefono:   "))
    correo=input("Ingrese su correo electronico:   ")
#Registrar clientes
while True:
    cliente=input("Ingrese el nombre del cliente:  (o 'salir' para terminar): ")
    if cliente.lower() == "salir":
        break
    cliente=input("Ingrese el nombre del cliente:  ")
    direccionCliente=input("Ingrese la direccion del cliente:   ")
    telefonoCliente=int (input("Ingrese el numero de telefono del cliente:   "))
    correoCliente=input("Ingrese el correo electronico del cliente:   ")
#Registrar Proveedores
while True:
    proveedor=input("Ingrese el nombre del proveedor:  (o 'salir' para terminar): ")
    if proveedor.lower() == "salir":
        break
    proveedor=input("Ingrese el nombre del proveedor:  ")
    direccionProveedor=input("Ingrese la direccion del proveedor:   ")
    telefonoProveedor=int (input("Ingrese el numero de telefono del proveedor:   "))
    correoProveedor=input("Ingrese el correo electronico del proveedor:   ")
    empresa=input("Ingrese el nombre de la empresa:   ")# ProyectoProgra1
