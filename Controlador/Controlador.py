from tkinter import messagebox
from Modelo.Conexion import ValidarUsuarios
from Vista.FrmLogin import Login
from Vista.FrmPrincipal import FrmPrincipal 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import os 

class Controlador:
    def __init__(self):
        self.Modelo = ValidarUsuarios()
        self.VistaLogin = Login(self)
        self.VistaPrincipal = None  # Aún no se crea la ventana principal

    def iniciar_sesion(self, usuario, contraseña):
        # Otras lógicas de inicio de sesión
        if self.Modelo.validar_credenciales(usuario, contraseña):
            self.usuario_actual = usuario
            self.contraseña_actual = contraseña
            return True
        else:
            return False

    def abrir_ventana_principal(self, usuario):
        # Crea la ventana principal y pasa el usuario y el controlador
        self.VistaPrincipal = FrmPrincipal(usuario, self)
        self.VistaPrincipal.iniciar_aplicacion()

    def ejecutar_aplicacion(self):
        self.VistaLogin.iniciar_aplicacion()

    def cargar_usuarios_en_etiqueta(self):
        # Llama al método cargar_usuarios en la ventana principal
        if self.VistaPrincipal:
            self.VistaPrincipal.cargar_usuarios()
            
    def insertar_novedad(self, usuario_actual, novedad, fecha_actual,):
        usuario_actual = self.obtener_usuario_actual()
        self.Modelo.insertar_novedad(usuario_actual, novedad, fecha_actual,)

    def obtener_usuario_actual(self):
        return self.usuario_actual
    
    def obtener_todas_las_novedades(self):
        # Realiza una consulta a la base de datos para obtener todas las novedades
        novedades = self.Modelo.obtener_todas_las_novedades()
        return novedades
    
    def obtener_reportes(self):
        reportes = self.Modelo.obtener_reportes()
        return reportes
    
    def obtener_informes(self):
        # Realiza una consulta a la base de datos para obtener los informes
        informes = self.Modelo.obtener_reportes()
        return informes
    
    def generar_pdf_informes(self, informes, nombre_archivo):
        documentos_path = os.path.expanduser("~\\Documents")
        pdf_path = os.path.join(documentos_path, f"{nombre_archivo}.pdf")
        
        try:
            # Crear el objeto de lienzo (canvas)
            c = SimpleDocTemplate(pdf_path, pagesize=letter)

            # Configurar el título
            titulo = "Informe de Datos"
            styles = getSampleStyleSheet()
            c_title = styles["Title"]

            # Agregar el título al PDF
            c_title.fontName = "Helvetica-Bold"
            c_title.fontSize = 16
            c_title.alignment = 1  # Alineación al centro
            c_title.textColor = colors.black
            c_title.leading = 20

            titulo_para = Paragraph(titulo, c_title)
            contenido = [titulo_para]

            # Datos para la tabla
            encabezados = ["Corriente", "Voltaje", "Temperatura"]
            datos_tabla = [[informe["Corriente"], informe["Voltaje"], informe["Temperatura"]] for informe in informes]

            # Crear la tabla
            tabla = Table([encabezados] + datos_tabla)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ]))

            contenido.append(tabla)

            # Construir el PDF con el contenido
            c.build(contenido)

            # Mostrar messagebox con el mensaje de éxito
            messagebox.showinfo("Éxito", "PDF creado y exportado satisfactoriamente.")

        except Exception as e:
            print(f"Error al crear el PDF: {e}")

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar_aplicacion()
