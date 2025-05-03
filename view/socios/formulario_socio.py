import flet as ft
import re
from datetime import datetime
from utils.colors import Colores
from utils.alerts import UtilMensajes


class SociosForm:
    def __init__(self, socios_page, titulo, accion, socio=None):
        self.socios_page = socios_page
        self.accion = accion
        self.socio = socio or {}

        # Campos con valor inicial si es edición
        self.campo_control = ft.TextField(
            label="Control",
            value=self.socio.get("numero_control", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=100,
            max_length=2,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        self.campo_nombres = ft.TextField(
            label="Nombres",
            value=self.socio.get("nombres", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=275,
            max_length=30,
            on_change=self.validar_texto,
        )
        self.campo_apellidos = ft.TextField(
            label="Apellidos",
            value=self.socio.get("apellidos", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=275,
            max_length=30,
            on_change=self.validar_texto,
        )
        self.campo_cedula = ft.TextField(
            label="Cédula",
            value=self.socio.get("cedula", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=125,
            max_length=11,
            hint_text="V-/E-",
            on_change=self.validar_cedula,
        )
        self.campo_fecha = ft.TextField(
            label="Fecha Nacimiento",
            value=self.socio.get("fecha_nacimiento", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=140,
            max_length=10,
            hint_text="AAAA-MM-DD",
            on_change=self.validar_fecha_nacimiento,
        )
        self.campo_telefono = ft.TextField(
            label="Teléfono",
            value=self.socio.get("numero_telefono", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=155,
            max_length=15,
            prefix_text="+58 ",
            hint_text="414 1234567",
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        self.campo_direccion = ft.TextField(
            label="Dirección",
            value=self.socio.get("direccion", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=370,
            max_length=30,
            hint_text="Municipio/Urb/Sector/Calle/Casa",
            multiline=True,
        )
        self.campo_rif = ft.TextField(
            label="RIF",
            value=self.socio.get("rif", ""),
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=180,
            max_length=13,
            hint_text="V121233211",
            on_change=self.validar_rif,
            error_style=ft.TextStyle(color="#FF5733"),
        )

        # Botón principal
        boton_guardar = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.SAVE, color=Colores.NEGRO1),
                ft.Text(
                    "Agregar" if accion == "agregar" else "Actualizar",
                    color=Colores.NEGRO1,
                    size=16,
                    weight=ft.FontWeight.BOLD
                )
            ], spacing=5),
            on_click=lambda _: self.guardar_socio(),
            style=ft.ButtonStyle(bgcolor=Colores.AMARILLO1),
        )

        # Contenedor del formulario
        self.formulario = ft.Container(
            content=ft.Column([
                ft.Row([self.campo_nombres, self.campo_apellidos], spacing=15),
                ft.Row([self.campo_control, self.campo_cedula, self.campo_fecha, self.campo_telefono], spacing=15),
                ft.Row([self.campo_direccion, self.campo_rif], spacing=15),
                ft.Row([boton_guardar], alignment=ft.MainAxisAlignment.END)
            ]),
            padding=20,
            border_radius=15,
        )

    def guardar_socio(self):
        try:
            UtilMensajes.mostrar_snack(self.socios_page, "Socio guardado con éxito", tipo="success")
            for campo in [
                self.campo_control, self.campo_nombres, self.campo_apellidos,
                self.campo_cedula, self.campo_fecha, self.campo_telefono,
                self.campo_direccion, self.campo_rif,
            ]:
                campo.value = ""
                campo.error_text = None
                campo.update()
        except Exception as err:
            UtilMensajes.mostrar_snack(self.socios_page, f"Error al guardar: {err}", tipo="error")

    # Validaciones
    def validar_fecha_nacimiento(self, e):
        e.control.error_text = None if Validacion.validar_fecha(e.control.value) else "AAAA-MM-DD"
        e.control.update()

    def validar_cedula(self, e):
        e.control.error_text = None if Validacion.validar_cedula(e.control.value) else "'V-' o 'E-'"
        e.control.update()

    def validar_texto(self, e):
        e.control.error_text = None if Validacion.validar_texto(e.control.value) else "Solo se permiten letras"
        e.control.update()

    def validar_rif(self, e):
        e.control.error_text = None if Validacion.validar_rif(e.control.value) else "Formato RIF inválido"
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
