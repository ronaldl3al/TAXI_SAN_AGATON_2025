# utils/helpers.py
import flet as ft
from utils.colors import Colores

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
        bgcolor = Colores.AMARILLO1
        text_color = Colores.AMARILLO1
    else:
        bgcolor = Colores.AMARILLO1
        text_color = Colores.AMARILLO1
    def handle_dismissal(e):
        print("holis")
    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=20,
            bgcolor=bgcolor,
            border_radius=5,
            width=400,  
            height=300,  
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Text(mensaje, color=text_color),
                    ft.ElevatedButton(
                        "Cerrar",
                        on_click=lambda _: page.close(bs)
                    )
                ],
            ),
        ),
    )
    page.open(bs)
    page.update()