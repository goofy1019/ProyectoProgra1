import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def actualizar_seleccion(*args):
    opcion = filtro_combobox.get()
    if opcion == "Cliente":
        opciones_seleccion = list(data['cliente'].unique())
    elif opcion == "Producto":
        opciones_seleccion = list(data['producto'].unique())
    elif opcion == "TipoPago":
        opciones_seleccion = list(data['metodo_pago'].unique())
    else:
        opciones_seleccion = []
    opciones_seleccion.insert(0, "Todos")
    seleccion_combobox["values"] = opciones_seleccion

def generar_informe():
    opcion = filtro_combobox.get()
    seleccion = seleccion_combobox.get()
    
    if seleccion == "Todos":
        ventas_filtradas = data.copy()
        titulo = f"Informe de ventas para todos los {opcion.lower()}s"
    else:
        if opcion == "Cliente":
            filtro_columna = 'cliente'
            titulo = f"Informe de ventas para el cliente: {seleccion}"
        elif opcion == "Producto":
            filtro_columna = 'producto'
            titulo = f"Informe de ventas para el producto: {seleccion}"
        elif opcion == "TipoPago":
            filtro_columna = 'metodo_pago'
            ventas_filtradas = data[data[filtro_columna] == seleccion]
            titulo = f"Informe de ventas para el tipo de pago: {seleccion}"
        else:
            messagebox.showinfo("Error", "Opción de filtrado no válida.")
            return
        
        ventas_filtradas = data[data[filtro_columna] == seleccion]

    # Calcular el total de ventas para la selección
    total_ventas = ventas_filtradas['cantidad'] * ventas_filtradas['precio']
    ventas_filtradas['total_venta'] = total_ventas

    informe_text.delete(1.0, tk.END)  # Limpiar el área de texto

    if ventas_filtradas.empty:
        messagebox.showinfo("Información", f"No se encontraron ventas para la {opcion.lower()} especificada: {seleccion}")
    else:
        informe_text.insert(tk.END, f"{titulo}\n\n")
        informe_text.insert(tk.END, ventas_filtradas[['id', 'cliente', 'producto', 'cantidad', 'precio', 'total_venta', 'metodo_pago']].to_string(index=False))
        monto_total_ventas = total_ventas.sum()
        informe_text.insert(tk.END, f"\n\nMonto total de ventas: ${monto_total_ventas:.2f}")

# Cargar el archivo CSV en un DataFrame
archivo_csv = "registroventas.csv"
data = pd.read_csv(archivo_csv)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Generador de Informes de Ventas")

# Etiqueta y opción para elegir el filtro
filtro_label = tk.Label(ventana, text="Seleccione un Filtro:")
filtro_label.pack()
filtro_combobox = ttk.Combobox(ventana, values=["Cliente", "Producto", "TipoPago"], state="readonly")
filtro_combobox.pack()
filtro_combobox.bind("<<ComboboxSelected>>", actualizar_seleccion)

# Etiqueta y opción para elegir la selección (cliente, producto o tipo de pago)
seleccion_label = tk.Label(ventana, text="Seleccione un Cliente, Producto o Tipo de Pago:")
seleccion_label.pack()
seleccion_combobox = ttk.Combobox(ventana, values=[], state="readonly")
seleccion_combobox.pack()

# Botón para generar el informe
generar_button = tk.Button(ventana, text="Generar Informe", command=generar_informe)
generar_button.pack()

# Área de texto para mostrar el informe
informe_text = tk.Text(ventana)
informe_text.pack()
