import flet as ft
import re
from datetime import datetime
from utils.colors import Colores
from utils.alerts import UtilMensajes

class SancionesForm:
    def __init__(self, sanciones_page, titulo: str, accion: str, sancion: dict = None):
        self.sanciones_page = sanciones_page
        self.accion = accion
        self.sancion = sancion or {}

        # Cédula del Socio
        self.campo_cedula_socio = ft.TextField(
            label="Cédula Socio",
            value=self.sancion.get("cedula_socio", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=205, max_length=11,
            hint_text="V-/E-12345678",
            on_change=self.validar_cedula_socio,
            hover_color=Colores.GRIS00,
            border_color=ft.colors.TRANSPARENT
        )
        # Nombre
        self.campo_nombre = ft.TextField(
            label="Nombre",
            value=self.sancion.get("nombre", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            border_color=ft.colors.TRANSPARENT,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270, max_length=30,
            on_change=self.validar_texto,
            hover_color=Colores.GRIS00
        )
        # Apellido
        self.campo_apellido = ft.TextField(
            label="Apellido",
            value=self.sancion.get("apellido", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=270, max_length=30,
            on_change=self.validar_texto,
            border_color=ft.colors.TRANSPARENT,
            hover_color=Colores.GRIS00
        )
        # Inicio de Sanción
        self.campo_inicio = ft.TextField(
            label="Inicio Sanción",
            value=self.sancion.get("inicio_sancion", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=160, max_length=10,
            hint_text="YYYY-MM-DD",
            on_change=self.validar_fecha,
            border_color=ft.colors.TRANSPARENT,
            hover_color=Colores.GRIS00
        )
        # Fin de Sanción
        self.campo_fin = ft.TextField(
            label="Fin Sanción",
            value=self.sancion.get("fin_sancion", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=160, max_length=10,
            hint_text="YYYY-MM-DD",
            on_change=self.validar_fecha,
            border_color=ft.colors.TRANSPARENT,
            hover_color=Colores.GRIS00
        )
        # Monto
        self.campo_monto = ft.TextField(
            label="Monto",
            value=str(self.sancion.get("monto", "")),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=120,
            input_filter=ft.TextOnlyInputFilter(),
            border_color=ft.colors.TRANSPARENT,
            on_change=self.validar_numero,
            hover_color=Colores.GRIS00
        )
        # Motivo
        self.campo_motivo = ft.TextField(
            label="Motivo",
            value=self.sancion.get("motivo", ""),
            border_radius=0, bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            width=420, max_length=100,
            on_change=self.validar_texto,
            border_color=ft.colors.TRANSPARENT,
            hover_color=Colores.GRIS00
        )

        # Botón Guardar
        texto_btn = "Agregar" if accion == "agregar" else "Actualizar"
        boton_guardar = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.SAVE, color=Colores.NEGRO1),
                ft.Text(texto_btn, color=Colores.NEGRO1, size=16, weight=ft.FontWeight.BOLD)
            ], spacing=5),
            on_click=lambda _: self.guardar_sancion(),
            style=ft.ButtonStyle(
                bgcolor=Colores.AMARILLO1,
                shape=ft.RoundedRectangleBorder(radius=0)
            )
        )

        # Ensamblar formulario
        self.formulario = ft.Container(
            padding=20,
            border_radius=0,
            content=ft.Column([
                ft.Row([self.campo_nombre, self.campo_apellido], spacing=15),
                ft.Row([self.campo_cedula_socio, self.campo_inicio, self.campo_fin], spacing=15),
                ft.Row([self.campo_monto, self.campo_motivo], spacing=15),
                ft.Row([boton_guardar], alignment=ft.MainAxisAlignment.END),
            ])
        )

    def guardar_sancion(self):
        try:
            UtilMensajes.mostrar_snack(self.sanciones_page, "Sanción guardada con éxito", tipo="success")
            for campo in [
                self.campo_cedula_socio, self.campo_nombre, self.campo_apellido,
                self.campo_inicio, self.campo_fin, self.campo_monto, self.campo_motivo
            ]:
                campo.value = ""
                campo.error_text = None
                campo.update()
        except Exception as err:
            UtilMensajes.mostrar_snack(self.sanciones_page, f"Error: {err}", tipo="error")

    # Validaciones
    def validar_cedula_socio(self, e):
        e.control.error_text = None if re.match(r'^[VE]-\d{7,9}$', e.control.value) else "'V-' o 'E-'"
        e.control.update()

    def validar_texto(self, e):
        e.control.error_text = None if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', e.control.value) else "Solo letras"
        e.control.update()

    def validar_fecha(self, e):
        try:
            datetime.strptime(e.control.value, "%Y-%m-%d")
            e.control.error_text = None
        except:
            e.control.error_text = "Formato YYYY-MM-DD"
        e.control.update()

    def validar_numero(self, e):
        try:
            float(e.control.value)
            e.control.error_text = None
        except:
            e.control.error_text = "Número inválido"
        e.control.update()
