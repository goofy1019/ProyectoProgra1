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

def guardar_en_csv(productos):
    df = pd.DataFrame(productos)
    df.to_csv("Catalogo_Productos.csv", encoding='utf-8', index=False)

def cargar_desde_csv():
    try:
        df = pd.read_csv("Catalogo_Productos.csv")
        return df.to_dict(orient='records')
    except FileNotFoundError:
        return []

Productos_Agregados = cargar_desde_csv()
nuevos_productos = Categoria_de_productos()
Productos_Agregados.extend(nuevos_productos)
guardar_en_csv(Productos_Agregados)

df = pd.DataFrame(Productos_Agregados)
print(df)
