import flet as ft
from pages.home import home_content
from pages.categories import categories_content
from pages.history import history_content
from pages.settings import settings_content
from pages.navigation import create_navigation_bar  # Импортируем функцию

def main(page):
    page.adaptive = True

    # Создаем навигационный бар
    page.navigation_bar = create_navigation_bar(page)

    # Функция для отображения выбранной страницы
    def show_page(selected_index):
        # Очищаем текущие элементы на странице
        page.controls.clear()

        # Добавляем содержимое выбранной страницы
        if selected_index == 0:
            page.add(home_content(page))
        elif selected_index == 1:
            page.add(categories_content(page))
        elif selected_index == 2:
            page.add(history_content(page))
        elif selected_index == 3:
            page.add(settings_content(page))
        
        
    # Устанавливаем обработчик для навигационной панели
    page.navigation_bar.on_change = lambda e: show_page(e.control.selected_index)

    # Отображаем главную страницу по умолчанию
    show_page(0)

# Запуск приложения
ft.app(main)