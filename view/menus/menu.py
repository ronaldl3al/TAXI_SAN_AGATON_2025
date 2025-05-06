import flet as ft
from datos.datos import datos_de_prueba 

class Vista_Menu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.card_socios = None 
        self.menu_container = self.build()

    def design_cards(self):
        bg_color = "#161618"
        header_gradient = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#2c2c34", "#161618"]
        )
        card_color = "#1f1f26"
        accent_color = "#cbb1f2"
        text_color = "white"

        header = ft.Container(
            height=60,
            bgcolor=header_gradient,
            padding=ft.padding.symmetric(horizontal=20),
            alignment=ft.alignment.center,
            content=ft.Text(
                "¡HOLA!",
                weight="bold",
                size=24,
                color=text_color
            )
        )

        def card(title: str, value: str, icon: ft.Control):
            return ft.Container(
                width=120,
                height=120,
                padding=10,
                margin=5,
                border_radius=0,
                bgcolor=card_color,
                shadow=ft.BoxShadow(
                    color="black", spread_radius=1, blur_radius=5, offset=ft.Offset(2, 2)
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        icon,
                        ft.Text(title, size=14, color=text_color),
                        ft.Text(value, size=20, weight="bold", color=accent_color)
                    ]
                )
            )

        self.card_socios = card(
            "SOCIOS", 
            str(len(datos_de_prueba)),
            ft.Icon(ft.icons.PEOPLE_OUTLINE, color=accent_color, size=30)
        )
        
        card2 = card("VEHICULOS", "10", ft.Icon(ft.icons.LOCAL_TAXI_OUTLINED, color=accent_color, size=30))
        card3 = card("AVANCES", "6", ft.Icon(ft.icons.WORK_OUTLINE, color=accent_color, size=30))

        cards_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[self.card_socios, card2, card3]
        )

        container_cards = ft.Column(
            expand=True,
            controls=[
                header,
                ft.Container(expand=True, padding=20, content=cards_row)
            ]
        )
        return container_cards

    def actualizar_contador_socios(self):
        """Actualiza el contador de socios dinámicamente"""
        nueva_cantidad = len(datos_de_prueba)
        self.card_socios.content.controls[2].value = str(nueva_cantidad)
        self.card_socios.update()

    def build(self):
        container1 = self.design_cards()
        container2 = ft.Container(
            expand=True,
            padding=20,
            alignment=ft.alignment.center,
            bgcolor="#282c34",
            content=ft.Text("Menú de Navegación", color="white", size=20)
        )

        container3 = ft.Container(
            expand=True,
            padding=20,
            alignment=ft.alignment.center,
            bgcolor="#3c4048",
            content=ft.Text("Contenido Principal", color="white", size=20)
        )

        main_layout = ft.Column(
            expand=True,
            controls=[
                container1,
                container2,
                container3
            ],
            spacing=5,
            scroll=ft.ScrollMode.AUTO
        )

        return ft.Container(
            content=main_layout,
            bgcolor=ft.colors.TRANSPARENT,
            padding=5,
            expand=True
        )

def vista_menu(page: ft.Page):
    menu = Vista_Menu(page)
    return menu.menu_container