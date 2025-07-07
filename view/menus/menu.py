import flet as ft
from datos.datos import datos_de_prueba 
from utils.colors import Colores
class Vista_Menu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.card_socios = None 
        self.menu_container = self.build()

    def _create_card(self, title: str, value: str, icon_data):
        return ft.Container(
            width=150, height=250, padding=10, margin=5,
            border_radius=0, bgcolor="#1f1f26",
            shadow=ft.BoxShadow(color="black", spread_radius=1, blur_radius=5, offset=ft.Offset(2, 2)),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Icon(icon_data, color=Colores.BLANCO, size=60),
                    ft.Text(title, size=14, color=Colores.BLANCO, weight="bold"),
                    ft.Text(value, size=20, weight="bold", color="#cbb1f2"),
                ],
            ),
        )

    def design_cards(self):
        # Cabecera
        header = ft.Container(
            height=60, bgcolor=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#2c2c34", "#161618"],
            ),
            alignment=ft.alignment.center,
        )

        # Definimos los datos de cada tarjeta: (atributo, valor, icono)
        cards_info = [
            ("SOCIOS", str(len(datos_de_prueba)), ft.icons.PEOPLE_OUTLINE),
            ("VEHÍCULOS", "15", ft.icons.LOCAL_TAXI_OUTLINED),
            ("AVANCES", "6", ft.icons.WORK_OUTLINE),
            ("SANCIONES", "8", ft.icons.REPORT_OUTLINED),
            ("FINANZAS", "15", ft.icons.PAYMENTS_OUTLINED),
        ]

        # Generamos dinámicamente las tarjetas
        cards = []
        for title, value, icon in cards_info:
            card = self._create_card(title, value, icon)
            cards.append(card)
            if title == "SOCIOS":
                self.card_socios = card  # guardamos referencia para actualizaciones

        # Las colocamos en fila centrada
        cards_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=cards
        )

        return ft.Column(
            expand=True,
            controls=[
                header,
                ft.Container(expand=True, padding=20, content=cards_row)
            ]
        )

    def actualizar_contador_socios(self):
        """Actualiza el contador de socios dinámicamente."""
        nueva_cantidad = len(datos_de_prueba)
        # El texto está en controls[2]
        self.card_socios.content.controls[2].value = str(nueva_cantidad)
        self.card_socios.update()

    def build(self):
        # Tres secciones principales
        return ft.Container(
            expand=True, padding=5, bgcolor=ft.colors.TRANSPARENT,
            content=ft.Column(
                expand=True, spacing=5, scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Container(expand=True, padding=20, alignment=ft.alignment.center,
                                 content=ft.Text("¡BIENVENIDO!", weight="bold", size=24, color="white")),
                    ft.Container(expand=True, padding=20, alignment=ft.alignment.center,
                                 content=ft.Text("SISTEMA DE GESTION LINEA SAN AGATÓN", color=Colores.AMARILLO1, size=50, weight="bold", )),
                    ft.Divider(color=Colores.AMARILLO1,),
                    self.design_cards(),
                    
                    
                ]
            )
        )

def vista_menu(page: ft.Page):
    menu = Vista_Menu(page)
    return menu.menu_container
