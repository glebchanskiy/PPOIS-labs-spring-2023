from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from lab4.gui.view import View


def Authorization(view: View):
    return MDScreen(
        MDTopAppBar(
            id='bar',
            title="Authorization",
            elevation=0,
            pos_hint={'top': 1, 'left': 0},
        ),
        MDBoxLayout(
            MDTextField(
                id="card_number_input",
                text="1111111111111111",
                hint_text="Card number",
                font_size='48',
                helper_text="Input card number (16 numbers)",
                max_text_length=16,
                helper_text_mode="on_error",
            ),
            MDTextField(
                id="pin_code_input",
                text="1111",
                password=True,
                password_mask="*",
                hint_text="Pin code",
                font_size='48',
                max_text_length=4,
                helper_text="Input pincode (4 numbers)",
                helper_text_mode="on_error",
            ),
            MDFlatButton(

                text="SUBMIT",
                halign='center',
                theme_text_color="Custom",
                on_press=view.submit_authorization,
            ),
            id='auth_form',
            orientation='vertical',
            padding=(100, 500),

        ),
        name='authorization',
        id='authorization',
    )
