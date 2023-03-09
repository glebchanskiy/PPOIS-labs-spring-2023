from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel


class ErrorView(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.root = MDBoxLayout(
            MDTopAppBar(
                id='bar',
                title="Connection refused",
                elevation=0,
                pos_hint={'top': 1, 'left': 0},
            ),
            MDLabel(
                markup=True,
                text="[size=40]Check connection.\nMake sure that lab2_db database is running on port 5432.[/size]",
                halign="center"
            ),
            orientation='vertical'
        )
