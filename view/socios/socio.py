import flet as ft
from utils.alerts import mostrar_mensaje, mostrar_bottomSheet
from utils.colors import Colores
from auth.auth import AuthControlador
from auth.auth import AuthControlador
from datos.datos import datos_de_prueba

class SociosTable:
    def __init__(self, socios_page, socios_data):
        self.socios_page = socios_page
        self.data_table = self.crear_tabla_socios(socios_data)

    def crear_tabla_socios(self, socios):
        return ft.DataTable(
            bgcolor=ft.colors.TRANSPARENT,
            border_radius=20,
            heading_row_color=Colores.AZUL3,
            data_row_color={
                "hovered": Colores.AZUL, 
                "selected": Colores.AZUL2
            },
            columns=[
                ft.DataColumn(ft.Text("Control", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic",)),
                ft.DataColumn(ft.Text("Nombres", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Apellidos", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Cédula", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Teléfono", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Dirección", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("RIF", weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Fecha Nac.", weight="w800", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
                ft.DataColumn(ft.Text("Acciones", weight="w800", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")),
            ],
            rows=self.crear_filas(socios),
        )

    def crear_filas(self, socios):
        def obtener_acciones(socio):
            return [
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color="#F4F9FA",
                    on_click=lambda _, s=socio: self.socios_page.mostrar_bottomsheet_editar(s)
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE_OUTLINE,
                    icon_color="#eb3936",
                    on_click=lambda _, s=socio: self.socios_page.confirmar_eliminar_socio(s)
                )
            ]

        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(socio['numero_control'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['nombres'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['apellidos'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['cedula'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['numero_telefono'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['direccion'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['rif'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Text(socio['fecha_nacimiento'], color=Colores.BLANCO, size=13)),
                    ft.DataCell(ft.Row(obtener_acciones(socio), alignment="start")),
                ]
            ) for socio in socios
        ]

    def actualizar_filas(self, socios):
        self.data_table.rows = self.crear_filas(socios)
        self.data_table.update()

def vista_socios(page: ft.Page):
   
    rol = AuthControlador.obtener_rol()
    
    btn_agregar = None
    if rol in ["Admin", "Editor"]:
        btn_agregar = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=lambda e: mostrar_bottomSheet (page, "Agregar botón presionado", tipo="info"),
            icon_size=40,
            style=ft.ButtonStyle(color="#06F58E")
        )
    elif rol == "Viewer":
        btn_agregar = ""  

    # Datos de prueba


    tabla_socios = SociosTable(page, datos_de_prueba)

    botones_test = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="PDF",
                icon=ft.icons.PICTURE_AS_PDF,
                icon_color=Colores.AZUL2,
                bgcolor=Colores.AMARILLO1,
                color=Colores.AZUL2,
                on_click=lambda e: mostrar_mensaje(page, "Documento PDF generado correctamente", tipo="pdf")
            ),
            btn_agregar  if btn_agregar != "" else ft.Container(), 
        ],
        alignment="start",
        spacing=10
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("SOCIOS", size=20, weight="bold", color=Colores.AMARILLO1),
                        botones_test,
                    ],
                    alignment="spaceBetween", 
                ),
                tabla_socios.data_table,
            ],
            spacing=5,
            scroll=ft.ScrollMode.AUTO
        ),
        bgcolor= ft.colors.TRANSPARENT,
        padding=5,
        expand=True
    )