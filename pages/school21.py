import flet as ft

def main(page: ft.Page):
    page.title = "Название Заведения"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Логотип
    logo = ft.Image(src="path_to_logo.png", width=200, height=100)

    # Название
    title = ft.Text("Название Заведения", size=30, weight=ft.FontWeight.BOLD)

    # Контактные данные
    contact_info = ft.Column([
        ft.Text("Телефон: +7 (123) 456-78-90"),
        ft.Text("Email: example@example.com"),
    ])

    # Местоположение
    location = ft.Text("Адрес: г. Москва, ул. Примерная, д. 1")

    # Карта (можно использовать iframe или изображение карты)
    map_image = ft.Image(src="path_to_map_image.png", width=600, height=400)

    # Выбор филиалов
    branches = ft.Dropdown(
        options=[
            ft.dropdown.Option("Филиал 1"),
            ft.dropdown.Option("Филиал 2"),
            ft.dropdown.Option("Филиал 3"),
        ],
        label="Выберите филиал"
    )

    # Создание контейнеров для блоков
    logo_container = ft.Container(content=logo, padding=10, bgcolor=ft.colors.LIGHT_GREEN, border_radius=5)
    title_container = ft.Container(content=title, padding=10, bgcolor=ft.colors.LIGHT_BLUE, border_radius=5)
    contact_container = ft.Container(content=contact_info, padding=10, bgcolor=ft.colors.LIGHT_GREEN, border_radius=5)
    location_container = ft.Container(content=location, padding=10, bgcolor=ft.colors.LIGHT_GREEN, border_radius=5)
    map_container = ft.Container(content=map_image, padding=10, bgcolor=ft.colors.LIGHT_GREEN, border_radius=5)
    branches_container = ft.Container(content=branches, padding=10, bgcolor=ft.colors.LIGHT_BLUE, border_radius=5)

    # Добавление всех элементов на страницу
    page.add(logo_container, title_container, contact_container, location_container, map_container, branches_container)

ft.app(target=main)