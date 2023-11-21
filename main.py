import customtkinter as ctk
from Controlador.Controlador import Controlador
from Vista.FrmLogin import Login
from Vista.FrmPrincipal import FrmPrincipal

if __name__ == "__main__":
    controlador = Controlador()
    vista = Login(controlador)

    # Crear una instancia de FrmPrincipal y asociarla con la ventana principal
    ventana_principal = ctk.CTk()
    frm_principal = FrmPrincipal(ventana_principal, controlador)

    controlador.vista = vista
    controlador.frm_principal = frm_principal

    vista.iniciar_aplicacion()

