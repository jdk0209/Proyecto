import sqlite3
from datetime import datetime

class ValidarUsuarios:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDatos")
        self.cursor = self.conexion.cursor()

    def validar_credenciales(self, usuario, contraseña):
        self.cursor.execute(
            "SELECT * FROM Usuarios WHERE CodigoID = ? AND Contraseña = ?", (usuario, contraseña))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def obtener_usuarios(self):
        self.cursor.execute("SELECT CodigoID FROM Usuarios")
        usuarios = [row[0] for row in self.cursor.fetchall()]
        return usuarios
    
    def insertar_novedad(self, usuario, novedad, fecha_actual):
        self.cursor.execute("SELECT Cedula FROM Usuarios WHERE CodigoID = ?", (usuario,))
        id_usuario = self.cursor.fetchone()[0]

        # Insertar la novedad con la información del usuario y la fecha
        self.cursor.execute(
            "INSERT INTO Novedades (Usuario, Novedad, Fecha, frk_usuario) VALUES (?, ?, ?, ?)",
            (usuario, novedad, fecha_actual, id_usuario)
        )
        self.conexion.commit()
        
    def obtener_todas_las_novedades(self):
        self.cursor.execute("SELECT * FROM Novedades")
        novedades = self.cursor.fetchall()
        return novedades
    
    def obtener_reportes(self):
        self.cursor.execute("SELECT * FROM Informes")
        reportes = self.cursor.fetchall()
        return reportes

        
    def cerrar_conexion(self):
        self.conexion.close()