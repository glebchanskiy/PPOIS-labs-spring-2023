from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from lab4.gui.view import View


def PhonePayment(view: View):
    return MDScreen(
        MDTopAppBar(
            id='bar',
            title="Phone payment",
            elevation=0,
            pos_hint={'top': 1, 'left': 0},
        ),
        MDBoxLayout(
            MDTextField(
                id="phone_number",
                hint_text="Phone number",
                font_size='48',
                helper_text="blablaba",
                helper_text_mode="on_error",
            ),
            MDTextField(
                id="money_amount",
                hint_text="Enter the amount",
                font_size='48',
                helper_text="blablaba",
                helper_text_mode="on_error",
            ),
            MDRaisedButton(
                text="BACK",
                size_hint=(0.3,0.3),
                font_size=40,
                pos_hint={'center_x': 0.5},
                halign='center',
                theme_text_color="Custom",
                on_press=view.to_operations,
            ),
            MDRaisedButton(
                text="SUBMIT",
                size_hint=(0.3,0.3),
                font_size=40,
                pos_hint={'center_x': 0.5},
                halign='center',
                theme_text_color="Custom",
                on_press=view.submit_phone_payment,
            ),
            id='phone_pay_form',
            orientation='vertical',
            spacing=50,
            padding=(100, 300)

        ),
        name='phone_payment',
        id='phone_payment',
    )
