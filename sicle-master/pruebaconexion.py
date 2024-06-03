import flet as ft
import sqlite3
from sqlite3 import Error

# Nombre de tu base de datos SQLite
db_name = "sicle.db"

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print("Conexión a SQLite establecida correctamente.")
    except Error as e:
        print(f"Error al conectar a SQLite: {e}")
    return connection

def dataAlumno_view(page: ft.Page):
    id_alumno = 21350301
    conexiondb = create_connection(db_name)
    alumno_data = None
    if conexiondb is not None:
        try:
            cursor = conexiondb.cursor()

            # Consulta SQL para obtener datos del alumno (usando el ID recibido)
            cursor.execute("SELECT id, apellido_paterno, apellido_materno, nombres, carrera, genero FROM alumnos WHERE id = ?", (id_alumno,))
            alumno_data = cursor.fetchone()

            if alumno_data:
                control = str(alumno_data[0])
                nombreCompleto = str(alumno_data[3]) + " " + str(alumno_data[1])  + " " + str(alumno_data[2]) 
                carrera = str(alumno_data[4])
            else:
                print("No se encontró el alumno con el ID especificado.")

        except Error as e:
            print(f"Error al ejecutar las consultas: {e}")
        finally:
            conexiondb.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

    barra = ft.Container(
        ft.Text(
            "Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)",
            font_family="Open-Sans",
            weight=ft.FontWeight.BOLD,
            size=25,
            color="white",
            text_align="center",
        ),
        bgcolor="#0D257C",
        padding=10,
        height=60,
    )

    if alumno_data:
        datos_personales = ft.Container(
            ft.Column(
                [
                    ft.Row([ft.Text("Datos Personales", color="white", text_align="center", size=20)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Campo")),
                                ft.DataColumn(ft.Text("Valor")),
                            ],
                            rows=[
                                ft.DataRow(cells=[ft.DataCell(ft.Text("No. Control")), ft.DataCell(ft.Text(control))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Nombre")), ft.DataCell(ft.Text(nombreCompleto))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Carrera")), ft.DataCell(ft.Text(carrera))]),
                            ],
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    else:
        datos_personales = ft.Container(
            ft.Text("No se encontraron datos para el alumno con ID: " + str(id_alumno), color="red"),
            alignment=ft.alignment.center,
        )

    page.add(barra, datos_personales)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

ft.app(target=dataAlumno_view, view=ft.AppView.WEB_BROWSER)
