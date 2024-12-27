import flet as ft

class AdaptiveNavigationBarDestination(ft.NavigationBarDestination):
    def __init__(self, ios_icon, android_icon, label):
        super().__init__()
        self._ios_icon = ios_icon
        self._android_icon = android_icon
        self.label = label

    def build(self):
        self.icon = (
            self._ios_icon
            if self.page.platform in [ft.PagePlatform.IOS, ft.PagePlatform.MACOS]
            else self._android_icon
        )

def create_navigation_bar(page):
    return ft.NavigationBar(
        selected_index=0,
        destinations=[
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.HOME,
                android_icon=ft.Icons.HOME,
                label="Главная",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.PERSON_3_FILL,
                android_icon=ft.Icons.MENU,
                label="Категории",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,
                android_icon=ft.Icons.HISTORY,
                label="История",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.SETTINGS,
                android_icon=ft.Icons.SETTINGS,
                label="Настройки",
            ),
        ],
    )