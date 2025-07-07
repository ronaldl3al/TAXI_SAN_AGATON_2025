import flet as ft
import re
from datetime import datetime
from utils.colors import Colores
from utils.alerts import UtilMensajes

class AvancesForm:
    def __init__(self, avances_page, titulo: str, accion: str, avance: dict = None):
        self.avances_page = avances_page
        self.accion = accion
        self.avance = avance or {}

        # Control
        self.campo_control = ft.TextField(
            label="Control",
            value=self.avance.get("control", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=120,
            max_length=5,
            input_filter=ft.NumbersOnlyInputFilter(),
            hover_color=Colores.GRIS00
        )

        # Nombre
        self.campo_nombre = ft.TextField(
            label="Nombre",
            value=self.avance.get("nombre", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270,
            max_length=30,
            on_change=self.validar_texto,
            hover_color=Colores.GRIS00
        )

        # Apellido
        self.campo_apellido = ft.TextField(
            label="Apellido",
            value=self.avance.get("apellido", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270,
            max_length=30,
            on_change=self.validar_texto,
            hover_color=Colores.GRIS00
        )

        # Fecha de Nacimiento
        self.campo_fecha = ft.TextField(
            label="F. Nacimiento",
            value=self.avance.get("fecha_nacimiento", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=200,
            max_length=10,
            hint_text="AAAA-MM-DD",
            on_change=self.validar_fecha,
            hover_color=Colores.GRIS00
        )

        # RIF
        self.campo_rif = ft.TextField(
            label="RIF",
            value=self.avance.get("rif", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=205,
            max_length=13,
            hint_text="V123456789",
            on_change=self.validar_rif,
            hover_color=Colores.GRIS00
        )

        # Cédula Avance
        self.campo_cedula_avance = ft.TextField(
            label="Cédula Avance",
            value=self.avance.get("cedula_avance", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270,
            max_length=11,
            hint_text="V-/E-12345678",
            on_change=self.validar_cedula_avance,
            hover_color=Colores.GRIS00
        )

        # Teléfono
        self.campo_telefono = ft.TextField(
            label="Teléfono",
            value=self.avance.get("telefono", ""),
            border_radius=0,
            border_color=ft.colors.TRANSPARENT,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270,
            max_length=15,
            prefix_text="+58 ",
            input_filter=ft.NumbersOnlyInputFilter(),
            hover_color=Colores.GRIS00
        )

        # Botón Guardar
        self.boton_guardar = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.SAVE, color=Colores.NEGRO1),
                ft.Text("Agregar" if accion=="agregar" else "Actualizar",
                        color=Colores.NEGRO1, size=16, weight=ft.FontWeight.BOLD)
            ], spacing=5),
            on_click=lambda _: self.guardar_avance(),
            style=ft.ButtonStyle(
                bgcolor=Colores.AMARILLO1,
                shape=ft.RoundedRectangleBorder(radius=0)
            )
        )

        # Contenedor del formulario
        self.formulario = ft.Container(
            content=ft.Column([
                ft.Row([self.campo_nombre, self.campo_apellido], spacing=15),
                ft.Row([self.campo_control,self.campo_fecha, self.campo_rif], spacing=15),
                ft.Row([self.campo_telefono, self.campo_cedula_avance], spacing=15),
                ft.Row([self.boton_guardar], alignment=ft.MainAxisAlignment.END)
            ]),
            padding=20,
            border_radius=0,
        )

    def guardar_avance(self):
        try:
            UtilMensajes.mostrar_snack(self.avances_page, "Avance guardado con éxito", tipo="success")
            for campo in [
                self.campo_control, self.campo_nombre, self.campo_apellido,
                self.campo_fecha, self.campo_rif, self.campo_cedula_avance,
                self.campo_telefono
            ]:
                campo.value = ""
                campo.error_text = None
                campo.update()
        except Exception as err:
            UtilMensajes.mostrar_snack(self.avances_page, f"Error al guardar: {err}", tipo="error")

    # Validaciones
    def validar_texto(self, e):
        e.control.error_text = None if ValidacionAvance.validar_texto(e.control.value) else "Solo letras"
        e.control.update()

    def validar_fecha(self, e):
        e.control.error_text = None if ValidacionAvance.validar_fecha(e.control.value) else "AAAA-MM-DD"
        e.control.update()

    def validar_rif(self, e):
        e.control.error_text = None if ValidacionAvance.validar_rif(e.control.value) else "Formato RIF inválido"
        e.control.update()

    def validar_cedula_avance(self, e):
        e.control.error_text = None if ValidacionAvance.validar_cedula(e.control.value) else "'V-' o 'E-'"
        e.control.update()

class ValidacionAvance:
    @staticmethod
    def validar_texto(texto: str) -> bool:
        return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', texto))

    @staticmethod
    def validar_fecha(fecha: str) -> bool:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except:
            return False

    @staticmethod
    def validar_rif(rif: str) -> bool:
        return bool(re.match(r'^[VEJPG]\d{7,10}$', rif))

    @staticmethod
    def validar_cedula(cedula: str) -> bool:
        return bool(re.match(r'^[VE]-\d{7,9}$', cedula))

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        return telefono.isdigit()

