import pandas as pd #Libreria que ayuda a analizar los CSV
#import matplotlib.pyplot as plt
import tkinter as tk #Libreria de la interfaz
from tkinter import messagebox #Verifica que se importe los messageboxes para poder interactuar con el usuario
import smtplib #Libreria que nos va a ayudar con el manejo de los envios de correo
from PIL import Image, ImageTk #Libreria para poder insertar imagenes en la interfaz
import csv
import subprocess

######################################################################################################################################

# Clase para el sistema de gestión comercial
class SistemaGestionComercial:
    #Funcion para inicializar ciertas variables y elementos necesarios
    def __init__(self):
        self.usuarios = []
        self.clientes = self.cargar_clientes_desde_csv()
        self.proveedores = []
        self.productos = self.cargar_desde_csv()
        self.metodos_pago = []
        self.ventas = self.cargar_ventas_desde_csv()
        self.id_venta = 1
        self.cargar_metodos_pago()

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
        self.guardar_clientes_en_csv()  # Llamamos a la función para guardar en CSV
        messagebox.showinfo("Ingreso de Cliente", "Cliente ingresado exitosamente.")

    def guardar_clientes_en_csv(self):
        with open("clientes.csv", "w", newline="") as csvfile:
            fieldnames = ['nombre', 'direccion', 'telefono', 'correo']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for cliente in self.clientes:
                csv_writer.writerow(cliente)

    def cargar_clientes_desde_csv(self):
        try:
            df_clientes = pd.read_csv("clientes.csv")
            clientes = df_clientes.to_dict('records')
            return clientes
        except FileNotFoundError:
            return []

    def ingresar_proveedor(self, nombre, direccion, contacto):
        proveedor = {
            'nombre': nombre,
            'direccion': direccion,
            'contacto': contacto
        }
        self.proveedores.append(proveedor)
        messagebox.showinfo("Ingreso de Proveedor", "Proveedor ingresado exitosamente.")

    # Funciones para el cálculo del IVA
    def calcular_precio_con_iva(self, precio, Valor_IVA):
        while True:
            precio = float(input("Ingrese el precio (ingrese 0 para salir): "))
            Valor_IVA = float(input("Ingese el valor de IVA: "))
            if precio == 0:
                break
        iva = precio * Valor_IVA
        precio_con_iva = precio + iva
        print(f"El precio con IVA es: {precio_con_iva}") 
    
    
    # Funciones para la gestión de inventarios de ventas
    def registrar_venta(self, producto, cantidad, cliente_nombre, metodo_pago):
        producto_encontrado = None
        for prod in self.productos:
            if prod['Nombre'] == producto:
                producto_encontrado = prod
                break

        if producto_encontrado is None:
            messagebox.showerror("Error", "Producto no encontrado.")
            return

        precio = producto_encontrado['Precio']

        cliente_encontrado = None
        for c in self.clientes:
            if c['nombre'] == cliente_nombre:
                cliente_encontrado = c
                break

        if cliente_encontrado is None:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return
            
        venta = {
            'id': len(self.ventas) + 1,
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'cliente': cliente_encontrado['nombre'],
            'metodo_pago': metodo_pago
        }
    
        self.ventas.append(venta)
        self.actualizar_inventario(producto, cantidad)
        self.guardar_ventas_en_csv()
        self.id_venta += 1
        messagebox.showinfo("Registro de Venta", "Venta registrada exitosamente.")

    #Carga las ventas anteriores
    def cargar_ventas_desde_csv(self):
        try:
            df_ventas = pd.read_csv('RegistroVentas.csv')
            df_ventas['id'] = df_ventas['id'].astype(int)  # Convertir la columna 'id' a enteros
            ventas = df_ventas.to_dict('records')
            return ventas
        except FileNotFoundError:
            return []

    def obtener_producto_por_nombre(self, nombre_producto):
        for prod in self.productos:
            if prod['Nombre'] == nombre_producto:
                return prod
        return None

    #Carga los productos del catalogo para que cada vez que se empiece el programa salgan
    def cargar_desde_csv(self):
        try:
            df_productos = pd.read_csv("Catalogo_Productos.csv")
            return df_productos.to_dict(orient='records')
        except FileNotFoundError:
            return []

    #Funciones para poder guardar la info de ventas usando la libreria pandas
    def guardar_ventas_en_csv(self):
        df_ventas = pd.DataFrame(self.ventas)
        df_ventas.to_csv('RegistroVentas.csv', index=False)

    def guardar_productos_en_csv(self):
        df_productos = pd.DataFrame(self.productos)
        df_productos.to_csv('Catalogo_Productos.csv', index=False)

    #Funcion para poder actualizar el inventario
    def actualizar_inventario(self, producto, cantidad_vendida):
        for prod in self.productos:
            if prod['Nombre'] == producto:
                prod['Cantidad'] -= int(cantidad_vendida)
        self.guardar_productos_en_csv()


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
    def ingresar_producto(self, nombre, precio, Cantidad):
        producto = {
            'nombre': nombre,
            'precio': precio,
            'Cantidad': Cantidad
        }
        self.productos.append(producto)
        messagebox.showinfo("Ingreso de Producto", "Producto ingresado exitosamente.")

    #Funcion que carga los metodos de pago aceptados
    def cargar_metodos_pago(self):
        try:
            metodos_pago_df = pd.read_csv("metodos_pago.csv")
            self.metodos_pago = metodos_pago_df["metodo_pago"].tolist()
        except FileNotFoundError:
            self.metodos_pago = []

    #Guarda los metodos de pago cuando ya se termina
    def guardar_metodos_pago(self):
        metodos_pago_df = pd.DataFrame({"metodo_pago": self.metodos_pago})
        metodos_pago_df.to_csv("metodos_pago.csv", index=False)

    #Funcion que ayuda para registrar un metodo de pago
    def registrar_metodo_pago(self, metodo_pago):
        self.metodos_pago.append(metodo_pago)
        self.guardar_metodos_pago()
        messagebox.showinfo("Registro de Método de Pago", "Método de pago registrado exitosamente.")

    #Funcion para enviar factura al cliente
    def enviar_factura(self, cliente, id_venta):
        venta_encontrada = None
        for venta in self.ventas:
            if venta['id'] == id_venta:
                venta_encontrada = venta
                break

        if venta_encontrada:
            # Configurar los detalles del servidor de correo
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "gestionsistema53@gmail.com"
            sender_password = "owpexhtgwaicabqn"

            # Crear el mensaje
            subject = "Factura para el cliente"
            message = f"Estimado cliente {cliente},\nAdjuntamos la factura de la venta:\n\n"
            message += f"ID de Venta: {venta['id']}\n"
            message += f"Producto: {venta['producto']}\n"
            message += f"Cantidad: {venta['cantidad']}\n"
            message += f"Precio: {venta['precio']}\n"
            message += f"Método de Pago: {venta['metodo_pago']}\n\n"

            try:
                # Iniciar conexión con el servidor
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                # Iniciar sesión con tu cuenta de correo
                server.login(sender_email, sender_password)
            
                # Construir el mensaje completo
                full_message = f"Subject: {subject}\n\n{message}"
            
                # Convertir el mensaje a bytes utilizando UTF-8
                full_message_bytes = full_message.encode("utf-8")
            
                # Enviar el correo electrónico
                server.sendmail(sender_email, cliente, full_message_bytes)
            
                # Terminar la conexión
                server.quit()


                messagebox.showinfo("Envío de Factura", "Factura enviada exitosamente por correo electrónico.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo enviar la factura. Error: {str(e)}")

        else:
            messagebox.showerror("Error", f"No se encontró la venta con ID {id_venta}.")

######################################################################################################################################

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
            ventana_ingreso_cliente.geometry("500x500")

            def cargar_clientes_desde_csv():
                self.clientes = self.cargar_clientes_desde_csv()

            def abrir_archivo_csv():
                try:
                    subprocess.Popen(["start", "clientes.csv"], shell=True)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo abrir el archivo CSV. Error: {str(e)}")

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

            btn_abrir_csv = tk.Button(ventana_ingreso_cliente, text="Abrir CSV en Excel", command=abrir_archivo_csv)
            btn_abrir_csv.pack()

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

        #Funcion que modifica la interfaz de la ventana para el registro de las ventas
        def mostrar_registro_venta():
            ventana_registro_venta = tk.Toplevel(ventana_principal)
            ventana_registro_venta.title("Registro de Venta")
            ventana_registro_venta.geometry("300x250")

            def registrar_venta():
                producto = entry_producto.get()
                cantidad = entry_cantidad.get()
                cliente = cliente_var.get()
                metodo_pago = metodo_pago_var.get()

                if not metodo_pago:
                    messagebox.showerror("Error", "Por favor, seleccione un método de pago.")
                    return

                sistema.registrar_venta(producto, cantidad, cliente, metodo_pago)
                ventana_registro_venta.destroy()


            label_producto = tk.Label(ventana_registro_venta, text="Producto:")
            label_producto.pack()
            entry_producto = tk.Entry(ventana_registro_venta)
            entry_producto.pack()

            label_cantidad = tk.Label(ventana_registro_venta, text="Cantidad:")
            label_cantidad.pack()
            entry_cantidad = tk.Entry(ventana_registro_venta)
            entry_cantidad.pack()

            label_cliente = tk.Label(ventana_registro_venta, text="Cliente:")
            label_cliente.pack()
             # Obtener la lista de clientes desde el sistema y crear el menú desplegable
            clientes = [cliente['nombre'] for cliente in sistema.clientes]
            cliente_var = tk.StringVar(ventana_registro_venta)
            cliente_var.set("")  # Valor inicial vacío
            dropdown_cliente = tk.OptionMenu(ventana_registro_venta, cliente_var, *clientes)
            dropdown_cliente.pack()

            label_metodo_pago = tk.Label(ventana_registro_venta, text="Método de Pago:")
            label_metodo_pago.pack()

            metodo_pago_var = tk.StringVar(ventana_registro_venta)
            metodo_pago_var.set("")  # Valor inicial vacío
            dropdown_metodo_pago = tk.OptionMenu(ventana_registro_venta, metodo_pago_var, *sistema.metodos_pago)
            dropdown_metodo_pago.pack()

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
            ventana_registro_metodo_pago.geometry("200x100")

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

        def mostrar_envio_factura():
            ventana_envio_factura = tk.Toplevel(ventana_principal)
            ventana_envio_factura.title("Envío de Factura")
            ventana_envio_factura.geometry("300x250")

            def enviar_factura():
                cliente = cliente_var.get()
                id_venta_str = entry_id_venta.get()  # Obtener el ID de venta ingresado como cadena
                cliente_encontrado = None
                try:
                    id_venta = int(id_venta_str)  # Convertir la cadena a entero
                    for c in sistema.clientes:
                        if c['nombre'] == cliente:
                            cliente_encontrado = c
                            break
                    if cliente_encontrado:
                        correo_cliente = cliente_encontrado['correo']
                        sistema.enviar_factura(correo_cliente, id_venta)  # Llamar a la función enviar_factura
                        ventana_envio_factura.destroy()
                    else:
                        messagebox.showerror("Error", "Cliente no encontrado.")
                except ValueError:
                    messagebox.showerror("Error", "ID de Venta debe ser un número entero")

            label_cliente = tk.Label(ventana_envio_factura, text="Cliente:")
            label_cliente.pack()

            # Obtener la lista de clientes desde el sistema y crear el menú desplegable
            clientes = [cliente['nombre'] for cliente in sistema.clientes]
            cliente_var = tk.StringVar(ventana_envio_factura)
            cliente_var.set("")  # Valor inicial vacío
            dropdown_cliente = tk.OptionMenu(ventana_envio_factura, cliente_var, *clientes)
            dropdown_cliente.pack()

            label_id_venta = tk.Label(ventana_envio_factura, text="ID de Venta:")
            label_id_venta.pack()
            entry_id_venta = tk.Entry(ventana_envio_factura)
            entry_id_venta.pack()

            btn_enviar = tk.Button(ventana_envio_factura, text="Enviar", command=enviar_factura)
            btn_enviar.pack()

######################################################################################################################################

        ventana_principal = tk.Tk()
        ventana_principal.title("Sistema de Gestión Comercial")
        ventana_principal.geometry("600x700")
        
        imagen_fondo = Image.open("Stonks.jpg")
   
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        
        label_fondo = tk.Label(ventana_principal, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        btn_registro_usuario = tk.Button(ventana_principal, text="Registrar Usuario", command=mostrar_registro_usuario, width=20, height=2)
        btn_registro_usuario.pack(pady=10)

        btn_ingreso_cliente = tk.Button(ventana_principal, text="Ingresar Cliente", command=mostrar_ingreso_cliente, width=20, height=2)
        btn_ingreso_cliente.pack(pady=10)

        btn_ingreso_proveedor = tk.Button(ventana_principal, text="Ingresar Proveedor", command=mostrar_ingreso_proveedor, width=20, height=2)
        btn_ingreso_proveedor.pack(pady=10)

        btn_configuracion_iva = tk.Button(ventana_principal, text="Configuración de IVA", command=mostrar_configuracion_iva, width=20, height=2)
        btn_configuracion_iva.pack(pady=10)

        btn_registro_venta = tk.Button(ventana_principal, text="Registrar Venta", command=mostrar_registro_venta , width=20, height=2)
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

        btn_envio_factura = tk.Button(ventana_principal, text="Envío de Factura", command=mostrar_envio_factura, width=20, height=2)
        btn_envio_factura.pack(pady=10)

        ventana_principal.mainloop()

######################################################################################################################################

#Se inicializa el sistema
sistema = SistemaGestionComercial()
sistema.menu_principal()
