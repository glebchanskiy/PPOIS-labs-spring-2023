from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


def Dialog(view, message: str):
    return MDDialog(
        title="Alert",
        text=message,
        buttons=[
            MDFlatButton(
                text="Ok",
                theme_text_color="Custom",
                on_press=view.close_dialog,
            ),
        ],
    )