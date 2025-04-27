
import flet as ft
import re
from datetime import datetime
from utils.colors import Colores

class SociosForm:
    def __init__(self, socios_page, titulo, accion, socio=None):
        self.socios_page = socios_page
        self.accion = accion
        self.formulario = self.formulario_socio(titulo, accion, socio)

    def formulario_socio(self, titulo, accion, socio=None):
        control = ft.TextField(
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            focused_border_color=Colores.AMARILLO1, 
            label="Control", 
            max_length=2, 
            width=100, 
            input_filter=ft.NumbersOnlyInputFilter(), 
           )
        nombres = ft.TextField(
            border_radius=5,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1, 
            label="Nombres",
            width=275,  
            max_length=30, 
            on_change=self.validar_texto
        )
        apellidos = ft.TextField(
            border_radius=5, 
            border_color=Colores.BLANCO, 
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1, 
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Apellidos", 
            width=275, 
            max_length=30, 
            on_change=self.validar_texto
        )
        cedula = ft.TextField(
            border_radius=5,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1, 
            label="Cédula", 
            max_length=11, 
            width=125, 
            hint_text="V-/E-", 
            on_change=self.validar_cedula
        )
        telefono = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            focused_border_color=Colores.AMARILLO1, 
            label="Teléfono", 
            max_length=15, 
            width=155, 
            prefix_text="+58 ", 
            input_filter=ft.NumbersOnlyInputFilter(), 
            hint_text="414 1234567", 
            )
        direccion = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Dirección", 
            width=370, 
            max_length=50, 
            hint_text="Municipio/Urb/Sector/Calle/Casa", 
            multiline=True)
        rif = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,  # Cambiar el color del borde enfocado
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="RIF", 
            width=180, 
            max_length=13, 
            on_change=self.validar_rif,
            hint_text="V121233211",
            error_style=ft.TextStyle(color="#FF5733"),  # Cambiar el color del texto de error
        )
        fecha_nacimiento = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Fecha Nacimiento", 
            max_length=10, 
            width=140, 
            hint_text="AAAA-MM-DD", 
            on_change=self.validar_fecha_nacimiento
        )

        formulario = ft.Container(
            content=ft.Column([
                ft.Row([nombres, apellidos], spacing=15),
                ft.Row([control, cedula, fecha_nacimiento, telefono], spacing=15),
                ft.Row([direccion, rif], spacing=15),
                ft.Row([
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon(ft.icons.SAVE, color=Colores.NEGRO1),
                                        ft.Text("Agregar", color=Colores.NEGRO1, size=16, weight=ft.FontWeight.BOLD)],
                                    spacing=5),
                        on_click=lambda _: self.guardar_socio(cedula, nombres, apellidos, direccion, telefono, control, rif, fecha_nacimiento),
                        style=ft.ButtonStyle(bgcolor=Colores.AMARILLO1)
                    )
                ], alignment=ft.MainAxisAlignment.END)
            ]),
            padding=20,
            border_radius=15,
        )
        return formulario

    # Métodos de validación de datos del formulario
    def validar_fecha_nacimiento(self, e):
        if Validacion.validar_fecha(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "AAAA-MM-DD"
            e.control.update()

    def validar_cedula(self, e):
        if Validacion.validar_cedula(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "'V-' o 'E-'"
            e.control.update()

    def validar_texto(self, e):
        if Validacion.validar_texto(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "Solo se permiten letras"
            e.control.update()

    def validar_rif(self, e):
        if Validacion.validar_rif(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "Formato RIF inválido"
            e.control.update()
class Validacion:
    @staticmethod
    def validar_fecha(fecha):
        if isinstance(fecha, datetime):
            fecha = fecha.strftime('%Y-%m-%d')
        patron = r'^\d{4}-\d{2}-\d{2}$'
        return re.match(patron, fecha) is not None

    @staticmethod
    def validar_cedula(cedula):
        patron = r'^[VE]-\d{7,9}$'
        return re.match(patron, cedula) is not None

    @staticmethod
    def validar_texto(texto):
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        return re.match(patron, texto) is not None


    @staticmethod
    def validar_rif(rif):
        patron = r'^[VEJPG]\d{7,10}$'
        return re.match(patron, rif) is not None
