
#import pandas as pd
#import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


# Clase para el sistema de gestión comercial
class SistemaGestionComercial:
    def __init__(self):
        self.usuarios = []
        self.clientes = []
        self.proveedores = []
        self.productos = []
        self.metodos_pago = []
        self.ventas = []

    # Funciones para la gestión de información
    def registrar_usuario(self, nombre, direccion, telefono, correo):
        usuario = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo
        }
        self.usuarios.append(usuario)
        messagebox.showinfo("Registro de Usuario", "Usuario registrado exitosamente.")

    def ingresar_cliente(self, nombre, direccion, telefono, correo):
        cliente = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo
        }
        self.clientes.append(cliente)
        messagebox.showinfo("Ingreso de Cliente", "Cliente ingresado exitosamente.")

    def ingresar_proveedor(self, nombre, direccion, contacto):
        proveedor = {
            'nombre': nombre,
            'direccion': direccion,
            'contacto': contacto
        }
        self.proveedores.append(proveedor)
        messagebox.showinfo("Ingreso de Proveedor", "Proveedor ingresado exitosamente.")

    # Funciones para el cálculo del IVA
    def configurar_valores_iva(self, valores_iva):
        self.valores_iva = valores_iva
        messagebox.showinfo("Configuración de IVA", "Valores de IVA configurados exitosamente.")

    def calcular_iva(self, precio, porcentaje_iva):
        iva = precio * (porcentaje_iva / 100)
        return iva

    # Funciones para la gestión de inventarios de ventas
    def registrar_venta(self, producto, cantidad, precio, cliente):
        venta = {
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'cliente': cliente
        }
        self.ventas.append(venta)
        # Actualizar inventario
        # ...
        messagebox.showinfo("Registro de Venta", "Venta registrada exitosamente.")

    def generar_informe_ventas(self):
        df_ventas = pd.DataFrame(self.ventas)
        informe_ventas = df_ventas.groupby('producto').sum()['cantidad']
        messagebox.showinfo("Informe de Ventas", str(informe_ventas))

    def generar_informe_inventario(self):
        # Generar informe de inventario
        # ...
        messagebox.showinfo("Informe de Inventario", "Informe de inventario generado exitosamente.")

    def generar_informe_clientes(self):
        # Generar informe de clientes
        # ...
        messagebox.showinfo("Informe de Clientes", "Informe de clientes generado exitosamente.")

    # Funciones para el catálogo de productos
    def ingresar_producto(self, nombre, descripcion, precio, proveedor, porcentaje_iva):
        producto = {
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'proveedor': proveedor,
            'porcentaje_iva': porcentaje_iva
        }
        self.productos.append(producto)
        messagebox.showinfo("Ingreso de Producto", "Producto ingresado exitosamente.")

    # Funciones para el sistema de pagos
    def registrar_metodo_pago(self, metodo_pago):
        self.metodos_pago.append(metodo_pago)
        messagebox.showinfo("Registro de Método de Pago", "Método de pago registrado exitosamente.")

    def seleccionar_metodo_pago(self, metodo_pago):
        # Seleccionar método de pago
        # ...
        messagebox.showinfo("Selección de Método de Pago", f"Método de pago seleccionado: {metodo_pago}")

    def enviar_factura(self, cliente, factura):
        # Enviar factura por correo electrónico al cliente
        # ...
        messagebox.showinfo("Envío de Factura", f"Factura enviada al cliente: {cliente}")

    # Funciones para el sistema de gráficos
    def generar_grafico_productos_mas_vendidos(self):
        df_ventas = pd.DataFrame(self.ventas)
        productos_mas_vendidos = df_ventas.groupby('producto').sum().nlargest(10, 'cantidad')
        productos_mas_vendidos.plot(kind='bar', x='producto', y='cantidad')
        plt.show()

    # Función para el menú principal
    def menu_principal(self):
        def mostrar_registro_usuario():
            ventana_registro_usuario = tk.Toplevel(ventana_principal)
            ventana_registro_usuario.title("Registro de Usuario")
            ventana_registro_usuario.geometry("800x600")

            def registrar_usuario():
                nombre = entry_nombre.get()
                direccion = entry_direccion.get()
                telefono = entry_telefono.get()
                correo = entry_correo.get()
                self.registrar_usuario(nombre, direccion, telefono, correo)
                ventana_registro_usuario.destroy()

            label_nombre = tk.Label(ventana_registro_usuario, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_registro_usuario)
            entry_nombre.pack()

            label_direccion = tk.Label(ventana_registro_usuario, text="Dirección:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_registro_usuario)
            entry_direccion.pack()

            label_telefono = tk.Label(ventana_registro_usuario, text="Teléfono:")
            label_telefono.pack()
            entry_telefono = tk.Entry(ventana_registro_usuario)
            entry_telefono.pack()

            label_correo = tk.Label(ventana_registro_usuario, text="Correo electrónico:")
            label_correo.pack()
            entry_correo = tk.Entry(ventana_registro_usuario)
            entry_correo.pack()

            btn_registrar = tk.Button(ventana_registro_usuario, text="Registrar", command=registrar_usuario)
            btn_registrar.pack()

        def mostrar_ingreso_cliente():
            ventana_ingreso_cliente = tk.Toplevel(ventana_principal)
            ventana_ingreso_cliente.title("Ingreso de Cliente")
            ventana_ingreso_cliente.geometry("800x600")

            def ingresar_cliente():
                nombre = entry_nombre.get()
                direccion = entry_direccion.get()
                telefono = entry_telefono.get()
                correo = entry_correo.get()
                self.ingresar_cliente(nombre, direccion, telefono, correo)
                ventana_ingreso_cliente.destroy()

            label_nombre = tk.Label(ventana_ingreso_cliente, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_cliente)
            entry_nombre.pack()

            label_direccion = tk.Label(ventana_ingreso_cliente, text="Dirección:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_ingreso_cliente)
            entry_direccion.pack()

            label_telefono = tk.Label(ventana_ingreso_cliente, text="Teléfono:")
            label_telefono.pack()
            entry_telefono = tk.Entry(ventana_ingreso_cliente)
            entry_telefono.pack()

            label_correo = tk.Label(ventana_ingreso_cliente, text="Correo electrónico:")
            label_correo.pack()
            entry_correo = tk.Entry(ventana_ingreso_cliente)
            entry_correo.pack()

            btn_ingresar = tk.Button(ventana_ingreso_cliente, text="Ingresar", command=ingresar_cliente)
            btn_ingresar.pack()

        def mostrar_ingreso_proveedor():
            ventana_ingreso_proveedor = tk.Toplevel(ventana_principal)
            ventana_ingreso_proveedor.title("Ingreso de Proveedor")
            ventana_ingreso_proveedor.geometry("800x600")

            def ingresar_proveedor():
                nombre = entry_nombre.get()
                direccion = entry_direccion.get()
                contacto = entry_contacto.get()
                self.ingresar_proveedor(nombre, direccion, contacto)
                ventana_ingreso_proveedor.destroy()

            label_nombre = tk.Label(ventana_ingreso_proveedor, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_proveedor)
            entry_nombre.pack()

            label_direccion = tk.Label(ventana_ingreso_proveedor, text="Dirección:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_ingreso_proveedor)
            entry_direccion.pack()

            label_contacto = tk.Label(ventana_ingreso_proveedor, text="Contacto:")
            label_contacto.pack()
            entry_contacto = tk.Entry(ventana_ingreso_proveedor)
            entry_contacto.pack()

            btn_ingresar = tk.Button(ventana_ingreso_proveedor, text="Ingresar", command=ingresar_proveedor)
            btn_ingresar.pack()

        def mostrar_configuracion_iva():
            ventana_configuracion_iva = tk.Toplevel(ventana_principal)
            ventana_configuracion_iva.title("Configuración de IVA")
            ventana_configuracion_iva.geometry("800x600")

            def configurar_iva():
                valores_iva = entry_valores_iva.get().split(',')
                self.configurar_valores_iva(valores_iva)
                ventana_configuracion_iva.destroy()

            label_valores_iva = tk.Label(ventana_configuracion_iva, text="Valores de IVA (separados por coma):")
            label_valores_iva.pack()
            entry_valores_iva = tk.Entry(ventana_configuracion_iva)
            entry_valores_iva.pack()

            btn_configurar = tk.Button(ventana_configuracion_iva, text="Configurar", command=configurar_iva)
            btn_configurar.pack()

        def mostrar_registro_venta():
            ventana_registro_venta = tk.Toplevel(ventana_principal)
            ventana_registro_venta.title("Registro de Venta")
            ventana_registro_venta.geometry("800x600")

            def registrar_venta():
                producto = entry_producto.get()
                cantidad = entry_cantidad.get()
                precio = entry_precio.get()
                cliente = entry_cliente.get()
                self.registrar_venta(producto, cantidad, precio, cliente)
                ventana_registro_venta.destroy()

            label_producto = tk.Label(ventana_registro_venta, text="Producto:")
            label_producto.pack()
            entry_producto = tk.Entry(ventana_registro_venta)
            entry_producto.pack()

            label_cantidad = tk.Label(ventana_registro_venta, text="Cantidad:")
            label_cantidad.pack()
            entry_cantidad = tk.Entry(ventana_registro_venta)
            entry_cantidad.pack()

            label_precio = tk.Label(ventana_registro_venta, text="Precio:")
            label_precio.pack()
            entry_precio = tk.Entry(ventana_registro_venta)
            entry_precio.pack()

            label_cliente = tk.Label(ventana_registro_venta, text="Cliente:")
            label_cliente.pack()
            entry_cliente = tk.Entry(ventana_registro_venta)
            entry_cliente.pack()

            btn_registrar = tk.Button(ventana_registro_venta, text="Registrar", command=registrar_venta)
            btn_registrar.pack()

        def mostrar_informe_ventas():
            ventana_informe_ventas = tk.Toplevel(ventana_principal)
            ventana_informe_ventas.title("Informe de Ventas")
            ventana_informe_ventas.geometry("800x600")

            def generar_informe():
                self.generar_informe_ventas()
                ventana_informe_ventas.destroy()

            btn_generar = tk.Button(ventana_informe_ventas, text="Generar Informe", command=generar_informe)
            btn_generar.pack()

        def mostrar_informe_inventario():
            ventana_informe_inventario = tk.Toplevel(ventana_principal)
            ventana_informe_inventario.title("Informe de Inventario")
            ventana_informe_inventario.geometry("800x600")

            def generar_informe():
                self.generar_informe_inventario()
                ventana_informe_inventario.destroy()

            btn_generar = tk.Button(ventana_informe_inventario, text="Generar Informe", command=generar_informe)
            btn_generar.pack()

        def mostrar_informe_clientes():
            ventana_informe_clientes = tk.Toplevel(ventana_principal)
            ventana_informe_clientes.title("Informe de Clientes")
            ventana_informe_clientes.geometry("800x600")

            def generar_informe():
                self.generar_informe_clientes()
                ventana_informe_clientes.destroy()

            btn_generar = tk.Button(ventana_informe_clientes, text="Generar Informe", command=generar_informe)
            btn_generar.pack()

        def mostrar_ingreso_producto():
            ventana_ingreso_producto = tk.Toplevel(ventana_principal)
            ventana_ingreso_producto.title("Ingreso de Producto")
            ventana_ingreso_producto.geometry("800x600")

            def ingresar_producto():
                nombre = entry_nombre.get()
                descripcion = entry_descripcion.get()
                precio = entry_precio.get()
                proveedor = entry_proveedor.get()
                porcentaje_iva = entry_porcentaje_iva.get()
                self.ingresar_producto(nombre, descripcion, precio, proveedor, porcentaje_iva)
                ventana_ingreso_producto.destroy()

            label_nombre = tk.Label(ventana_ingreso_producto, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_producto)
            entry_nombre.pack()

            label_descripcion = tk.Label(ventana_ingreso_producto, text="Descripción:")
            label_descripcion.pack()
            entry_descripcion = tk.Entry(ventana_ingreso_producto)
            entry_descripcion.pack()

            label_precio = tk.Label(ventana_ingreso_producto, text="Precio:")
            label_precio.pack()
            entry_precio = tk.Entry(ventana_ingreso_producto)
            entry_precio.pack()

            label_proveedor = tk.Label(ventana_ingreso_producto, text="Proveedor:")
            label_proveedor.pack()
            entry_proveedor = tk.Entry(ventana_ingreso_producto)
            entry_proveedor.pack()

            label_porcentaje_iva = tk.Label(ventana_ingreso_producto, text="Porcentaje de IVA:")
            label_porcentaje_iva.pack()
            entry_porcentaje_iva = tk.Entry(ventana_ingreso_producto)
            entry_porcentaje_iva.pack()

            btn_ingresar = tk.Button(ventana_ingreso_producto, text="Ingresar", command=ingresar_producto)
            btn_ingresar.pack()

        def mostrar_registro_metodo_pago():
            ventana_registro_metodo_pago = tk.Toplevel(ventana_principal)
            ventana_registro_metodo_pago.title("Registro de Método de Pago")
            ventana_registro_metodo_pago.geometry("800x600")

            def registrar_metodo_pago():
                metodo_pago = entry_metodo_pago.get()
                self.registrar_metodo_pago(metodo_pago)
                ventana_registro_metodo_pago.destroy()

            label_metodo_pago = tk.Label(ventana_registro_metodo_pago, text="Método de Pago:")
            label_metodo_pago.pack()
            entry_metodo_pago = tk.Entry(ventana_registro_metodo_pago)
            entry_metodo_pago.pack()

            btn_registrar = tk.Button(ventana_registro_metodo_pago, text="Registrar", command=registrar_metodo_pago)
            btn_registrar.pack()

        def mostrar_seleccion_metodo_pago():
            ventana_seleccion_metodo_pago = tk.Toplevel(ventana_principal)
            ventana_seleccion_metodo_pago.title("Selección de Método de Pago")
            ventana_seleccion_metodo_pago.geometry("800x600")

            def seleccionar_metodo_pago():
                metodo_pago = entry_metodo_pago.get()
                self.seleccionar_metodo_pago(metodo_pago)
                ventana_seleccion_metodo_pago.destroy()

            label_metodo_pago = tk.Label(ventana_seleccion_metodo_pago, text="Método de Pago:")
            label_metodo_pago.pack()
            entry_metodo_pago = tk.Entry(ventana_seleccion_metodo_pago)
            entry_metodo_pago.pack()

            btn_seleccionar = tk.Button(ventana_seleccion_metodo_pago, text="Seleccionar", command=seleccionar_metodo_pago)
            btn_seleccionar.pack()

        def mostrar_envio_factura():
            ventana_envio_factura = tk.Toplevel(ventana_principal)
            ventana_envio_factura.title("Envío de Factura")
            ventana_envio_factura.geometry("800x600")

            def enviar_factura():
                cliente = entry_cliente.get()
                factura = entry_factura.get()
                self.enviar_factura(cliente, factura)
                ventana_envio_factura.destroy()

            label_cliente = tk.Label(ventana_envio_factura, text="Cliente:")
            label_cliente.pack()
            entry_cliente = tk.Entry(ventana_envio_factura)
            entry_cliente.pack()

            label_factura = tk.Label(ventana_envio_factura, text="Factura:")
            label_factura.pack()
            entry_factura = tk.Entry(ventana_envio_factura)
            entry_factura.pack()

            btn_enviar = tk.Button(ventana_envio_factura, text="Enviar", command=enviar_factura)
            btn_enviar.pack()

        def mostrar_grafico_productos_mas_vendidos():
            ventana_grafico_productos_mas_vendidos = tk.Toplevel(ventana_principal)
            ventana_grafico_productos_mas_vendidos.title("Gráfico de Productos Más Vendidos")
            ventana_grafico_productos_mas_vendidos.geometry("800x600")

            def generar_grafico():
                self.generar_grafico_productos_mas_vendidos()
                ventana_grafico_productos_mas_vendidos.destroy()

            btn_generar = tk.Button(ventana_grafico_productos_mas_vendidos, text="Generar Gráfico", command=generar_grafico)
            btn_generar.pack()

        ventana_principal = tk.Tk()
        ventana_principal.title("Sistema de Gestión Comercial Avanzado")
        ventana_principal.geometry("800x600")

        btn_registro_usuario = tk.Button(ventana_principal, text="Registrar Usuario", command=mostrar_registro_usuario, width=20, height=2)
        btn_registro_usuario.pack(pady=10)

        btn_ingreso_cliente = tk.Button(ventana_principal, text="Ingresar Cliente", command=mostrar_ingreso_cliente, width=20, height=2)
        btn_ingreso_cliente.pack(pady=10)

        btn_ingreso_proveedor = tk.Button(ventana_principal, text="Ingresar Proveedor", command=mostrar_ingreso_proveedor, width=20, height=2)
        btn_ingreso_proveedor.pack(pady=10)

        btn_configuracion_iva = tk.Button(ventana_principal, text="Configuración de IVA", command=mostrar_configuracion_iva, width=20, height=2)
        btn_configuracion_iva.pack(pady=10)

        btn_registro_venta = tk.Button(ventana_principal, text="Registrar Venta", command=mostrar_registro_venta, width=20, height=2)
        btn_registro_venta.pack(pady=10)

        btn_informe_ventas = tk.Button(ventana_principal, text="Informe de Ventas", command=mostrar_informe_ventas, width=20, height=2)
        btn_informe_ventas.pack(pady=10)

        btn_informe_inventario = tk.Button(ventana_principal, text="Informe de Inventario",command=mostrar_informe_inventario, width=20, height=2)
        btn_informe_inventario.pack(pady=10)

        btn_informe_clientes = tk.Button(ventana_principal, text="Informe de Clientes", command=mostrar_informe_clientes, width=20, height=2)
        btn_informe_clientes.pack(pady=10)

        btn_ingreso_producto = tk.Button(ventana_principal, text="Ingresar Producto", command=mostrar_ingreso_producto, width=20, height=2)
        btn_ingreso_producto.pack(pady=10)

        btn_registro_metodo_pago = tk.Button(ventana_principal, text="Registrar Método de Pago", command=mostrar_registro_metodo_pago, width=20, height=2)
        btn_registro_metodo_pago.pack(pady=10)

        btn_seleccion_metodo_pago = tk.Button(ventana_principal, text="Selección de Método de Pago", command=mostrar_seleccion_metodo_pago, width=20, height=2)
        btn_seleccion_metodo_pago.pack(pady=10)

        btn_envio_factura = tk.Button(ventana_principal, text="Envío de Factura", command=mostrar_envio_factura, width=20, height=2)
        btn_envio_factura.pack(pady=10)

        btn_grafico_productos_mas_vendidos = tk.Button(ventana_principal, text="Gráfico de Productos Más Vendidos", command=mostrar_grafico_productos_mas_vendidos, width=20, height=2)
        btn_grafico_productos_mas_vendidos.pack(pady=10)

        ventana_principal.mainloop()


# Ejemplo de uso del programa
sistema = SistemaGestionComercial()
sistema.menu_principal()