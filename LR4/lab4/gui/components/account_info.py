from kivymd.uix.button import MDRaisedButton

from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

from lab4.gui.view import View


def AccountInfo(view: View):
    return MDScreen(
        MDTopAppBar(
            id='bar',
            title="Account info",
            elevation=0,
            pos_hint={'top': 1, 'left': 0},
        ),
        MDGridLayout(

            MDLabel(
                id="card_number_label",
                text="Account number:",
                theme_text_color="Primary",
                halign='left',
            ),
            MDLabel(
                id="card_number",
                theme_text_color="Secondary",
                font_size= "100",
                halign='left',
            ),

            MDLabel(
                id="currency_label",
                font_size= "100",
                halign='left',
                text='Currency',
            ),
            MDLabel(
                id="currency",
                theme_text_color="Secondary",
                font_size= "100",
                halign='left',
            ),
            MDLabel(
                id="balance_label",
                font_size= "100",
                halign='left',
                text='Balance',
            ),
            MDLabel(
                id="balance",
                theme_text_color="Secondary",
                font_size= "100",
                halign='left',
            ),

            id='info_form',
            padding=(150, 0, 0,300),
            cols=2,

            height=dp(500),
            size_hint_y=None,

            # orientation='vertical',
            # padding=100

        ),
        MDRaisedButton(
            text="BACK",
            halign='center',
            theme_text_color="Custom",
            on_press=view.to_operations,
            pos_hint={"center_x": .5, "center_y": 0.1},
            font_size=50
        ),
        name='account_info',
        id='account_info',
    )
