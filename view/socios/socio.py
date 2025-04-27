import flet as ft
from utils.alerts import mostrar_mensaje, mostrar_bottomSheet
from utils.colors import Colores
from auth.auth import AuthControlador
from datos.datos import datos_de_prueba


class SociosTable:
    def __init__(self, socios_page, socios_data):
        self.socios_page = socios_page
        self.data_table = self._crear_tabla(socios_data)

    def _crear_tabla(self, socios):
        return ft.DataTable(
            bgcolor=ft.colors.TRANSPARENT,
            border_radius=20,
            heading_row_color=Colores.AZUL3,
            data_row_color={
                "hovered": Colores.AZUL,
                "selected": Colores.AZUL2
            },
            columns=self._columnas(),
            rows=self._filas(socios),
        )

    def _columnas(self):
        estilos = dict(weight="w700", size=15, color=Colores.AMARILLO1, font_family="Arial Black italic")
        return [
            ft.DataColumn(ft.Text(label, **estilos))
            for label in [
                "Control", "Nombres", "Apellidos", "Cédula",
                "Teléfono", "Dirección", "RIF", "Fecha Nac.", "Acciones"
            ]
        ]

    def _filas(self, socios):
        return [ft.DataRow(cells=self._celdas(s)) for s in socios]

    def _celdas(self, socio):
        datos = [
            socio['numero_control'], socio['nombres'], socio['apellidos'],
            socio['cedula'], socio['numero_telefono'], socio['direccion'],
            socio['rif'], socio['fecha_nacimiento']
        ]
        celdas = [ft.DataCell(ft.Text(d, color=Colores.BLANCO, size=13)) for d in datos]
        acciones = ft.Row(self._botones_accion(socio), alignment="start")
        celdas.append(ft.DataCell(acciones))
        return celdas

    def _botones_accion(self, socio):
        return [
            ft.IconButton(
                icon=ft.icons.EDIT,
                icon_color="#F4F9FA",
                on_click=lambda e, s=socio: self.socios_page.mostrar_bottomsheet_editar(s)
            ),
            ft.IconButton(
                icon=ft.icons.DELETE_OUTLINE,
                icon_color="#eb3936",
                on_click=lambda e, s=socio: self.socios_page.confirmar_eliminar_socio(s)
            )
        ]

    def actualizar(self, nuevos_socios):
        self.data_table.rows = self._filas(nuevos_socios)
        self.data_table.update()


class SociosView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.rol = AuthControlador.obtener_rol()
        self.tabla = SociosTable(self, datos_de_prueba)

    def _boton_agregar(self):
        if self.rol in ["Admin", "Editor"]:
            return ft.IconButton(
                icon=ft.icons.ADD,
                icon_size=40,
                style=ft.ButtonStyle(color="#06F58E"),
                on_click=lambda e: mostrar_bottomSheet(self.page, " AGREGAR SOCIO", tipo="formulario")
            )
        return ft.Container()

    def _botones_test(self):
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="PDF",
                    icon=ft.icons.PICTURE_AS_PDF,
                    icon_color=Colores.AZUL2,
                    bgcolor=Colores.AMARILLO1,
                    color=Colores.AZUL2,
                    on_click=lambda e: mostrar_mensaje(self.page, "Documento PDF generado correctamente", tipo="pdf")
                ),
                self._boton_agregar()
            ],
            alignment="start",
            spacing=10
        )

    def mostrar_bottomsheet_editar(self, socio):
        # Delegar o implementar como antes
        mostrar_bottomSheet(self.page, "Editar Socio", socio=socio)

    def confirmar_eliminar_socio(self, socio):
        # Delegar o implementar como antes
        mostrar_mensaje(self.page, f"¿Eliminar socio {socio['nombres']}?", tipo="confirm")

    def construir(self):
        header = ft.Row(
            controls=[
                ft.Text("SOCIOS", size=20, weight="bold", color=Colores.AMARILLO1),
                self._botones_test()
            ],
            alignment="spaceBetween"
        )
        contenido = ft.Column(
            controls=[header, self.tabla.data_table],
            spacing=5,
            scroll=ft.ScrollMode.AUTO
        )
        return ft.Container(
            content=contenido,
            bgcolor=ft.colors.TRANSPARENT,
            padding=5,
            expand=True
        )


def vista_socios(page: ft.Page):
    view = SociosView(page)
    return view.construir()