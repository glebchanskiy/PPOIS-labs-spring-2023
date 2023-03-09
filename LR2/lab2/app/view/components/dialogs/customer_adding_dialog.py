from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from lab2.app.services.action import Action


def confirm_adding_customer(controller):
    def confirm(event):
        controller.dispatch(Action(type='ADD_CUSTOMER'))
    return confirm

def deny_adding_customer(controller):
    def deny(event):
        controller.dispatch(Action(type='CLOSE_DIALOG'))
    return deny


def CustomerAddingDialog(props):
    return MDDialog(
        title="Customer",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id='fullname',
                hint_text="Full name",
                font_size='36',
                helper_text= "Full name should contain minimum 3 characters",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id='account_number',
                hint_text="Account No",
                font_size='36',
                max_text_length=8,
                helper_text= "Account number must contain 8 characters",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id="address",
                hint_text="Address",
                font_size='36',
                helper_text= "Address should contain minimum 3 characters",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id="mobile",
                hint_text="Mobile phone",
                font_size='36',
                helper_text= "Input format: +xxx-xx-xxx-xx-xx",
                helper_text_mode= "on_error"

            ),
            MDTextField(
                id="landline",
                hint_text="Landline phone",
                font_size='36',
                helper_text= "Input format: x-xxx-xxxxxxx",
                helper_text_mode= "on_error"
            ),
            id="form",
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="370dp"
        ),
        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=deny_adding_customer(props['controller'])
            ),
            MDFlatButton(
                text="ADD",
                theme_text_color="Custom",
                on_release=confirm_adding_customer(props['controller'])
            ),
        ],
    )
