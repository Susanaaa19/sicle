import flet as ft
import sqlite3
from sqlite3 import Error

# Nombre de tu base de datos SQLite
db_name = "sicle.db"
session = False

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print("Conexión a SQLite establecida correctamente.")
    except Error as e:
        print(f"Error al conectar a SQLite: {e}")
    return connection

def main(page: ft.Page):

    def goEstu(e):
        page.go('/estudiante')

    def goDoc(e):
        page.go('/docente')

    def goAdmin(e):
        page.go('/admin')

    def loginAlumno(username, password):
        conexiondb = create_connection(db_name)
        cursor = conexiondb.cursor()

        # Verificar si el ID de usuario existe
        cursor.execute('''
        SELECT id_alumno FROM login WHERE id_alumno = ?
        ''', (username,))
        
        user = cursor.fetchone()
        
        if not user:
            print("ID de alumno no existe")
        else:
            # Si el ID existe, verificar el PIN
            cursor.execute('''
            SELECT * FROM login WHERE id_alumno = ? AND pin = ?
            ''', (username, password))
            
            user = cursor.fetchone()
            
            if user:
                print("Inicio de sesión exitoso")
            else:
                print("PIN incorrecto")
        
        conexiondb.close()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(main_view())
        elif page.route == "/estudiante":
            page.views.append(estudiante_view())
        elif page.route == "/docente":
            page.views.append(docente_view())
        elif page.route == "/admin":
            page.views.append(admin_view())
        page.update()

    def main_view():
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text(
                'Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white',
                text_align='center'
            )], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ),
                bgcolor='#0D257C',
                padding=10,
                height=60,)


        logo = ft.ResponsiveRow([
        ft.Column([ft.Image('https://i.postimg.cc/PrFD80ML/4.png', width=150, height=150, border_radius=150),
                   ft.Text('Instituto Tecnologico de Tuxtepec', text_align='center'),],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,  # Espacio entre elementos en la fila
            run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} )
        
        opciones = ft.Container(
            expand=True,
            content= ft.Column(
                scroll="auto",
                controls=[
                    ft.ResponsiveRow(
                        [
                                                ft.Container(
                        ft.Column([
                                ft.Image(src="https://i.postimg.cc/x1VBNBmk/1.png", width=120, height=120),
                                ft.TextButton(content=ft.Container(ft.Text(value="Estudiante", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')),on_click=goEstu),
                                ft.Text('Modulo de Consultas y servicios para los estudiantes', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Image(src="https://i.postimg.cc/1XvqBdhj/2.png", width=120, height=120),
                                ft.TextButton(
                                    content=ft.Container(
                                        ft.Text(value="Docente", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')
                                    ),
                                    on_click=goDoc
                                ),
                                ft.Text('Modulo de Consultas y Actividades', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Image(src="https://i.postimg.cc/HWzXTrc9/3.png", width=120, height=120),
                                ft.TextButton(
                                    content=ft.Container(
                                        ft.Text(value="Administrador", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')
                                    ),
                                    on_click=goAdmin
                                ),
                                ft.Text('Modulo de Consultas', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    )
                        ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
                run_spacing={"xs": 20, "sm": 30}
                    )
                ]
            ),padding=20
        )
        return ft.View("/", [barra, logo, opciones])

    def estudiante_view():
        id = ft.TextField(hint_text='Usuario Estudiante', bgcolor='white', border_radius=10, width=380, height=50, adaptive=True)
        pin = ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10, width=380, height=50,password = True, adaptive=True)
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text('Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white', text_align='center'
            )], alignment=ft.MainAxisAlignment.CENTER, spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ), bgcolor='#0D257C', padding=10, height=60,)

        container = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Row([
                        ft.Text(
                            'Inicio de Sesion', 
                            color='#0D257C', 
                            weight=ft.FontWeight.BOLD, 
                            size=20,
                            font_family='OpenSans',
                            text_align='center'
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER), bgcolor='white', width=450,  height=50, border_radius=60, padding=10
                ),
                ft.Row([
                    ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100)
                ], alignment=ft.MainAxisAlignment.CENTER, height=100),
                ft.Divider(height=30, color='transparent'),
                ft.Column([
                    id, pin,
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar',on_click = lambda e: loginAlumno(id.value, pin.value), style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
            width=page.width*0.9 if page.width < 600 else page.width*0.3,
            height=page.width*0.9 if page.width < 600 else page.width*0.3,
            bgcolor='#0D257C',
            border_radius=40,
            margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
        )

        return ft.View("/estudiante", [barra, container])
    
    def docente_view():
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text(
                'Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white',
                text_align='center'
            )], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ),
                bgcolor='#0D257C',
                padding=10,
                height=60,)
        container = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Row([
                        ft.Text(
                            'Inicio de Sesion', 
                            color='#0D257C', 
                            weight=ft.FontWeight.BOLD, 
                            size=20,
                            font_family='OpenSans',
                            text_align='center'
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor='white', 
                    width=450, 
                    height=50, 
                    border_radius=60, 
                    padding=10
                ),
                ft.Row([
                    ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100)
                ], alignment=ft.MainAxisAlignment.CENTER, height=100),
                ft.Divider(height=30, color='transparent'),
                ft.Column([
                    ft.TextField(hint_text='Usuario Docente', bgcolor='white', border_radius=10, width=380, height=50,adaptive=True),
                    ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10, width=380, height=50, password=True,adaptive=True),
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar', style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
            width=page.width*0.9 if page.width < 600 else page.width*0.3,
            height=page.width*0.9 if page.width < 600 else page.width*0.3,
            bgcolor='#0D257C',
            border_radius=40,
            margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
        )

        return ft.View("/docente", [barra, container])

    def admin_view():
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text(
                'Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white',
                text_align='center'
            )], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ),
                bgcolor='#0D257C',
                padding=10,
                height=60,)


        container = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Row([
                        ft.Text(
                            'Inicio de Sesion', 
                            color='#0D257C', 
                            weight=ft.FontWeight.BOLD, 
                            size=20,
                            font_family='OpenSans',
                            text_align='center'
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor='white', 
                    width=450, 
                    height=50, 
                    border_radius=60, 
                    padding=10
                ),
                ft.Row([
                    ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100)
                ], alignment=ft.MainAxisAlignment.CENTER, height=100),
                ft.Divider(height=30, color='transparent'),
                ft.Column([
                    ft.TextField(hint_text='Usuario Administrador', bgcolor='white', border_radius=10, width=380, height=50),
                    ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10, width=380, height=50, password = True, adaptive=True),
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar', style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
            width=page.width*0.9 if page.width < 600 else page.width*0.3,
            height=page.width*0.9 if page.width < 600 else page.width*0.3,
            bgcolor='#0D257C',
            border_radius=40,
            margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
        )

        return ft.View("/admin", [barra, container])

    page.theme_mode = ft.ThemeMode.LIGHT
    page.on_route_change = route_change
    page.go(page.route)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
