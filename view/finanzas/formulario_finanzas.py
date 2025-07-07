import flet as ft
import re
from datetime import datetime
from utils.colors import Colores
from utils.alerts import UtilMensajes

class FinanzasForm:
    def __init__(self, finanzas_page, titulo: str, accion: str, finanza: dict = None):
        self.finanzas_page = finanzas_page
        self.accion = accion
        self.finanza = finanza or {}

        # Número de Control
        self.campo_control = ft.TextField(
            label="Número de Control",
            value=self.finanza.get("control", ""),
            width=150,
            max_length=2,
            input_filter=ft.NumbersOnlyInputFilter(),
            border_radius=0,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            on_change=self.validar_control,
            border_color=ft.colors.TRANSPARENT,
            hover_color=Colores.GRIS00

        )

        # Cédula
        self.campo_cedula = ft.TextField(
            label="Cédula",
            value=self.finanza.get("cedula", ""),
            width=200,
            max_length=11,
            hint_text="V-/E-12345678",
            border_radius=0,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            border_color=ft.colors.TRANSPARENT,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            on_change=self.validar_cedula,
            hover_color=Colores.GRIS00
        )

        # Pagos Mensuales
        self.campo_pagos = ft.TextField(
            label="Pagos Mensuales",
            value=str(self.finanza.get("pagos_mensuales", "")),
            width=270,
            input_filter=ft.NumbersOnlyInputFilter(),
            border_radius=0,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=ft.colors.TRANSPARENT,
            on_change=self.validar_numero,
            hover_color=Colores.GRIS00
        )

        # Impuestos Anuales
        self.campo_impuestos = ft.TextField(
            label="Impuestos Anuales",
            value=str(self.finanza.get("impuestos_anuales", "")),
            width=270,
            input_filter=ft.NumbersOnlyInputFilter(),
            border_radius=0,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=ft.colors.TRANSPARENT,
            on_change=self.validar_numero,
            hover_color=Colores.GRIS00
        )

        # Fecha de Pago
        self.campo_fecha = ft.TextField(
            label="Fecha de Pago",
            value=self.finanza.get("fecha_pago", ""),
            width=180,
            max_length=10,
            hint_text="YYYY-MM-DD",
            border_radius=0,
            bgcolor=Colores.NEGRO,
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=ft.colors.TRANSPARENT,
            on_change=self.validar_fecha,
            hover_color=Colores.GRIS00
        )

        # Botón Guardar
        texto_btn = "Agregar" if accion == "agregar" else "Actualizar"
        boton_guardar = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.SAVE, color=Colores.NEGRO1),
                ft.Text(texto_btn, color=Colores.NEGRO1, size=16, weight=ft.FontWeight.BOLD)
            ], spacing=5),
            on_click=lambda _: self.guardar(),
            style=ft.ButtonStyle(
                bgcolor=Colores.AMARILLO1,
                shape=ft.RoundedRectangleBorder(radius=0)
            )
        )

        # Contenedor del formulario
        self.formulario = ft.Container(
            padding=20,
            border_radius=0,
            content=ft.Column([
                ft.Row([self.campo_control, self.campo_cedula, self.campo_fecha], spacing=15),
                ft.Row([self.campo_pagos, self.campo_impuestos], spacing=15),
                ft.Row([boton_guardar], alignment=ft.MainAxisAlignment.END)
            ])
        )

    def guardar(self):
        try:
            UtilMensajes.mostrar_snack(self.finanzas_page, "Registro de finanzas guardado", tipo="success")
            for campo in [
                self.campo_control,
                self.campo_cedula,
                self.campo_pagos,
                self.campo_impuestos,
                self.campo_fecha
            ]:
                campo.value = ""
                campo.error_text = None
                campo.update()
        except Exception as err:
            UtilMensajes.mostrar_snack(self.finanzas_page, f"Error: {err}", tipo="error")

    # Validaciones
    def validar_control(self, e):
        e.control.error_text = None if e.control.value.isdigit() else "Solo números"
        e.control.update()

    def validar_cedula(self, e):
        e.control.error_text = None if re.match(r'^[VE]-\d{7,9}$', e.control.value) else "'V-' o 'E-'"
        e.control.update()

    def validar_numero(self, e):
        try:
            float(e.control.value)
            e.control.error_text = None
        except:
            e.control.error_text = "Número inválido"
        e.control.update()

    def validar_fecha(self, e):
        try:
            datetime.strptime(e.control.value, "%Y-%m-%d")
            e.control.error_text = None
        except:
            e.control.error_text = "Formato YYYY-MM-DD"
        e.control.update()
