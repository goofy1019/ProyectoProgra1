#Registrar usuarios
while True:
    usuario=input("Igrese el nombre de usuario:   (o 'salir' para terminar): ")
    if usuario.lower() == "salir":
        break
    direccion=input("Ingrese su direccion:   ")
    telefono=int (input("Ingrese su numero de telefono:   "))
    correo=input("Ingrese su correo electronico:   ")
