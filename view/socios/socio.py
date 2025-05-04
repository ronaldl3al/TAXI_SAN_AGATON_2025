import flet as ft
from utils.colors import Colores
from utils.alerts import UtilMensajes
from auth.auth import AuthControlador
from datos.datos import datos_de_prueba


class SociosTable:
    def __init__(self, pagina_view, socios):
        # pagina_view es la instancia de SociosView
        self.pagina_view = pagina_view
        self._socios_original = socios
        # Anchos de columna en píxeles
        self.anchos = [20, None, None, 65, 85, None, 77, 70, None]
        self.data_table = self._armar_tabla(socios)

    def _armar_tabla(self, socios):
        return ft.DataTable(
            bgcolor=Colores.NEGRO0,
            border_radius=5,
            heading_row_color=Colores.AZUL3,
            data_row_color={
                "hovered": Colores.AZUL,
                "selected": Colores.AZUL2
            },
            # Altura mínima y máxima de filas para permitir varias líneas
            data_row_min_height=40,
            data_row_max_height=float("inf"),
            heading_row_height=65,
            columns=self._columnas(),
            rows=self._filas(socios),
        )

    def _columna(self, texto, ancho):
        estilos = dict(
            weight="w700",
            size=15,
            color=Colores.AMARILLO1,
            font_family="Arial Black italic"
        )
        return ft.DataColumn(
            ft.Container(
                width=ancho,
                content=ft.Text(texto, no_wrap=True, **estilos)
            )
        )

    def _columnas(self):
        etiquetas = [
            "N°", "Nombres", "Apellidos", "Cédula",
            "Teléfono", "Dirección", "RIF", "F. Nac.", "Acciones"
        ]
        return [self._columna(et, self.anchos[i]) for i, et in enumerate(etiquetas)]

    def _fila(self, socio):
        valores = [
            socio["numero_control"],
            socio["nombres"],
            socio["apellidos"],
            socio["cedula"],
            socio["numero_telefono"],
            socio["direccion"],
            socio["rif"],
            socio["fecha_nacimiento"],
            ""
        ]
        celdas = []
        for i, val in enumerate(valores[:-1]):
            celdas.append(
                ft.DataCell(
                    ft.Container(
                        width=self.anchos[i],
                        content=ft.Text(
                            val,
                            color=Colores.BLANCO,
                            size=12,
                            no_wrap=False,  # permitir ajuste de línea
                            weight="bold",
                            font_family="Arial",
                            selectable=True,
                        )
                    )
                )
            )

        acciones = ft.Row(self._botones_accion(socio), alignment="end")
        celdas.append(
            ft.DataCell(
                ft.Container(
                    width=self.anchos[-1],
                    content=acciones
                )
            )
        )
        return ft.DataRow(cells=celdas)

    def _filas(self, socios):
        return [self._fila(s) for s in socios]

    def _botones_accion(self, socio):
        page = self.pagina_view.page
        rol = self.pagina_view.rol

        botones = []

        if rol in ["Admin", "Editor"]:
            botones.append(
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color="#F4F9FA",
                    on_click=lambda e, s=socio: UtilMensajes.mostrar_sheet(
                        page, "Editar Socio", tipo="formulario", socio=s
                    )
                )
            )

        if rol == "Admin":
            botones.append(
                ft.IconButton(
                    icon=ft.icons.DELETE_OUTLINE,
                    icon_color="#eb3936",
                    on_click=lambda e, s=socio: UtilMensajes.confirmar(
                        page=page,
                        titulo="Confirmar Eliminación",
                        mensaje=f"¿Está seguro de eliminar al socio {s['nombres']}?",
                        on_confirm=lambda e, s=socio: self.eliminar_socio_api(s),
                        on_cancel=lambda e: print("Eliminación cancelada")
                    )
                )
            )

        return botones

    def eliminar_socio_api(self, socio):
        # Lógica para conectar con la API y eliminar al socio
        print(f"Conectando a la API para eliminar al socio {socio['nombres']}...")
        # Aquí iría tu llamada real a requests.delete(...)

    def filtrar(self, texto):
        texto = texto.lower()
        filtrados = [
            s for s in self._socios_original
            if texto in s["nombres"].lower()
            or texto in s["apellidos"].lower()
            or texto in s["cedula"].lower()
            or texto in s["numero_control"].lower()
            or texto in s["numero_telefono"].lower()
        ]
        self.actualizar(filtrados)

    def actualizar(self, socios):
        self.data_table.rows = self._filas(socios)
        self.data_table.update()


class SociosView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.rol = AuthControlador.obtener_rol()
        self.tabla = SociosTable(self, datos_de_prueba)
        self.buscador = ft.TextField(
            label="Buscar",
            prefix_icon=ft.icons.SEARCH,
            border_radius=5,
            width=500,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=20),
            hint_text="Buscar por nombre, apellido, cédula, control...",
            bgcolor=Colores.GRIS,
            on_change=self._al_buscar,
            border_color=Colores.BLANCO,
            focused_border_color=Colores.AMARILLO1,
        )

    def _al_buscar(self, e):
        self.tabla.filtrar(self.buscador.value)

    def _boton_agregar(self):
        if self.rol in ["Admin", "Editor"]:
            return ft.IconButton(
                icon=ft.icons.ADD,
                icon_size=40,
                style=ft.ButtonStyle(color="#06F58E"),
                on_click=lambda e: UtilMensajes.mostrar_sheet(
                    self.page, "Agregar Socio", tipo="formulario", socio=None
                )
            )
        return ft.Container()

    def _botones_prueba(self):
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="PDF",
                    icon=ft.icons.PICTURE_AS_PDF,
                    icon_color=Colores.AZUL2,
                    bgcolor=Colores.AMARILLO1,
                    color=Colores.AZUL2,
                    on_click=lambda e: UtilMensajes.mostrar_snack(
                        self.page, "Documento PDF generado correctamente", tipo="pdf"
                    )
                ),
                self._boton_agregar()
            ],
            alignment="start",
            spacing=10
        )

    def construir(self):
        encabezado = ft.Row(
            controls=[
                ft.Text(
                    "SOCIOS",
                    size=30,
                    weight="bold",
                    color=Colores.AMARILLO1,
                    font_family="Arial Black italic"
                ),
                self.buscador,
                self._botones_prueba(),
            ],
            alignment="spaceBetween"
        )
        encabezado = ft.Container(content=encabezado, margin=15)
        contenido = ft.Column(
            controls=[encabezado, self.tabla.data_table],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START
        )
        return ft.Container(
            content=contenido,
            bgcolor=ft.colors.TRANSPARENT,
            padding=5,
            expand=True,
            alignment=ft.alignment.top_left
        )


def vista_socios(page: ft.Page):
    view = SociosView(page)
    return view.construir()
