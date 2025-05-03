# utils/helpers.py
import flet as ft
from utils.colors import Colores


class UtilMensajes:
    @staticmethod
    def mostrar_snack(page, texto, tipo="info"):
        if tipo == "error":
            fondo, color = ft.colors.RED_800, ft.colors.WHITE
        elif tipo == "success":
            fondo, color = ft.colors.GREEN, ft.colors.WHITE
        elif tipo == "pdf":
            fondo, color = "#4511ED", ft.colors.WHITE
        else:
            fondo, color = ft.colors.BLUE_GREY, ft.colors.WHITE

        snack = ft.SnackBar(
            content=ft.Text(texto, color=color),
            bgcolor=fondo,
            open=True
        )
        page.open(snack)
        page.update()

    @staticmethod
    def mostrar_sheet(page, titulo, tipo="mensaje", socio=None):
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
                        ft.Text(titulo, style=ft.TextStyle(size=20, weight="bold", color=Colores.AMARILLO1)),
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
                    ft.ElevatedButton("Cerrar", on_click=lambda _: page.close(bs))
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


    @staticmethod
    def confirmar(page, titulo, mensaje, on_confirm, on_cancel=None, modal=True):
        """
        Muestra un CupertinoAlertDialog con dos acciones: Confirmar y Cancelar.
        - on_confirm(e): callback al pulsar "Sí"
        - on_cancel(e): callback al pulsar "No" (opcional)
        """
        def _cerrar(e):
            page.close(dialog)

        acciones = [
            ft.CupertinoDialogAction(
                text="Sí",
                is_default_action=True,
                on_click=lambda e: (on_confirm(e), _cerrar(e))
            ),
            ft.CupertinoDialogAction(
                text="No",
                is_destructive_action=True,
                on_click=lambda e: (on_cancel(e) if on_cancel else None, _cerrar(e))
            ),
        ]
        dialog = ft.CupertinoAlertDialog(
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=acciones,
            modal=modal,
        )
        page.open(dialog)


    @staticmethod
    def confirmar_material(page, titulo, mensaje, on_confirm, on_cancel=None, modal=True):
        """
        Muestra un AlertDialog material con dos botones: Confirmar y Cancelar.
        - on_confirm(e): callback al pulsar "Sí"
        - on_cancel(e): callback al pulsar "No" (opcional)
        """
        def _cerrar(e):
            page.close(dialog)

        acciones = [
            ft.TextButton(
                text="No",
                on_click=lambda e: (on_cancel(e) if on_cancel else None, _cerrar(e))
            ),
            ft.TextButton(
                text="Sí",
                on_click=lambda e: (on_confirm(e), _cerrar(e))
            ),
        ]
        dialog = ft.AlertDialog(
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=acciones,
            modal=modal,
        )
        page.open(dialog)