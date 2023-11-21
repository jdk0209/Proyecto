import customtkinter as ctk
from Vista.FrmPrincipal import FrmPrincipal
from tkinter import messagebox
from Modelo.Conexion import ValidarUsuarios
import os

Carpeta_Principal = os.path.dirname("__file__")
Carpeta_Imagenes = os.path.join(Carpeta_Principal, "Vista\Imagenes")


class CrearUsuario:
    def __init__(self, controlador, ventana_anterior):
        self.controlador = controlador
        self.ventana_anterior = ventana_anterior
        self.ventana_crear_usuario = ctk.CTk()
        self.ventana_crear_usuario.title("Crear Usuario")

        # Campos de texto y etiquetas
        self.etiqueta_nombre = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Nombre:")
        self.etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entrada_nombre = ctk.CTkEntry(self.ventana_crear_usuario)
        self.entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta_apellido = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Apellido:")
        self.etiqueta_apellido.grid(row=1, column=0, padx=10, pady=10)
        self.entrada_apellido = ctk.CTkEntry(self.ventana_crear_usuario)
        self.entrada_apellido.grid(row=1, column=1, padx=10, pady=10)

        self.etiqueta_cedula = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Cedula:")
        self.etiqueta_cedula.grid(row=2, column=0, padx=10, pady=10)
        self.entrada_cedula = ctk.CTkEntry(self.ventana_crear_usuario)
        self.entrada_cedula.grid(row=2, column=1, padx=10, pady=10)

        self.etiqueta_codigo_id = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Codigo ID:")
        self.etiqueta_codigo_id.grid(row=3, column=0, padx=10, pady=10)
        self.entrada_codigo_id = ctk.CTkEntry(self.ventana_crear_usuario)
        self.entrada_codigo_id.grid(row=3, column=1, padx=10, pady=10)

        self.etiqueta_contraseña = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Contraseña:")
        self.etiqueta_contraseña.grid(row=4, column=0, padx=10, pady=10)
        self.entrada_contraseña = ctk.CTkEntry(
            self.ventana_crear_usuario, show="*")
        self.entrada_contraseña.grid(row=4, column=1, padx=10, pady=10)

        self.etiqueta_confirmar_contraseña = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Confirmar Contraseña:")
        self.etiqueta_confirmar_contraseña.grid(row=5, column=0, padx=10, pady=10)
        self.entrada_confirmar_contraseña = ctk.CTkEntry(
            self.ventana_crear_usuario, show="*")
        self.entrada_confirmar_contraseña.grid(row=5, column=1, padx=10, pady=10)

        self.etiqueta_cargo = ctk.CTkLabel(
            self.ventana_crear_usuario, text="Cargo:")
        self.etiqueta_cargo.grid(row=6, column=0, padx=10, pady=10)
        opciones_cargo = ["Cargo 1", "Cargo 2", "Cargo 3"]  # Puedes cambiar las opciones según tus necesidades
        self.combo_cargo = ctk.CTkComboBox(self.ventana_crear_usuario, values=opciones_cargo)
        self.combo_cargo.grid(row=6, column=1, padx=10, pady=10)

        # Botón para guardar
        self.boton_guardar = ctk.CTkButton(
            self.ventana_crear_usuario, text="Guardar", command=self.guardar_usuario)
        self.boton_guardar.grid(row=7, column=0, columnspan=2, pady=20)

    def guardar_usuario(self):
        # Aquí puedes agregar la lógica para guardar el usuario en la base de datos
        # Puedes obtener los valores de los campos usando self.entrada_nombre.get(), self.entrada_apellido.get(), etc.

        messagebox.showinfo("Éxito", "Usuario guardado correctamente")
        self.ventana_crear_usuario.destroy()  # Cierra la ventana de creación de usuario
        self.ventana_anterior.deiconify()  # Muestra la ventana anterior


    def mostrar(self):
        self.ventana_crear_usuario.deiconify()  # Muestra la ventana


class Login:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana_login = ctk.CTk()
        self.ventana_login.title("Login")
        self.ventana_login.iconbitmap(
            os.path.join(Carpeta_Imagenes, "logo.ico"))

        # Calcular dimensiones y ubicación centrada
        ancho_ventana = 590
        alto_ventana = 320
        ancho_pantalla = self.ventana_login.winfo_screenwidth()
        alto_pantalla = self.ventana_login.winfo_screenheight()
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Dimensiones y ubicación de la ventana centrada
        self.ventana_login.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
        self.ventana_login.resizable(False, False)

        # Canvas para mostrar imagen (ocupará la mitad izquierda de la ventana)
        self.canvas_imagen = ctk.CTkCanvas(
            self.ventana_login, width=ancho_ventana // 2, height=alto_ventana)
        self.canvas_imagen.place(x=0, y=0)

        # Se crean y posicionan botones, etiquetas y campos de texto
        self.etiqueta_Login = ctk.CTkLabel(
            self.ventana_login, text="Iniciar Sesion", font=ctk.CTkFont(size=30, weight="bold"))
        self.etiqueta_Login.place(x=350, y=40)

        self.etiqueta_usuario = ctk.CTkLabel(
            self.ventana_login, text="Usuario:")
        self.etiqueta_usuario.place(x=370, y=80)
        self.entrada_usuario = ctk.CTkEntry(self.ventana_login)
        self.entrada_usuario.place(x=370, y=100)

        self.etiqueta_contraseña = ctk.CTkLabel(
            self.ventana_login, text="Contraseña:")
        self.etiqueta_contraseña.place(x=370, y=130)
        self.entrada_contraseña = ctk.CTkEntry(self.ventana_login, show="*")
        self.entrada_contraseña.place(x=370, y=150)

        self.boton_inicio_sesion = ctk.CTkButton(
            self.ventana_login, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_inicio_sesion.place(x=370, y=190)

        self.boton_crear_ususario = ctk.CTkButton(
            self.ventana_login, text="Crear Usuario", command=self.abrir_ventana_crear_usuario)
        self.boton_crear_ususario.place(x=370, y=230)

        self.etiqueta_recuperar_contra = ctk.CTkLabel(
            self.ventana_login, text="¿Olvidaste tu contraseña?")
        self.etiqueta_recuperar_contra.place(x=365,  y=260)

        # Ventana principal (inicialmente oculta)
        self.ventana_principal = None

    def abrir_ventana_crear_usuario(self):
        respuesta = messagebox.askquestion("Crear Usuario", "¿Desea crear un nuevo usuario?")

        if respuesta == 'yes':
            # Crear la ventana de creación de usuario
            ventana_crear_usuario = CrearUsuario(self.controlador, self.ventana_login)

            # Ocultar la ventana de inicio de sesión
            self.ventana_login.withdraw()

            # Mostrar la ventana de creación de usuario
            ventana_crear_usuario.mostrar()

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        resultado = self.controlador.iniciar_sesion(usuario, contraseña)

        if resultado:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
            self.abrir_ventana_principal()  # Abre la ventana principal
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

            # Borrar el contenido de los campos de usuario y contraseña
            self.entrada_usuario.delete(0, ctk.END)
            self.entrada_contraseña.delete(0, ctk.END)

        # instancia para llamar el Frm Principal
    def abrir_ventana_principal(self):
        if self.controlador.frm_principal is None:
            self.controlador.frm_principal = FrmPrincipal(self.ventana_principal, self.controlador)
        self.controlador.frm_principal.mostrar()
            
    def iniciar_aplicacion(self):
        self.ventana_login.mainloop()

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar_aplicacion()
