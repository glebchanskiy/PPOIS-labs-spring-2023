from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout

from lab4.gui.view import View

def Operations(view: View):
    
    return MDScreen(
        MDTopAppBar(
            id='bar',
            title="Operations",
            elevation=0,
            pos_hint={'top': 1, 'left': 0},
        ),


        MDBoxLayout(
            MDRaisedButton(
                pos_hint={'center_x': 0.5},
                text="Phone payment",
                on_press=view.to_phone_payment,
                font_size=50,
                size_hint=(0.5,0.5),
                
            ),
            MDRaisedButton(
                pos_hint={'center_x': 0.5},
                text="Transfers",
                on_press=view.to_transfers,
                font_size=50,
                size_hint=(0.5,0.5),
            ),
            MDRaisedButton(
                pos_hint={'center_x': 0.5},
                text="Account info",
                on_press=view.to_account_info,
                font_size=50,
                size_hint=(0.5,0.5),
            ),
            MDRaisedButton(
                pos_hint={'center_x': 0.5},
                text="Withdrawal",
                on_press=view.to_withdrawal,
                font_size=50,
                size_hint=(0.5,0.5),
            ),
            MDRaisedButton(
                pos_hint={'center_x': 0.5},
                text="Exit",
                on_press=view.terminate,
                font_size=50,
                size_hint=(0.5,0.5),
                
            ),
            orientation='vertical',
            spacing=50,
            # size_hint_y = None,
            padding=(100, 300),
        ),


        name='operations',
        id='operations',
        # orientation='vertical',
    )
