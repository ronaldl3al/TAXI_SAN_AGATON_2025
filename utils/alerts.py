# utils/helpers.py
import flet as ft
from utils.colors import Colores
from view.socios.formulario_socio import SociosForm

def mostrar_mensaje(page, mensaje, tipo="info"):
    if tipo == "error":
        bgcolor = ft.colors.RED_800
        text_color = ft.colors.WHITE
    elif tipo == "success":
        bgcolor = ft.colors.GREEN
        text_color = ft.colors.WHITE
    elif tipo == "pdf":
        bgcolor = "#4511ED"
        text_color = ft.colors.WHITE
    else:
        bgcolor = ft.colors.BLUE_GREY
        text_color = ft.colors.WHITE

    snack = ft.SnackBar(
        content=ft.Text(mensaje, color=text_color),
        bgcolor=bgcolor,
        open=True
    )
    page.open(snack)
    page.update()

def mostrar_bottomSheet(page, mensaje, tipo="mensaje"):
    if tipo == "formulario":
        bgcolor = Colores.AZUL2
        text_color = Colores.AMARILLO1
        # Crear el formulario de Socio
        socio_form = SociosForm(
            socios_page=page,
            titulo=mensaje,
            accion="Agregar",
            socio=None
        )
        form_content = socio_form.formulario
    else:
        bgcolor = Colores.AMARILLO1
        text_color = Colores.AMARILLO1
        form_content = ft.Column(
            tight=True,
            controls=[
                ft.Text(mensaje, color=text_color),
                ft.ElevatedButton(
                    "Cerrar",
                    on_click=lambda _: page.close(bs)  # Aquí estaba el problema
                )
            ],  # Este paréntesis faltaba
        )

    def handle_dismissal(e):
        print("BottomSheet cerrado")

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=20,
            bgcolor=bgcolor,
            border_radius=5,
            height=300,  # Ajusta la altura según necesidad
            content=form_content
        ),
    )

    page.open(bs)
    page.update()

