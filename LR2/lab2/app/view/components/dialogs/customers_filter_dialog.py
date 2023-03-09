from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from lab2.app.services.action import Action


def filter_customers(controller):
    def confirm(event):
        controller.dispatch(Action(type='FILTER'))
    return confirm

def deny_filter_customers(controller):
    def deny(event):
        controller.dispatch(Action(type='CLOSE_DIALOG'))
    return deny

def CustomerFilterDialog(props):
    return MDDialog(
        title="Filter",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id='fullname',
                hint_text="Full name",
                font_size='36',

            ),
            MDTextField(
                id='account_number',
                hint_text="Account No",
                font_size='36',
            ),
            MDTextField(
                id="address",
                hint_text="Address",
                font_size='36'
            ),
            MDTextField(
                id="phone",
                hint_text="Phone",
                font_size='36'
            ),
        
            id="form",
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="300dp"
        ),
        buttons=[
            MDFlatButton(
                text="DISABLE",
                theme_text_color="Custom",
                on_release=filter_customers(props['controller'])
            ),
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=deny_filter_customers(props['controller'])
            ),
            MDFlatButton(
                text="SEARCH",
                theme_text_color="Custom",
                on_release=filter_customers(props['controller'])
            ),
        ],
    )
