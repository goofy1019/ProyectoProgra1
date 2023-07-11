import csv

producto = " "
cantidad = " "
precio = " "
cliente = " "

def nuevoProducto(producto, cantidad, precio, cliente):
    producto = input("Producto: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    cliente = input("Cliente: ")
    with open("RegistroVentas.csv", mode='w') as registro_file:
        registro_writer = csv.writer(registro_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        registro_writer.writerow([producto, cantidad, precio, cliente])
    
