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
    page.snack_bar = snack
    page.update()

def mostrar_bottomSheet(page, mensaje, tipo="mensaje"):
    if tipo == "formulario":
        bgcolor = Colores.AZUL2
        text_color = Colores.AMARILLO1
        
        # Crear instancia del formulario sin el parámetro controls
        socio_form = SociosForm(
            socios_page=page,
            titulo=mensaje,
            accion="Agregar",
            socio=None  # Asegúrate que este parámetro sea válido para tu clase
        )
        
        # Crear controles adicionales por fuera del formulario
        form_content = ft.Column(
            controls=[
            ft.Row(
                controls=[
                ft.Text(mensaje, style=ft.TextStyle(size=20, weight="bold", color=Colores.AMARILLO1)),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color="#eb3936",
                    on_click=lambda _: page.close(bs)
                )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Divider(color=Colores.AMARILLO1),
            socio_form.formulario,  # Asumiendo que formulario es la propiedad que contiene los controles
            ]
        )
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
        print("FORMULARIO CERRADO")

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=20,
            bgcolor=bgcolor,
            border_radius=5,
            height=400,
            content=form_content
        ),
    )

    page.open(bs)
    page.update()

