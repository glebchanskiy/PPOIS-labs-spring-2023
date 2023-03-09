from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable

from kivy.metrics import dp
from lab4.gui.view import View


def TransfersInfo(view: View):
    return MDScreen(
        MDTopAppBar(
            id='bar',
            title="Transfers",
            elevation=0,
            pos_hint={'top': 1, 'left': 0},
            size=(200, 100),
            size_hint=(1, None),
        ),
        MDDataTable(
            padding=(0, 100, 0, 0),
            elevation=0,
            use_pagination=True,
            pagination_menu_height=300,
            column_data=[
                ("datetime", dp(60)),
                ("operation", dp(60)),
                ("type", dp(60)),
                ("amount", dp(60)),
            ],

        ),
        MDRaisedButton(
            
            text="BACK",
            size_hint=(0.2,0.08),
            pos_hint={'center_x': 0.12, 'top': 0.1},
            font_size=40,
            on_press=view.to_operations,
        ),
    
        name='transfers_info',
        id='transfers_info',
    )
