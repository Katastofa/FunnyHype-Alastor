import flet as ft

def categories_content(page):
    # Создаем список категорий с изображениями и подписями
    categories = [
        {"image": "category_image/unnamed.png", "label": "Категория 1"},
        {"image": "category_image/unnamed.png", "label": "Категория 2"},
        {"image": "category_image/unnamed.png", "label": "Категория 3"},
        {"image": "category_image/unnamed.png", "label": "Категория 4"},
        {"image": "category_image/unnamed.png", "label": "Категория 5"},
        {"image": "category_image/unnamed.png", "label": "Категория 6"},
        {"image": "category_image/unnamed.png", "label": "Категория 7"},
        {"image": "category_image/unnamed.png", "label": "Категория 8"},
    ]

    # Функция для создания элементов категории
    def create_category_item(category):
        # Адаптивный размер изображения на основе текущей ширины окна
        image_size = min(page.window_width / 6, 150)
        return ft.Column(
            controls=[
                ft.Image(src=category["image"], width=image_size, height=image_size),
                ft.Text(category["label"], size=14, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        )

    # Создаем колонки для категорий
    left_column = ft.Column(
        controls=[
            create_category_item(cat) for cat in categories[:4]
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    right_column = ft.Column(
        controls=[
            create_category_item(cat) for cat in categories[4:]
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    # Создаем строку для двух колонок
    categories_row = ft.Row(
        controls=[left_column, right_column],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    return ft.Column(
        controls=[

            categories_row,  # Добавляем строки с категориями
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        scroll="adaptive",  # Добавляем вертикальную прокрутку при необходимости
    )