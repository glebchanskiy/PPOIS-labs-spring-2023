from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# from lab4.gui.view import View

def Dialog(view, message: str):
    return MDDialog(
        title="Alert",
        # type="custom",
        text=message,
        buttons=[
            MDFlatButton(
                text="Ok",
                theme_text_color="Custom",
                on_press=view.close_dialog,
            ),
        ],
    )