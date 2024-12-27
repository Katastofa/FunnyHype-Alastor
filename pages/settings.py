import flet as ft

def settings_content(page):
    return ft.Column(
        controls=[
            ft.Text("4", size=24),
            ft.Text("Д4!", size=16),
            ft.Image(src="https://via.placeholder.com/300", width=300, height=200),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=100,
    )