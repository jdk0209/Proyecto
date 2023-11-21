from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
import customtkinter as ctk
import os
from datetime import datetime
from Modelo.Conexion import ValidarUsuarios

Carpeta_Principal = os.path.dirname("__file__")
Carpeta_Imagenes = os.path.join(Carpeta_Principal, "Vista/Imagenes")

class FrmPrincipal:
    def __init__(self, usuario_actual, controlador):
        self.controlador = controlador
        self.usuario_actual = usuario_actual
        self.ventana_principal = ctk.CTk()
        self.ventana_principal.title("Sistema de reportes hidroeléctrica")
        self.ventana_principal.iconbitmap(os.path.join(Carpeta_Imagenes, "logo.ico"))

        # Calcular dimensiones y ubicación centrada
        ancho_ventana = 1280
        alto_ventana = 720
        ancho_pantalla = self.ventana_principal.winfo_screenwidth()
        alto_pantalla = self.ventana_principal.winfo_screenheight()
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Dimensiones y ubicación de la ventana centrada
        self.ventana_principal.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
        self.ventana_principal.resizable(False, False)

        # Frame para los botones "Consultas", "Reportes" y "Novedades"
        self.frame_botones = ctk.CTkFrame(self.ventana_principal)
        self.frame_botones.pack(side="left", fill="y")

        # Frame para el contenido de las ventanas
        self.frame_ventanas = ctk.CTkFrame(self.ventana_principal)
        self.frame_ventanas.pack(expand=True, fill="both", side="right")
        self.frame_ventanas.grid_propagate(False)
        self.frame_ventanas.grid_columnconfigure(0, weight=1)

        # botones y eventos
        self.btn_Consultas = ctk.CTkButton(self.frame_botones, text="Consultas", command=self.abrir_frm_consultas)
        self.btn_Consultas.pack(fill="x", padx=10, pady=10)

        self.btn_Novedades = ctk.CTkButton(self.frame_botones, text="Novedades", command=self.abrir_frm_novedades)
        self.btn_Novedades.pack(fill="x", padx=10, pady=10)

        self.btn_Reportes = ctk.CTkButton(self.frame_botones, text="Reportes", command=self.abrir_frm_reportes)
        self.btn_Reportes.pack(fill="x", padx=10, pady=10)

        # Etiqueta para la hora y fecha del sistema
        self.etiqueta_hora_fecha = tk.Label(self.frame_botones, text="")
        self.etiqueta_hora_fecha.pack(fill="x", padx=10, pady=10)
        self.actualizar_hora_fecha()

        # Variables para rastrear si las ventanas están abiertas o no
        self.ventana_consultas_abierta = None
        self.ventana_novedades_abierta = None
        self.ventana_reportes_abierta = None
        self.Ent_usuario = None
        self.Ent_Novedad = None

    def cargar_usuarios_en_etiqueta(self, etiqueta):
        validar_usuarios = ValidarUsuarios()
        usuarios = validar_usuarios.obtener_usuarios()

        etiqueta.set("")

        if usuarios:
            etiqueta.set(usuarios[0])
            
    def actualizar_hora_fecha(self):
        ahora = datetime.now()
        hora_fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
        self.etiqueta_hora_fecha.config(text=hora_fecha)
        self.ventana_principal.after(1000, self.actualizar_hora_fecha)

    # Ventanas Secundarias
    def abrir_frm_consultas(self):
        self.cerrar_ventanas_abiertas()
        self.ventana_consultas_abierta = ctk.CTkFrame(self.frame_ventanas)
        self.ventana_consultas_abierta.pack(expand=True, fill="both")

        # Agregar widgets a self.ventana_consultas_abierta
        label = ctk.CTkLabel(self.ventana_consultas_abierta, text="Consultas", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(padx=10, pady=10)
        
        Label_Hora_Fercha = ctk.CTkLabel(self.ventana_consultas_abierta, text="Fecha Inicial", font=ctk.CTkFont(size=12))
        Label_Hora_Fercha.place(x=70,y=70)
        
        Label_Hora_Fercha3 = ctk.CTkLabel(self.ventana_consultas_abierta, text="Fecha Final", font=ctk.CTkFont(size=12))
        Label_Hora_Fercha3.place(x=500,y=70)

        # Botones de accion 
        btn_atras = ctk.CTkButton(self.ventana_consultas_abierta, text="Atrás", command=self.cerrar_frm_consultas)
        btn_atras.place(x=50, y=150)
        
        btn_Consulta = ctk.CTkButton(self.ventana_consultas_abierta, text="Generar")
        btn_Consulta.place(x=930, y=150)

    def cerrar_frm_consultas(self):
        if self.ventana_consultas_abierta:
            self.ventana_consultas_abierta.destroy()
            self.ventana_consultas_abierta = None


    def abrir_frm_novedades(self):
        self.cerrar_ventanas_abiertas()
        self.ventana_novedades_abierta = ctk.CTkFrame(self.frame_ventanas)
        self.ventana_novedades_abierta.pack(expand=True, fill="both")

        # Agregar widgets a self.ventana_novedades_abierta
        label = ctk.CTkLabel(self.ventana_novedades_abierta, text="Novedades", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(padx=10, pady=10)

        Lbl_Nombre_Usuario = ctk.CTkLabel(self.ventana_novedades_abierta, text="Usuario:", font=ctk.CTkFont(size=12))
        Lbl_Nombre_Usuario.place(x=90, y=70)

        lbl_novedad = ctk.CTkLabel(self.ventana_novedades_abierta, text="Describa la Novedad:", font=ctk.CTkFont(size=12))
        lbl_novedad.place(x=450, y=70)

        # Verifica si Ent_usuario es None y, en ese caso, inicialízalo
        if self.Ent_usuario is None:
            self.Ent_usuario = tk.StringVar()

        self.cargar_usuarios_en_etiqueta(self.Ent_usuario)

        usuario_actual = self.controlador.obtener_usuario_actual()

        lbl_usuario_actual = ctk.CTkLabel(self.ventana_novedades_abierta, text=f"Usuario: {usuario_actual}",
                                        font=ctk.CTkFont(size=12))
        lbl_usuario_actual.place(x=90, y=70)

        self.Ent_Novedad = ctk.CTkTextbox(self.ventana_novedades_abierta, width=280, height=150)
        self.Ent_Novedad.place(x=570, y=70)

        # Botones de acción
        btn_atras = ctk.CTkButton(self.ventana_novedades_abierta, text="Atrás", command=self.cerrar_frm_novedades)
        btn_atras.place(x=50, y=250)

        btn_novedades = ctk.CTkButton(self.ventana_novedades_abierta, text="Guardar", command=self.guardar_novedad)
        btn_novedades.place(x=710, y=250)
        
        # Obtener las novedades desde el controlador
        novedades = self.controlador.obtener_todas_las_novedades()
        
        # Agregar Treeview para mostrar las novedades
        columns = ("Codigo","Usuario", "Novedad", "Fecha")
        self.treeview_novedades = ttk.Treeview(self.ventana_novedades_abierta, columns=columns, show="headings")
        
        # Configurar las columnas
        for col in columns:
            self.treeview_novedades.heading(col, text=col)

        # Insertar los datos de las novedades en el Treeview
        for novedad in novedades:
            self.treeview_novedades.insert("", "end", values=novedad)

        # Mostrar el Treeview
        self.treeview_novedades.place(x=50, y=300)
        
    def cargar_novedades_en_treeview(self):
        # Obtener todas las novedades desde el controlador (ajusta esto según tu implementación)
        novedades = self.controlador.obtener_todas_las_novedades()

        # Limpiar el Treeview antes de cargar nuevos datos
        for item in self.treeview_novedades.get_children():
            self.treeview_novedades.delete(item)

        # Cargar los nuevos datos en el Treeview
        for novedad in novedades:
            self.treeview_novedades.insert("", "end", values=(novedad["Usuario"], novedad["Novedad"], novedad["Fecha"]))

    def guardar_novedad(self):
        novedad = self.Ent_Novedad.get("1.0", ctk.END)

        if not novedad.strip():
            messagebox.showerror("Error", "Por favor, complete la novedad.")
            return

        try:
            usuario_actual = self.controlador.obtener_usuario_actual()
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.controlador.insertar_novedad(usuario_actual, novedad,fecha_actual)
            messagebox.showinfo("Éxito", "Novedad guardada exitosamente.")
            
            # Borrar el contenido del campo Ent_Novedad
            self.Ent_Novedad.delete("1.0", ctk.END)   
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar la novedad: {str(e)}")
            
            # Borrar el contenido del campo Ent_Novedad
            self.Ent_Novedad.delete("1.0", ctk.END)   

    def cerrar_frm_novedades(self):
        if self.ventana_novedades_abierta:
            self.ventana_novedades_abierta.destroy()
            self.ventana_novedades_abierta = None
    
    def abrir_frm_reportes(self):
        self.cerrar_ventanas_abiertas()
        self.ventana_reportes_abierta = ctk.CTkFrame(self.frame_ventanas)
        self.ventana_reportes_abierta.pack(expand=True, fill="both")

        # Agregar widgets a self.ventana_reportes_abierta
        label = ctk.CTkLabel(self.ventana_reportes_abierta, text="Reportes", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(padx=10, pady=10)

        Label_Hora_Fercha1 = ctk.CTkLabel(self.ventana_reportes_abierta, text="Fecha Inicial: ", font=ctk.CTkFont(size=12))
        Label_Hora_Fercha1.place(x=70, y=70)
        
        # Selector de fecha inicial
        fecha_inicial_selector = DateEntry(self.ventana_reportes_abierta)
        fecha_inicial_selector.place(x=150, y=70)

        Label_Hora_Fercha2 = ctk.CTkLabel(self.ventana_reportes_abierta, text="Fecha Final: ", font=ctk.CTkFont(size=12))
        Label_Hora_Fercha2.place(x=500, y=70)
        
        # Selector de fecha final
        fecha_final_selector = DateEntry(self.ventana_reportes_abierta)
        fecha_final_selector.place(x=575, y=70)

        # Botones de acción
        btn_atras = ctk.CTkButton(self.ventana_reportes_abierta, text="Atrás", command=self.cerrar_frm_reportes)
        btn_atras.place(x=50, y=150)

        btn_Reportes = ctk.CTkButton(self.ventana_reportes_abierta, text="Generar", command=lambda: self.generar_reporte(fecha_inicial_selector.get(), fecha_final_selector.get()))
        btn_Reportes.place(x=930, y=150)

        btn_Imprimir = ctk.CTkButton(self.ventana_reportes_abierta, text="Imprimir", command=self.btn_Imprimir)
        btn_Imprimir.place(x=770, y=150)
        
         # Obtener las novedades desde el controlador
        reportes = self.controlador.obtener_reportes()
        
        # Agregar Treeview para mostrar las novedades
        columns = ("CodigoInforme","Corriente", "Voltaje", "Temperatura")
        self.treeview_reportes = ttk.Treeview(self.ventana_reportes_abierta, columns=columns, show="headings")
        
        # Configurar las columnas
        for col in columns:
            self.treeview_reportes.heading(col, text=col)

        # Insertar los datos de las novedades en el Treeview
        for report in reportes:
            self.treeview_reportes.insert("", "end", values=report)

        # Mostrar el Treeview
        self.treeview_reportes.place(x=50, y=300)
        
    def cargar_reportes_en_treeview(self):
        # Obtener todas las novedades desde el controlador (ajusta esto según tu implementación)
        reportes = self.controlador.obtener_reportes()

        # Limpiar el Treeview antes de cargar nuevos datos
        for item in self.treeview_reportes.get_children():
            self.treeview_reportes.delete(item)

        # Cargar los nuevos datos en el Treeview
        for report in reportes:
            self.treeview_reportes.insert("", "end", values=(report["CodigoInforme"], report["Corriente"], report["Voltaje"], report["Temperatura"]))

        # Método para generar el reporte con las fechas seleccionadas
    def generar_reporte(self, fecha_inicial, fecha_final):
        # Aquí puedes utilizar las fechas seleccionadas para generar tu reporte
        print(f"Fecha Inicial: {fecha_inicial}")
        print(f"Fecha Final: {fecha_final}")
        
    def btn_Imprimir(self):
        # Obtén los informes desde el controlador
        informes = self.controlador.obtener_informes()

        # Llama al método en el controlador para generar el PDF
        self.controlador.generar_pdf_informes(informes, "informes")

    def cerrar_frm_reportes(self):
        if self.ventana_reportes_abierta:
            self.ventana_reportes_abierta.destroy()
            self.ventana_reportes_abierta = None

    def cerrar_ventanas_abiertas(self):
        if self.ventana_consultas_abierta:
            self.ventana_consultas_abierta.destroy()
            self.ventana_consultas_abierta = None
        elif self.ventana_novedades_abierta:
            self.ventana_novedades_abierta.destroy()
            self.ventana_novedades_abierta = None
        elif self.ventana_reportes_abierta:
            self.ventana_reportes_abierta.destroy()
            self.ventana_reportes_abierta = None
            
    def mostrar(self):
        self.ventana_principal.deiconify()

    def iniciar_aplicacion(self):
        self.ventana_principal.mainloop()