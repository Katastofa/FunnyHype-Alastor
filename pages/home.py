import flet as ft

def home_content(page):
    return ft.Column(
        controls=[
            ft.Text("1", size=24),
            ft.Text("Д1", size=16),
            ft.Image(src="https://via.placeholder.com/300", width=300, height=200),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )