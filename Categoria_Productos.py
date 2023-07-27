import pandas as pd
def Categoria_de_productos():
    lista_productos = []
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto (fin para salir): ")
        if nombre_producto == "fin":
            break
        Precio_producto = float(input("Ingrese el precio del producto: "))
        Categoria_Producto = input("Ingrese la categoria a la que pertenece el producto: ")
        

        producto = {
            'Nombre': nombre_producto,
            'Precio': Precio_producto,
            'Categoria': Categoria_Producto
        }
        lista_productos.append(producto)

    return lista_productos

Productos_Agregados = Categoria_de_productos()
df = pd.DataFrame(Productos_Agregados)
print(df)