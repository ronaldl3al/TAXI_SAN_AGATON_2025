import flet as ft
from view.socios.socio import vista_socios
from utils.colors import Colores
from view.menus.menu import vista_menu
from utils.alerts import UtilMensajes
from auth.auth import AuthControlador


class BotonesNevegacion:
    @staticmethod
    def botonesNav(pagina):
        return ft.Column(
            controls=[
                ft.TextButton(
                    "Inicio",
                    scale=1.2,
                    icon=ft.icons.HOME,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/menu")
                ),
                ft.TextButton(
                    "Socios",
                    scale=1.2,
                    icon=ft.icons.PEOPLE_OUTLINE,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/socios")
                ),
                ft.TextButton(
                    "Vehiculos",
                    scale=1.2,
                    icon=ft.icons.LOCAL_TAXI_OUTLINED,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/vehiculos")
                ),
                ft.TextButton(
                    "Avances",
                    scale=1.2,
                    icon=ft.icons.WORK_OUTLINE,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/avances")
                ),
                ft.TextButton(
                    "Sanciones",
                    scale=1.2,
                    icon=ft.icons.REPORT_OUTLINED,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/sanciones")
                ),
                ft.TextButton(
                    "Finanzas",
                    scale=1.2,
                    icon=ft.icons.PAYMENTS_OUTLINED,
                    style=ft.ButtonStyle(
                        icon_color=Colores.AMARILLO1,
                        color=Colores.AMARILLO1
                    ),
                    on_click=lambda _: pagina.go("/finanzas")
                ),
            ],
            alignment=ft.MainAxisAlignment.END
        )


class MenuPage(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__(route="/menu")
        self.pagina = pagina
        self.bgcolor = Colores.NEGRO2
        self.rol = AuthControlador.obtener_rol()
        self.area_contenido = ft.Container(
            content=ft.Column(
                controls=[],
                spacing=10
            ),
            expand=True,
        )

        avatar = ft.Container(
            content=ft.Icon(
            name=ft.icons.PERSON_OUTLINE,
            size=64,
            color=Colores.BLANCO
            ),
            width=64,
            height=64,
            alignment=ft.alignment.center
        )

        user_header = ft.Container(
            content=ft.Column(
            controls=[
                avatar,
                ft.Text(
                self.rol,
                size=20, 
                weight="bold",  
                color=Colores.BLANCO,  
                text_align=ft.TextAlign.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  
            spacing=4
            ),
            alignment=ft.alignment.center  
        )

        barra_lateral = ft.Container(
            content=ft.Column(
                controls=[
                    user_header,
                    ft.Divider(color=Colores.BLANCO,),
                    BotonesNevegacion.botonesNav(pagina)
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[Colores.GRIS, Colores.AZUL2]
            ),
            width=140,
            padding=16,
            
            border_radius=ft.BorderRadius(0, 0, 0, 0),
            alignment=ft.alignment.top_center
        )

        barra_superior = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "  Linea San Agatón",
                        color=Colores.BLANCO,
                        size=30,
                        weight="bold",
                        expand=True,
                        font_family="Arial Black Italic",
                        italic=True
                    ),
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_color=Colores.ROJO,
                        tooltip="Cerrar sesión",
                        on_click=lambda e: UtilMensajes.confirmar_material(
                            page=pagina,
                            titulo="Confirmar Cierre de Sesión",
                            mensaje="¿Está seguro de cerrar sesión?",
                            on_confirm=lambda e: pagina.go("/login"),
                            on_cancel=lambda e: print("Cierre de sesión cancelado")
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.top_right,
                colors=[Colores.GRIS, Colores.AZUL2]
            ),
            height=50,
            
            border_radius=ft.BorderRadius(0, 0, 0, 0),
            alignment=ft.alignment.center_left
        )

        self.controls = [
            ft.Container(
                gradient=ft.RadialGradient(
                    center=ft.alignment.top_center,
                    radius=1,
                    colors=[Colores.NEGRO1, Colores.NEGRO2, Colores.AZUL2]
                ),
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src="https://iili.io/3XTug5P.png",
                            fit=ft.ImageFit.CONTAIN,
                            opacity=0.06,
                            expand=True
                        ),
                        ft.Column(
                            controls=[
                                barra_superior,
                                ft.Row(
                                    controls=[barra_lateral, self.area_contenido],
                                    expand=True
                                )
                            ],
                            expand=True,
                            spacing=5
                        )
                    ],
                    expand=True
                ),
                expand=True
            )
        ]

    def ruta_secundaria(self):
        ruta_actual = self.pagina.route

        if ruta_actual == "/socios":
            contenido = vista_socios(self.pagina)
        elif ruta_actual == "/vehiculos":
            contenido = vista_socios(self.pagina)
        elif ruta_actual == "/avances":
            contenido = ft.Text("Contenido de AVANCES", size=20)
        elif ruta_actual == "/sanciones":
            contenido = ft.Text("Contenido de SANCIONES", size=20)
        elif ruta_actual == "/finanzas":
            contenido = ft.Text("Contenido de FINANZAS", size=20)
        else:
            contenido = vista_menu(self.pagina)

        self.area_contenido.content = contenido
        self.pagina.update()
