import flet as ft
import sqlite3

db_name = "sicle.db"

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return connection

def dataAlumno_view(page: ft.Page):
    id_alumno = 21350301
    conexiondb = create_connection(db_name)
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
                control = nombreCompleto = carrera = "No data"

            # Consulta SQL para obtener calificaciones (usando el ID recibido)
            cursor.execute("SELECT * FROM calificaciones WHERE id_alumno = ?", (id_alumno,))
            grade_data = cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Error al ejecutar las consultas: {e}")
        finally:
            conexiondb.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

    barra = ft.Container(
        ft.ResponsiveRow(
            [
                ft.Text(
                    "Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)",
                    font_family="Open-Sans",
                    weight=ft.FontWeight.BOLD,
                    size={"xs": 25, "sm": 30, "md": 35, "lg": 40},
                    color="white",
                    text_align="center",
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=1,
            run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20},
        ),
        bgcolor="#0D257C",
        padding=10,
        height=60,
    )

    def opciones(e):
        if e.control.selected_index == 0:
            menu.visible = True
            calificaciones.visible = False
            page.update()
        elif e.control.selected_index == 1:
            calificaciones.visible = True
            menu.visible = False
            page.update()
        elif e.control.selected_index == 2:
            # Enlazar con el login
            pass

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PERSON), label="Datos Personales"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                label="Calificaciones",
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HIGHLIGHT_OFF), label="Salir"
            ),
        ],
        on_change=opciones,
    )

    def menu(e):
        page.drawer.open = True
        page.drawer.update()

    bar = ft.Container(
        ft.Column(
            [
                ft.Container(
                    content=ft.IconButton(
                        ft.icons.MENU, padding=20, on_click=menu
                    ),
                    margin=ft.margin.only(left=-10),
                )
            ]
        )
    )

    menu = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Datos Personales",
                                color="white",
                                text_align="center",
                                size=20,
                            ),
                            bgcolor="#0D257C",
                            width=250,
                            height=50,
                            alignment=ft.alignment.center,
                            border_radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("")),
                                ft.DataColumn(ft.Text("")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("No. Control: ")),
                                        ft.DataCell(ft.Text(control)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Extencion: ")),
                                        ft.DataCell(ft.Text("(TX) TUX")),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Coordinador: ")),
                                        ft.DataCell(ft.Text("")),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Nombre: ")),
                                        ft.DataCell(ft.Text(nombreCompleto)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Modalidad: ")),
                                        ft.DataCell(ft.Text("Presencial")),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Carrera: ")),
                                        ft.DataCell(ft.Text(carrera)),
                                    ]
                                ),
                            ],
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    calificaciones = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Calificaciones",
                                color="white",
                                text_align="center",
                                size=20,
                            ),
                            bgcolor="#0D257C",
                            width=250,
                            height=50,
                            alignment=ft.alignment.center,
                            border_radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Modulo")),
                                ft.DataColumn(ft.Text("   ")),
                                ft.DataColumn(ft.Text("Parcial 1")),
                                ft.DataColumn(ft.Text("Parcial 2")),
                                ft.DataColumn(ft.Text("Final")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(f"Modulo {i}")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                    ]
                                )
                                for i in range(1, 6)
                            ],
                            column_spacing=20,
                        ),
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Modulo")),
                                ft.DataColumn(ft.Text("   ")),
                                ft.DataColumn(ft.Text("Parcial 1")),
                                ft.DataColumn(ft.Text("Parcial 2")),
                                ft.DataColumn(ft.Text("Final")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(f"Modulo {i}")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                        ft.DataCell(ft.Text("")),
                                    ]
                                )
                                for i in range(6, 11)
                            ],
                            column_spacing=20,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [ft.Text("Calificacion Final: ")],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )
    )

    page.add(barra, bar, menu)
    page.theme_mode = ft.ThemeMode.LIGHT
    calificaciones.visible = False
    page.add(calificaciones)

    return ft.View("/estudiante", [barra, bar, menu, calificaciones])

ft.app(target=dataAlumno_view, view=ft.AppView.WEB_BROWSER)
