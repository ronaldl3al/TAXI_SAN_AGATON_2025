import flet as ft
from view.socios.socio import vista_socios
from utils.colors import Colores

class BotonesNevegacion:
    @staticmethod
    def botonesNav(pagina):
        return ft.Column(
            controls=[
            ft.TextButton(
            "INICIO", scale=1.2, icon=ft.icons.HOME,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/menu")
            ),
            ft.TextButton(
            "SOCIOS", scale=1.2, icon=ft.icons.PEOPLE_OUTLINE,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/socios")
            ),
            ft.TextButton(
            "VEHICULOS", scale=1.2, icon=ft.icons.LOCAL_TAXI_OUTLINED,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/vehiculos")
            ),
            ft.TextButton(
            "AVANCES", scale=1.2, icon=ft.icons.WORK_OUTLINE,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/avances")
            ),
            ft.TextButton(
            "SANCIONES", scale=1.2, icon=ft.icons.REPORT_OUTLINED,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/sanciones")
            ),
            ft.TextButton(
            "FINANZAS", scale=1.2, icon=ft.icons.PAYMENTS_OUTLINED,
            style=ft.ButtonStyle(
                icon_color=Colores.AMARILLO1,
                color=Colores.AMARILLO1
            ),
            on_click=lambda _: pagina.go("/finanzas")
            ),
            ],
            alignment=ft.MainAxisAlignment.START
        )
class MenuPage(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__(route="/menu")
        self.pagina = pagina
        self.bgcolor = Colores.NEGRO2

        self.area_contenido = ft.Container(
            content=ft.Column(
                controls=[], 
                spacing=10
            ),
            # bgcolor=ft.Colors.WHITE,  
            expand=True,
            # padding=10 
        )

        barra_lateral = ft.Container(
            content=ft.Column(
            controls=[
                ft.Text("MENU", size=20, weight="bold", color=Colores.AMARILLO1),
                ft.Divider(color=Colores.AMARILLO1),
                BotonesNevegacion.botonesNav(pagina)
            ],
            spacing=10
            ),
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[Colores.GRIS, Colores.AZUL2]
            ),
            width=200,
            padding=10,
            shadow=ft.BoxShadow(color="black", blur_radius=15, offset=ft.Offset(4, 4)),
            border_radius=ft.BorderRadius(5, 5, 5, 5),
            alignment=ft.alignment.top_left
        )

        barra_superior = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Linea San Agatón", color=Colores.AZUL2, size=22, weight="bold", expand=True),
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_color=Colores.NEGRO1,
                        tooltip="Cerrar sesión",
                        on_click=lambda _: pagina.go("/login")
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.center_right,
                end=ft.alignment.center_left,
                colors=[Colores.AMARILLO1, Colores.AMARILLO1]
            ),
            height=50,
            shadow=ft.BoxShadow(color="black", blur_radius=15, offset=ft.Offset(4, 4)),
            padding=10,
            border_radius=ft.BorderRadius(5, 5, 5, 5),
            alignment=ft.alignment.center_left
        )


        self.controls = [
            ft.Container(
                gradient=ft.RadialGradient(
                    center=ft.alignment.top_center,
                    radius=1,
                    colors=[Colores.NEGRO1, Colores.NEGRO2, Colores.AZUL2]
                ),
                content=ft.Column(
                    controls=[
                        barra_superior,
                        ft.Row(
                            controls=[barra_lateral, self.area_contenido],
                            expand=True
                        )
                    ],
                    expand=True,
                    spacing=5  
                ),
                expand=True
            )
        ]

    def ruta_secundaria(self):
            ruta_actual = self.pagina.route 

            if ruta_actual == "/socios":
                contenido = vista_socios(self.pagina)
            elif ruta_actual == "/vehiculos":
                contenido = ft.Text("Contenido de VEHÍCULOS", size=20)
            elif ruta_actual == "/avances":
                contenido = ft.Text("Contenido de AVANCES", size=20)
            elif ruta_actual == "/sanciones":
                contenido = ft.Text("Contenido de SANCIONES", size=20)
            elif ruta_actual == "/finanzas":
                contenido = ft.Text("Contenido de FINANZAS", size=20)
            else:
                contenido = ft.Text("Bienvenido al INICIO", size=20)

            self.area_contenido.content = contenido
            self.pagina.update()

