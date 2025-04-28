# utils/helpers.py
import flet as ft
from utils.colors import Colores


class UtilMensajes:
    @staticmethod
    def mostrar_snack(page, texto, tipo="info"):
        if tipo == "error":
            fondo = ft.colors.RED_800
            color = ft.colors.WHITE
        elif tipo == "success":
            fondo = ft.colors.GREEN
            color = ft.colors.WHITE
        elif tipo == "pdf":
            fondo = "#4511ED"
            color = ft.colors.WHITE
        else:
            fondo = ft.colors.BLUE_GREY
            color = ft.colors.WHITE

        snack = ft.SnackBar(
            content=ft.Text(texto, color=color),
            bgcolor=fondo,
            open=True
        )
        page.open(snack)
        page.update()

    @staticmethod
    def mostrar_sheet(page, titulo, tipo="mensaje", socio=None):
        # Importa aquí para evitar circular import
        if tipo == "formulario":
            from view.socios.formulario_socio import SociosForm

            fondo = Colores.AZUL2
            contenido_form = SociosForm(
                socios_page=page,
                titulo=titulo,
                accion="agregar" if socio is None else "actualizar",
                socio=socio
            ).formulario

            contenido = ft.Column([
                ft.Row(
                    controls=[
                        ft.Text(
                            titulo,
                            style=ft.TextStyle(size=20, weight="bold", color=Colores.AMARILLO1)
                        ),
                        ft.IconButton(
                            icon=ft.icons.CANCEL,
                            icon_color="#eb3936",
                            on_click=lambda _: page.close(bs)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(color=Colores.AMARILLO1),
                contenido_form
            ])
        else:
            fondo = Colores.AMARILLO1
            contenido = ft.Column(
                tight=True,
                controls=[
                    ft.Text(titulo, color=Colores.BLANCO),
                    ft.ElevatedButton(
                        "Cerrar",
                        on_click=lambda _: page.close(bs)
                    )
                ]
            )

        def _al_cerrar(e):
            print("SHEET CERRADO")

        bs = ft.BottomSheet(
            on_dismiss=_al_cerrar,
            content=ft.Container(
                padding=20,
                bgcolor=fondo,
                border_radius=5,
                height=400,
                content=contenido
            )
        )
        page.open(bs)
        page.update()
