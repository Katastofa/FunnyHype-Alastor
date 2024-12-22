import flet as ft

def categories_content(page):
    return ft.Column(
        controls=[
            ft.Text("Это главная страница", size=24),
            ft.Text("Добро пожаловать в приложение!", size=16),
            ft.Image(src="https://via.placeholder.com/300", width=300, height=200),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )