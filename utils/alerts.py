# utils/helpers.py
import flet as ft
from utils.colors import Colores
import re
from datetime import datetime

def mostrar_mensaje(page, mensaje, tipo="info"):
    if tipo == "error":
        bgcolor = ft.colors.RED_800
        text_color = ft.colors.WHITE
    elif tipo == "success":
        bgcolor = ft.colors.GREEN
        text_color = ft.colors.WHITE
    elif tipo == "pdf":
        bgcolor = "#4511ED"
        text_color = ft.colors.WHITE
    else:
        bgcolor = ft.colors.BLUE_GREY
        text_color = ft.colors.WHITE

    snack = ft.SnackBar(
        content=ft.Text(mensaje, color=text_color),
        bgcolor=bgcolor,
        open=True
    )
    page.open(snack)
    page.update()

def mostrar_bottomSheet(page, mensaje, tipo="mensaje"):
    if tipo == "formulario":
        bgcolor = Colores.AZUL2
        text_color = Colores.AMARILLO1
        # Crear el formulario de Socio
        socio_form = SociosForm(
            socios_page=page,
            titulo=mensaje,
            accion="Agregar",
            socio=None
        )
        form_content = socio_form.formulario
    else:
        bgcolor = Colores.AMARILLO1
        text_color = Colores.AMARILLO1
        form_content = ft.Column(
            tight=True,
            controls=[
                ft.Text(mensaje, color=text_color),
                ft.ElevatedButton(
                    "Cerrar",
                    on_click=lambda _: page.close(bs)  # Aquí estaba el problema
                )
            ],  # Este paréntesis faltaba
        )

    def handle_dismissal(e):
        print("BottomSheet cerrado")

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=20,
            bgcolor=bgcolor,
            border_radius=5,
            height=300,  # Ajusta la altura según necesidad
            content=form_content
        ),
    )

    page.open(bs)
    page.update()

class SociosForm:
    def __init__(self, socios_page, titulo, accion, socio=None):
        self.socios_page = socios_page
        self.accion = accion
        self.formulario = self.crear_formulario_socio(titulo, accion, socio)

    #  crear el formulario de socio
    def crear_formulario_socio(self, titulo, accion, socio=None):
        control = ft.TextField(
            border_radius=5,
            border_color=Colores.BLANCO,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            focused_border_color=Colores.AMARILLO1, 
            label="Control", 
            max_length=2, 
            width=100, 
            input_filter=ft.NumbersOnlyInputFilter(), 
           )
        nombres = ft.TextField(
            border_radius=5,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1, 
            label="Nombres",
            width=275,  
            max_length=30, 
            on_change=self.validar_texto
        )
        apellidos = ft.TextField(
            border_radius=5, 
            border_color=Colores.BLANCO, 
            bgcolor=Colores.GRIS,
            focused_border_color=Colores.AMARILLO1, 
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Apellidos", 
            width=275, 
            max_length=30, 
            on_change=self.validar_texto
        )
        cedula = ft.TextField(
            border_radius=5,
            bgcolor=Colores.GRIS,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1, 
            label="Cédula", 
            max_length=11, 
            width=125, 
            hint_text="V-/E-", 
            on_change=self.validar_cedula
        )
        telefono = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            focused_border_color=Colores.AMARILLO1, 
            label="Teléfono", 
            max_length=15, 
            width=155, 
            prefix_text="+58 ", 
            input_filter=ft.NumbersOnlyInputFilter(), 
            hint_text="414 1234567", 
            )
        direccion = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Dirección", 
            width=370, 
            max_length=50, 
            hint_text="Municipio/Urb/Sector/Calle/Casa", 
            multiline=True)
        rif = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,  # Cambiar el color del borde enfocado
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="RIF", 
            width=180, 
            max_length=13, 
            on_change=self.validar_rif,
            hint_text="V121233211",
            error_style=ft.TextStyle(color="#FF5733"),  # Cambiar el color del texto de error
        )
        fecha_nacimiento = ft.TextField(
            border_radius=5, 
            bgcolor=Colores.GRIS,
            border_color=Colores.BLANCO, 
            focused_border_color=Colores.AMARILLO1,
            label_style=ft.TextStyle(color=Colores.BLANCO, size=17),
            label="Fecha Nacimiento", 
            max_length=10, 
            width=140, 
            hint_text="AAAA-MM-DD", 
            on_change=self.validar_fecha_nacimiento
        )

        formulario = ft.Container(
            ft.Column([
                ft.Container(
                    content=ft.Row([nombres, apellidos], spacing=15),

                ),
                ft.Container(
                    content=ft.Row([control, cedula, fecha_nacimiento, telefono], spacing=15),

                ),
                ft.Container(
                    content=ft.Row([direccion, rif], spacing=15),

                ),
                ft.Row(
                    [
                        ft.TextButton("Cancelar", icon=ft.icons.CANCEL, style=ft.ButtonStyle(color="#eb3936"), on_click=lambda _: self.socios_page.cerrar_bottomsheet()),
                        ft.TextButton("Guardar", icon=ft.icons.SAVE, style=ft.ButtonStyle(color="#06F58E"), on_click=lambda _: self.guardar_socio(
                            cedula, nombres, apellidos, direccion, telefono, control, rif, fecha_nacimiento
                        ))
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ]),
            padding=20,
            border_radius=15,
        )

        return formulario

    # Métodos de validación de datos del formulario
    def validar_fecha_nacimiento(self, e):
        if Validacion.validar_fecha(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "AAAA-MM-DD"
            e.control.update()

    def validar_cedula(self, e):
        if Validacion.validar_cedula(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "'V-' o 'E-'"
            e.control.update()

    def validar_texto(self, e):
        if Validacion.validar_texto(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "Solo se permiten letras"
            e.control.update()

    def validar_rif(self, e):
        if Validacion.validar_rif(e.control.value):
            e.control.error_text = None
            e.control.update()
        else:
            e.control.error_text = "Formato RIF inválido"
            e.control.update()
class Validacion:
    @staticmethod
    def validar_fecha(fecha):
        if isinstance(fecha, datetime):
            fecha = fecha.strftime('%Y-%m-%d')
        patron = r'^\d{4}-\d{2}-\d{2}$'
        return re.match(patron, fecha) is not None

    @staticmethod
    def validar_cedula(cedula):
        patron = r'^[VE]-\d{7,9}$'
        return re.match(patron, cedula) is not None

    @staticmethod
    def validar_texto(texto):
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        return re.match(patron, texto) is not None


    @staticmethod
    def validar_rif(rif):
        patron = r'^[VEJPG]\d{7,10}$'
        return re.match(patron, rif) is not None
