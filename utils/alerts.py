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
    def mostrar_sheet(page, titulo, tipo="mensaje",
                      socio=None, vehiculo=None,
                      avance=None, sancion=None, finanza=None):
        """
        Muestra un BottomSheet con el formulario correspondiente según el objeto:
        - sancion    → SancionesForm
        - avance     → AvancesForm
        - vehiculo   → VehiculosForm
        - finanza    → FinanzasForm
        - socio      → SociosForm
        """
        if tipo == "formulario":
            # imports dentro de la función para evitar ciclos
            from view.socios.formulario_socio import SociosForm
            from view.vehiculos.formulario_vehiculo import VehiculosForm
            from view.avances.formulario_avances import AvancesForm
            from view.sanciones.formulario_sanciones import SancionesForm
            from view.finanzas.formulario_finanzas import FinanzasForm

            fondo = Colores.AZUL4
            lt = titulo.lower()

            if "sanción" in lt or "sancion" in lt:
                contenido_form = SancionesForm(
                    sanciones_page=page,
                    titulo=titulo,
                    accion="agregar" if sancion is None else "actualizar",
                    sancion=sancion
                ).formulario

            elif "avance" in lt:
                contenido_form = AvancesForm(
                    avances_page=page,
                    titulo=titulo,
                    accion="agregar" if avance is None else "actualizar",
                    avance=avance
                ).formulario

            elif "vehículo" in lt or "vehiculo" in lt:
                contenido_form = VehiculosForm(
                    vehiculos_page=page,
                    titulo=titulo,
                    accion="agregar" if vehiculo is None else "actualizar",
                    vehiculo=vehiculo
                ).formulario

            elif "finanza" in lt or "finanzas" in lt:
                contenido_form = FinanzasForm(
                    finanzas_page=page,
                    titulo=titulo,
                    accion="agregar" if finanza is None else "actualizar",
                    finanza=finanza
                ).formulario

            else:
                contenido_form = SociosForm(
                    socios_page=page,
                    titulo=titulo,
                    accion="agregar" if socio is None else "actualizar",
                    socio=socio
                ).formulario

            contenido = ft.Column([
                ft.Row(
                    controls=[
                        ft.Text(titulo,
                                style=ft.TextStyle(size=20, weight="bold", color=Colores.AMARILLO1)),
                        ft.IconButton(icon=ft.icons.CANCEL,
                                      icon_color="#eb3936",
                                      on_click=lambda _: page.close(bs))
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(color=Colores.AMARILLO1),
                contenido_form
            ])
        else:
            # Mensaje simple
            fondo = Colores.GRIS1
            contenido = ft.Column([
                ft.Row(
                    controls=[
                        ft.Text(titulo,
                                style=ft.TextStyle(size=18, weight="bold", color=Colores.AMARILLO1)),
                        ft.IconButton(icon=ft.icons.CANCEL,
                                      icon_color="#eb3936",
                                      on_click=lambda _: page.close(bs))
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(color=Colores.AMARILLO1),
                ft.Text("Este es un mensaje simple.", color=Colores.NEGRO1)
            ])

        def _al_cerrar(e):
            print("SHEET CERRADO")

        bs = ft.BottomSheet(
            on_dismiss=_al_cerrar,
            content=ft.Container(
                padding=20,
                bgcolor=fondo,
                border_radius=None,
                height=400,
                content=contenido
            )
        )
        page.open(bs)
        page.update()

    @staticmethod
    def confirmar_material(page, titulo, mensaje, on_confirm, on_cancel=None, modal=True):
        def _cerrar(e):
            page.close(dialog)

        acciones = [
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.CANCEL,
                        icon_color=ft.colors.RED,
                        on_click=lambda e: (_cerrar(e), on_cancel(e) if on_cancel else None)
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CHECK_CIRCLE,
                        icon_color=ft.colors.GREEN,
                        on_click=lambda e: (on_confirm(e), _cerrar(e))
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]
        dialog = ft.AlertDialog(
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=acciones,
            modal=modal,
            bgcolor=Colores.GRIS,
            shape=ft.RoundedRectangleBorder(radius=0),
        )
        page.open(dialog)
        page.update()
