import pandas as pd
def Categoria_de_productos():
    lista_productos = []
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto (fin para salir): ")
        if nombre_producto == "fin":
            break
        Precio_producto = float(input("Ingrese el precio del producto: "))
        Cantidad_Producto = int(input("Ingrese la cantidad del producto: "))
        

        producto = {
            'Nombre': nombre_producto,
            'Precio': Precio_producto,
            'Cantidad': Cantidad_Producto
        }
        lista_productos.append(producto)

    return lista_productos

Productos_Agregados = Categoria_de_productos()
df = pd.DataFrame(Productos_Agregados)
df.to_csv("Catalogo_Productos.csv", encoding='utf-8')
print(df)
