import pandas as pd #Libreria que ayuda a analizar los CSV
#import matplotlib.pyplot as plt
import tkinter as tk #Libreria de la interfaz
from tkinter import messagebox #Verifica que se importe los messageboxes para poder interactuar con el usuario
from tkinter import ttk #Para poder hacer uno de los dropdowns
import smtplib #Libreria que nos va a ayudar con el manejo de los envios de correo
from PIL import Image, ImageTk #Libreria para poder insertar imagenes en la interfaz
import csv
import subprocess #Libreria que nos va a permitir hacer varios procesos a la vez, para lo de los clientes

######################################################################################################################################

#Clase para el sistema de gestión comercial
class SistemaGestionComercial:
    
    #Funcion para inicializar ciertas variables y elementos necesarios
    def __init__(self):
        self.usuarios = self.cargar_usuarios_desde_csv() #Llama a los usuarios que ya estan en el CSV
        self.clientes = self.cargar_clientes_desde_csv() #Llama a los clientes que ya estan en el CSV
        self.proveedores = self.cargar_proveedores_desde_csv() #Llama a los proveedores que ya estan en el CSV
        self.productos = self.cargar_desde_csv() #Llama a los productos que ya estan en el CSV
        self.metodos_pago = []
        self.ventas = self.cargar_ventas_desde_csv() #Llama a las ventas que ya estan en el CSV
        self.id_venta = 1
        self.cargar_metodos_pago()

    #Funciones para la gestión de los usuarios
    def registrar_usuario(self, nombre, direccion, telefono, correo):
        usuario = {
            'usuario': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo
        }
        self.usuarios.append(usuario) #Se agrega al usuario al CSV
        self.guardar_usuarios_en_csv()  #Llamamos a la función para guardar los usuarios en el CSV
        messagebox.showinfo("Ingreso de Usuario", "Usuario ingresado exitosamente.")

    def guardar_usuarios_en_csv(self):
        with open("usuarios.csv", "w", newline="") as csvfile:
            fieldnames = ['usuario', 'direccion', 'telefono', 'correo']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for usuario in self.usuarios:
                csv_writer.writerow(usuario)

    def cargar_usuarios_desde_csv(self):
        try:
            df_usuarios = pd.read_csv("usuarios.csv")
            usuarios = df_usuarios.to_dict('records')
            return usuarios
        except FileNotFoundError:
            return []
        
    #Funciones para la gestión de los clientes
    def ingresar_cliente(self, nombre, direccion, telefono, correo):
        cliente = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo
        }
        self.clientes.append(cliente) #Se agrega al cliente al CSV
        self.guardar_clientes_en_csv()  #Llamamos a la función para guardar los clientes en el CSV
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

    #Funciones para la gestión de los proveedores
    def ingresar_proveedor(self, nombre, empresa, direccion, contacto):
        proveedor = {
            'nombre': nombre,
            'empresa': empresa,
            'telefono': direccion,
            'correo': contacto
        }
        self.proveedores.append(proveedor) #Se agrega al proveedor al CSV
        self.guardar_proveedores_en_csv()  #Llamamos a la función para guardar los proveedores en el CSV
        messagebox.showinfo("Ingreso de Proveedor", "Proveedor ingresado exitosamente.")

    def guardar_proveedores_en_csv(self):
        with open("proveedores.csv", "w", newline="") as csvfile:
            fieldnames = ['nombre', 'empresa', 'telefono', 'correo']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for proveedor in self.proveedores:
                csv_writer.writerow(proveedor)

    def cargar_proveedores_desde_csv(self):
        try:
            df_proveedores = pd.read_csv("proveedores.csv")
            proveedores = df_proveedores.to_dict('records')
            return proveedores
        except FileNotFoundError:
            return []

    #Funciones para el cálculo del IVA
    def calcular_precio_con_iva(self, precio, Valor_IVA):
        iva = float(precio)*float(Valor_IVA)/100
        precio_con_iva = float(precio) + iva
        messagebox.showinfo("Informe de IVA", f"EL precio con el IVA incluido es: ₡{precio_con_iva}")


    #Funcion que nos permite desplegar el inventario
    def mostrar_inventario(self):
            ventana_inventario = tk.Toplevel()
            ventana_inventario.title("Inventario de Productos")
            ventana_inventario.geometry("800x600")

            label_titulo = tk.Label(ventana_inventario, text="Inventario de Productos")
            label_titulo.pack()

            # Crear una tabla o lista para mostrar los productos y su información
            lista_productos = tk.Listbox(ventana_inventario, height=30, width=100)
            lista_productos.pack()

            for producto in self.productos: #Busca todos los productos en el archivo de CSV para desplegarlos
                info_producto = f"Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}"
                lista_productos.insert(tk.END, info_producto)

            btn_cerrar = tk.Button(ventana_inventario, text="Cerrar", command=ventana_inventario.destroy)
            btn_cerrar.pack()
    
    
    #Funciones para la gestión de inventarios de ventas
    def registrar_venta(self, producto, cantidad, cliente_nombre, metodo_pago):
        producto_encontrado = None
        for prod in self.productos: #Verifica que el producto exista en el inventario
            if prod['Nombre'] == producto:
                producto_encontrado = prod
                break

        if producto_encontrado is None: #Manejo de error si no lo encuentra
            messagebox.showerror("Error", "Producto no encontrado.")
            return

        precio = producto_encontrado['Precio'] #Automaticamente determina el precio
        cantidad_disponible = producto_encontrado['Cantidad'] #Verifica cual es la cantidad disponible del producto

        cliente_encontrado = None
        for c in self.clientes: #Da la opcion de elegir a los clientes desde el registro y no tener que ingresarlos cada vez
            if c['nombre'] == cliente_nombre:
                cliente_encontrado = c
                break

        if cliente_encontrado is None: #Manejo de error si no se encuentra el cliente
            messagebox.showerror("Error", "Cliente no encontrado.")
            return

        if int(cantidad) > cantidad_disponible: #Verificacion de que se este comprando menos de lo que hay disponible
            messagebox.showerror("Error", "Cantidad insuficiente en inventario.")
            return
            
        venta = { #Se forma la venta que se va a guardar en el archivo
            'id': len(self.ventas) + 1,
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'cliente': cliente_encontrado['nombre'],
            'metodo_pago': metodo_pago
        }
    
        self.ventas.append(venta) #Se agrega la venta al CSV
        self.actualizar_inventario(producto, cantidad) #Tambien se modifica el catalogo de productos
        self.guardar_ventas_en_csv() #Se guarda la venta
        self.id_venta += 1 #Se agrega uno al id
        messagebox.showinfo("Registro de Venta", "Venta registrada exitosamente.")

    #Carga las ventas anteriores
    def cargar_ventas_desde_csv(self):
        try:
            df_ventas = pd.read_csv('RegistroVentas.csv')
            df_ventas['id'] = df_ventas['id'].astype(int)  #Convertir la columna 'id' a enteros
            ventas = df_ventas.to_dict('records')
            return ventas
        except FileNotFoundError:
            return []

    #Carga los productos del catalogo para que cada vez que se empiece el programa salgan
    def cargar_desde_csv(self):
        try:
            df_productos = pd.read_csv("Catalogo_Productos.csv")
            return df_productos.to_dict(orient='records')
        except FileNotFoundError:
            return []

    #Funcion para poder guardar la info de ventas usando la libreria pandas
    def guardar_ventas_en_csv(self):
        df_ventas = pd.DataFrame(self.ventas)
        df_ventas.to_csv('RegistroVentas.csv', index=False)

    #Funcion para poder guardar la info de inventario usando la libreria pandas
    def guardar_productos_en_csv(self):
        df_productos = pd.DataFrame(self.productos)
        df_productos.to_csv('Catalogo_Productos.csv', mode='a', header=False, index=False)

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

    def generar_informe_clientes(self):
        # Generar informe de clientes
        # ...
        messagebox.showinfo("Informe de Clientes", "Informe de clientes generado exitosamente.")

    #Funcion para el ingreso de productos
    def ingresar_producto_csv(self, nombre, precio, Cantidad, IVA):
        lista_producto = []
        precio_iva = int(precio) + (int(precio) * (float(IVA)/100))
        producto = {
            'nombre': nombre,
            'precio': precio_iva,
            'Cantidad': Cantidad
        }
        #self.productos.append(producto)
        lista_producto.append(producto)
        csv_file = pd.DataFrame(lista_producto)
        csv_file.to_csv("Catalogo_Productos.csv", mode='a', header=False, index=False)
        messagebox.showinfo("Ingreso de Producto", "Producto ingresado exitosamente.")

    #Funcion que ayuda para registrar un metodo de pago
    def registrar_metodo_pago(self, metodo_pago):
        self.metodos_pago.append(metodo_pago)
        self.guardar_metodos_pago()
        messagebox.showinfo("Registro de Método de Pago", "Método de pago registrado exitosamente.")

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

    #Funcion para enviar factura al cliente
    def enviar_factura(self, cliente, id_venta):
        venta_encontrada = None
        for venta in self.ventas: #Se maneja la factura por cada venta, utilizando el id unico de la venta
            if venta['id'] == id_venta:
                venta_encontrada = venta
                break

        if venta_encontrada:
            #Configurar los detalles del servidor de correo
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "gestionsistema53@gmail.com"
            sender_password = "owpexhtgwaicabqn"

            #Crea el mensaje del email
            preciototal = int(venta['precio']) * int(venta['cantidad'])
            subject = "Factura para el cliente"
            message = f"Estimado cliente {cliente},\nAdjuntamos la factura de la venta:\n\n"
            message += f"ID de Venta: {venta['id']}\n"
            message += f"Producto: {venta['producto']}\n"
            message += f"Cantidad: {venta['cantidad']}\n"
            message += f"Precio unitario: {venta['precio']}\n"
            message += f"Precio total: " + str(preciototal) +"\n"
            message += f"Método de Pago: {venta['metodo_pago']}\n\n"

            try:
                #Inicia conexión con el servidor
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                #Inicia sesión con gmail
                server.login(sender_email, sender_password)
            
                #Construye el mensajhe
                full_message = f"Subject: {subject}\n\n{message}"
            
                #Convertir el mensaje a bytes utilizando UTF-8 porque sino hay problemas con gmail :(
                full_message_bytes = full_message.encode("utf-8")
            
                #Enviar el correo
                server.sendmail(sender_email, cliente, full_message_bytes)
            
                #Terminar la conexión
                server.quit()


                messagebox.showinfo("Envío de Factura", "Factura enviada exitosamente por correo electrónico.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo enviar la factura. Error: {str(e)}")

        else:
            messagebox.showerror("Error", f"No se encontró la venta con ID {id_venta}.") #Se maneja el error de venta no encontrada

######################################################################################################################################

    #Función para el menú principal
    def menu_principal(self):

        #Funcion para desplegar el registro de usuarios
        def mostrar_registro_usuario():
            ventana_registro_usuario = tk.Toplevel(ventana_principal)
            ventana_registro_usuario.title("Registro de Usuario") #Nombre de ventana
            ventana_registro_usuario.geometry("300x300") #Tamano de ventana

            def registrar_usuario():
                nombre = entry_nombre.get() #Establece variable para el nombre ingresado
                direccion = entry_direccion.get() #Establece variable para la direccion ingresada
                telefono = entry_telefono.get() #Establece variable para el telefono ingresado
                correo = entry_correo.get() #Establece variable para el correo ingresado
                self.registrar_usuario(nombre, direccion, telefono, correo) #Realiza la logica llamando a la funcion que maneja eso
                ventana_registro_usuario.destroy() #Cierra la ventana cuando se termina

            #Abre input para el nombre
            label_nombre = tk.Label(ventana_registro_usuario, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_registro_usuario)
            entry_nombre.pack()

            #Abre input para la direccion
            label_direccion = tk.Label(ventana_registro_usuario, text="Dirección:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_registro_usuario)
            entry_direccion.pack()

            #Abre input para el telefono
            label_telefono = tk.Label(ventana_registro_usuario, text="Teléfono:")
            label_telefono.pack()
            entry_telefono = tk.Entry(ventana_registro_usuario)
            entry_telefono.pack()

            #Abre input para el correo
            label_correo = tk.Label(ventana_registro_usuario, text="Correo electrónico:")
            label_correo.pack()
            entry_correo = tk.Entry(ventana_registro_usuario)
            entry_correo.pack()

            btn_registrar = tk.Button(ventana_registro_usuario, text="Registrar", command=registrar_usuario) #Llama a la funcion de arriba
            btn_registrar.pack()

        #Funcion para desplegar el registro de clientes
        def mostrar_ingreso_cliente():
            ventana_ingreso_cliente = tk.Toplevel(ventana_principal)
            ventana_ingreso_cliente.title("Ingreso de Cliente") #Nombre de ventana
            ventana_ingreso_cliente.geometry("300x300") #Tamano de ventana

            #Funcion para poder cargar los clientes que ya estan
            def cargar_clientes_desde_csv():
                self.clientes = self.cargar_clientes_desde_csv()

            #Funcion para poder abrir los clientes como un subproceso y poder modificar el archivo desde Excel
            def abrir_archivo_csv():
                try:
                    subprocess.Popen(["start", "clientes.csv"], shell=True)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo abrir el archivo CSV. Error: {str(e)}")

            def ingresar_cliente():
                nombre = entry_nombre.get() #Establece variable para el nombre ingresado
                direccion = entry_direccion.get() #Establece variable para la direccion ingresada
                telefono = entry_telefono.get() #Establece variable para el telefono ingresado
                correo = entry_correo.get() #Establece variable para el correo ingresado
                self.ingresar_cliente(nombre, direccion, telefono, correo) #Realiza la logica llamando a la funcion que maneja eso
                ventana_ingreso_cliente.destroy() #Cierra la ventana cuando se termina

            #Abre input para el nombre
            label_nombre = tk.Label(ventana_ingreso_cliente, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_cliente)
            entry_nombre.pack()

            #Abre input para la direccion
            label_direccion = tk.Label(ventana_ingreso_cliente, text="Dirección:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_ingreso_cliente)
            entry_direccion.pack()

            #Abre input para el telefono
            label_telefono = tk.Label(ventana_ingreso_cliente, text="Teléfono:")
            label_telefono.pack()
            entry_telefono = tk.Entry(ventana_ingreso_cliente)
            entry_telefono.pack()

            #Abre input para el correo
            label_correo = tk.Label(ventana_ingreso_cliente, text="Correo electrónico:")
            label_correo.pack()
            entry_correo = tk.Entry(ventana_ingreso_cliente)
            entry_correo.pack()

            btn_abrir_csv = tk.Button(ventana_ingreso_cliente, text="Modificar Datos", command=abrir_archivo_csv) #Llama a la funcion para modificar desde excel
            btn_abrir_csv.pack()

            btn_ingresar = tk.Button(ventana_ingreso_cliente, text="Ingresar", command=ingresar_cliente) #Llama a la funcion de arriba
            btn_ingresar.pack()

        #Funcion para desplegar el registro de proveedores
        def mostrar_ingreso_proveedor():
            ventana_ingreso_proveedor = tk.Toplevel(ventana_principal)
            ventana_ingreso_proveedor.title("Ingreso de Proveedor") #Nombre de ventana
            ventana_ingreso_proveedor.geometry("300x300") #Tamano de ventana

            def ingresar_proveedor():
                nombre = entry_nombre.get() #Establece variable para el nombre ingresado
                empresa = entry_empresa.get() #Establece variable para la empresa ingresada
                direccion = entry_direccion.get() #Establece variable para el telefono ingresado, dice direccion porque me dio pereza cambiarlo
                contacto = entry_contacto.get() #Establece variable para el correo ingresado
                self.ingresar_proveedor(nombre, empresa, direccion, contacto) #Realiza la logica llamando a la funcion que maneja eso
                ventana_ingreso_proveedor.destroy() #Cierra la ventana cuando se termina

            #Abre input para el nombre
            label_nombre = tk.Label(ventana_ingreso_proveedor, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_proveedor)
            entry_nombre.pack()

            #Abre input para la empresa
            label_empresa = tk.Label(ventana_ingreso_proveedor, text="Empresa:")
            label_empresa.pack()
            entry_empresa = tk.Entry(ventana_ingreso_proveedor)
            entry_empresa.pack()

            #Abre input para el telefono
            label_direccion = tk.Label(ventana_ingreso_proveedor, text="Telefono:")
            label_direccion.pack()
            entry_direccion = tk.Entry(ventana_ingreso_proveedor)
            entry_direccion.pack()

            #Abre input para el correo
            label_contacto = tk.Label(ventana_ingreso_proveedor, text="Correo:")
            label_contacto.pack()
            entry_contacto = tk.Entry(ventana_ingreso_proveedor)
            entry_contacto.pack()

            btn_ingresar = tk.Button(ventana_ingreso_proveedor, text="Ingresar", command=ingresar_proveedor) #Llama a la funcion de arriba
            btn_ingresar.pack()

        def mostrar_configuracion_iva():
            ventana_configuracion_iva = tk.Toplevel(ventana_principal)
            ventana_configuracion_iva.title("Cálculo de IVA")
            ventana_configuracion_iva.geometry("200x200")

            def configurar_iva():
                precio = entry_precio_iva.get()
                porcentaje = entry_porcentaje_iva.get()
                self.calcular_precio_con_iva(precio,porcentaje)
                ventana_configuracion_iva.destroy()



            label_precio_iva = tk.Label(ventana_configuracion_iva, text="Precio:")
            label_precio_iva.pack()
            entry_precio_iva = tk.Entry(ventana_configuracion_iva)
            entry_precio_iva.pack()

            label_porcentaje_iva = tk.Label(ventana_configuracion_iva, text="Porcentaje de IVA:")
            label_porcentaje_iva.pack()
            entry_porcentaje_iva = tk.Entry(ventana_configuracion_iva)
            entry_porcentaje_iva.pack()

            btn_configurar = tk.Button(ventana_configuracion_iva, text="Calcular", command=configurar_iva)
            btn_configurar.pack()

        #Funcion que modifica la interfaz de la ventana para el registro de las ventas
        def mostrar_registro_venta():
            ventana_registro_venta = tk.Toplevel(ventana_principal)
            ventana_registro_venta.title("Registro de Venta") #Nombre de ventana
            ventana_registro_venta.geometry("300x250") #Tamano de ventana

            def registrar_venta():
                producto = entry_producto.get() #Establece variable para el producto ingresado
                cantidad = entry_cantidad.get() #Establece variable para la cantidad ingresada
                cliente = cliente_var.get() #Establece variable para el cliente ingresado
                metodo_pago = metodo_pago_var.get() #Establece variable para el metodo de pago ingresado

                #Verifica que se debe de elegir un metodo de pago
                if not metodo_pago:
                    messagebox.showerror("Error", "Por favor, seleccione un método de pago.")
                    return

                sistema.registrar_venta(producto, cantidad, cliente, metodo_pago) #Realiza la logica llamando a la funcion que maneja eso
                ventana_registro_venta.destroy() #Cierra la ventana cuando se termina

            #Abre input para el producto
            label_producto = tk.Label(ventana_registro_venta, text="Producto:")
            label_producto.pack()
            entry_producto = tk.Entry(ventana_registro_venta)
            entry_producto.pack()

            #Abre input para la cantidad
            label_cantidad = tk.Label(ventana_registro_venta, text="Cantidad:")
            label_cantidad.pack()
            entry_cantidad = tk.Entry(ventana_registro_venta)
            entry_cantidad.pack()

            #Abre input para el cliente desde un dorp down menu
            label_cliente = tk.Label(ventana_registro_venta, text="Cliente:")
            label_cliente.pack()
            clientes = [cliente['nombre'] for cliente in sistema.clientes] #Obtener la lista de clientes desde el sistema y crear el menú desplegable
            cliente_var = tk.StringVar(ventana_registro_venta)
            cliente_var.set("")  #Valor inicial vacío
            dropdown_cliente = tk.OptionMenu(ventana_registro_venta, cliente_var, *clientes)
            dropdown_cliente.pack()

            #Abre input para el metodo de pago desde un dorp down menu
            label_metodo_pago = tk.Label(ventana_registro_venta, text="Método de Pago:")
            label_metodo_pago.pack()
            metodo_pago_var = tk.StringVar(ventana_registro_venta)
            metodo_pago_var.set("")  #Valor inicial vacío
            dropdown_metodo_pago = tk.OptionMenu(ventana_registro_venta, metodo_pago_var, *sistema.metodos_pago)
            dropdown_metodo_pago.pack()

            btn_registrar = tk.Button(ventana_registro_venta, text="Registrar", command=registrar_venta) #Llama a la funcion de arriba
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
            ventana_ingreso_producto.geometry("300x300")

            def ingresar_producto():
                nombre = entry_nombre.get()
                precio = entry_precio.get()
                cantidad = entry_cantidad.get()
                IVA = combo_iva.get()
                self.ingresar_producto_csv(nombre, precio, cantidad, IVA)
                ventana_ingreso_producto.destroy()

            label_nombre = tk.Label(ventana_ingreso_producto, text="Nombre:")
            label_nombre.pack()
            entry_nombre = tk.Entry(ventana_ingreso_producto)
            entry_nombre.pack()

            label_precio = tk.Label(ventana_ingreso_producto, text="Precio:")
            label_precio.pack()
            entry_precio = tk.Entry(ventana_ingreso_producto)
            entry_precio.pack()

            label_cantidad = tk.Label(ventana_ingreso_producto, text="Cantidad:")
            label_cantidad.pack()
            entry_cantidad = tk.Entry(ventana_ingreso_producto)
            entry_cantidad.pack()

            label_iva = tk.Label(ventana_ingreso_producto, text="% IVA:")
            label_iva.pack()
            iva_opciones = ["1", "2", "4", "13"]# Crear un menú desplegable con las opciones de IVA
            combo_iva = ttk.Combobox(ventana_ingreso_producto, values=iva_opciones)
            combo_iva.pack()
            
            btn_ingresar = tk.Button(ventana_ingreso_producto, text="Ingresar", command=ingresar_producto)
            btn_ingresar.pack()

        #Funcion para desplegar el registro de metodos de pago
        def mostrar_registro_metodo_pago():
            ventana_registro_metodo_pago = tk.Toplevel(ventana_principal)
            ventana_registro_metodo_pago.title("Registro de Método de Pago") #Nombre de ventana
            ventana_registro_metodo_pago.geometry("200x100") #Tamano de ventana

            def registrar_metodo_pago():
                metodo_pago = entry_metodo_pago.get() #Establece variable para el metodo de pago
                self.registrar_metodo_pago(metodo_pago) #Realiza la logica llamando a la funcion que maneja eso
                ventana_registro_metodo_pago.destroy() #Cierra la ventana cuando se termina

            #Abre input para el metodo de pago
            label_metodo_pago = tk.Label(ventana_registro_metodo_pago, text="Método de Pago:")
            label_metodo_pago.pack()
            entry_metodo_pago = tk.Entry(ventana_registro_metodo_pago)
            entry_metodo_pago.pack()

            btn_registrar = tk.Button(ventana_registro_metodo_pago, text="Registrar", command=registrar_metodo_pago) #Llama a la funcion de arriba
            btn_registrar.pack()

        #Funcion para desplegar el envio de factruras
        def mostrar_envio_factura():
            ventana_envio_factura = tk.Toplevel(ventana_principal)
            ventana_envio_factura.title("Envío de Factura") #Nombre de ventana
            ventana_envio_factura.geometry("300x250") #Tamano de ventana

            def enviar_factura():
                cliente = cliente_var.get() #Establece variable para el cleinte ingresado
                id_venta_str = entry_id_venta.get()  #Obtener el ID de venta ingresado como string para poder omparar de manera mas facil
                cliente_encontrado = None
                try:
                    id_venta = int(id_venta_str)  #Convertir el string a int
                    for c in sistema.clientes:
                        if c['nombre'] == cliente:
                            cliente_encontrado = c
                            break
                    if cliente_encontrado: #Busca el correo del cliente que realizo la compra
                        correo_cliente = cliente_encontrado['correo']
                        sistema.enviar_factura(correo_cliente, id_venta)  #Realiza la logica llamando a la funcion que maneja eso
                        ventana_envio_factura.destroy() #Cierra la ventana cuando se termina
                    else:
                        messagebox.showerror("Error", "Cliente no encontrado.") #Manejo de errores para el cliente no encontrrad
                except ValueError:
                    messagebox.showerror("Error", "ID de Venta debe ser un número entero") #Manejo de rrores para el id

            #Abre input para elegir el cliente desde un dorop down menu
            label_cliente = tk.Label(ventana_envio_factura, text="Cliente:")
            label_cliente.pack()
            clientes = [cliente['nombre'] for cliente in sistema.clientes] # Obtener la lista de clientes desde el sistema y crear el menú desplegable
            cliente_var = tk.StringVar(ventana_envio_factura)
            cliente_var.set("")  # Valor inicial vacío
            dropdown_cliente = tk.OptionMenu(ventana_envio_factura, cliente_var, *clientes)
            dropdown_cliente.pack()

            #Abre input para el id de compra
            label_id_venta = tk.Label(ventana_envio_factura, text="ID de Venta:")
            label_id_venta.pack()
            entry_id_venta = tk.Entry(ventana_envio_factura)
            entry_id_venta.pack()

            btn_enviar = tk.Button(ventana_envio_factura, text="Enviar", command=enviar_factura) #Llama a la funcion de arriba
            btn_enviar.pack()

######################################################################################################################################

        #Inicializa la ventana principal
        ventana_principal = tk.Tk()
        ventana_principal.title("Sistema de Gestión Comercial STONKS") #Nombre de la ventana
        ventana_principal.geometry("600x700") #Tamano de la ventana

        #Establece la imagen elegida como fondo de la interfaz
        imagen_fondo = Image.open("Stonks.jpg")
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(ventana_principal, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        #Agrega boton para el registro de usuarios
        btn_registro_usuario = tk.Button(ventana_principal, text="Registrar Usuario", command=mostrar_registro_usuario, width=20, height=2)
        btn_registro_usuario.pack(pady=10)

        #Agrega boton para el registro de clientes
        btn_ingreso_cliente = tk.Button(ventana_principal, text="Registrar Cliente", command=mostrar_ingreso_cliente, width=20, height=2)
        btn_ingreso_cliente.pack(pady=10)

        #Agrega boton para el registro de proveedores
        btn_ingreso_proveedor = tk.Button(ventana_principal, text="Registrar Proveedor", command=mostrar_ingreso_proveedor, width=20, height=2)
        btn_ingreso_proveedor.pack(pady=10)

        #Agrega boton para el IVA
        btn_configuracion_iva = tk.Button(ventana_principal, text="Cálculo de IVA", command=mostrar_configuracion_iva, width=20, height=2)
        btn_configuracion_iva.pack(pady=10)

        #Agrega boton para el registro de productos
        btn_ingreso_producto = tk.Button(ventana_principal, text="Ingresar Producto", command=mostrar_ingreso_producto, width=20, height=2)
        btn_ingreso_producto.pack(pady=10)

        #Agrega boton para el registro de ventas
        btn_registro_venta = tk.Button(ventana_principal, text="Registrar Venta", command=mostrar_registro_venta , width=20, height=2)
        btn_registro_venta.pack(pady=10)

        #Agrega boton para desplegar el inventario de productos
        btn_inventario = tk.Button(ventana_principal, text="Informe de Inventario", command=self.mostrar_inventario, width=20, height=2)
        btn_inventario.pack(pady=10)
        
        #Agrega boton para el informe de ventas
        btn_informe_ventas = tk.Button(ventana_principal, text="Informe de Ventas", command=mostrar_informe_ventas, width=20, height=2)
        btn_informe_ventas.pack(pady=10)

        #Agrega boton para el informe de clientes
        btn_informe_clientes = tk.Button(ventana_principal, text="Informe de Clientes", command=mostrar_informe_clientes, width=20, height=2)
        btn_informe_clientes.pack(pady=10)

        #Agrega boton para el registro de metodos de pago
        btn_registro_metodo_pago = tk.Button(ventana_principal, text="Registrar Método de Pago", command=mostrar_registro_metodo_pago, width=20, height=2)
        btn_registro_metodo_pago.pack(pady=10)

        #Agrega boton para el envio de facturas
        btn_envio_factura = tk.Button(ventana_principal, text="Envío de Factura", command=mostrar_envio_factura, width=20, height=2)
        btn_envio_factura.pack(pady=10)

        ventana_principal.mainloop()

######################################################################################################################################

#Se inicializa el sistema
sistema = SistemaGestionComercial()
sistema.menu_principal()
