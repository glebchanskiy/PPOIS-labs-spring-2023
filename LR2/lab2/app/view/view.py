from kivymd.uix.boxlayout import MDBoxLayout

from lab2.app.view.components.bar import Bar
from lab2.app.view.components.table import Table

from lab2.app.view.components.dialogs.customer_adding_dialog import CustomerAddingDialog
from lab2.app.view.components.dialogs.customers_filter_dialog import CustomerFilterDialog


class View(MDBoxLayout):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.dialog = None

        props = {
            "controller": self.controller
        }

        self.bar = Bar(props)
        self.table = Table(props)
        self.root = MDBoxLayout(
            self.bar,
            self.table,
            id='root_box',
            orientation='vertical',
        )

    def update(self):

        self.root.remove_widget(self.table)
        self.table = Table({
            "controller": self.controller
        })
        self.root.add_widget(self.table)

        print('ALL WIDGETS UPDATED')

    def close_dialog(self):
        self.dialog.dismiss(force=True)

    def open_customer_adding_dialog(self):
        self.dialog = CustomerAddingDialog({
            "controller": self.controller
        })
        self.dialog.open()

    def open_customer_filter_dialog(self):
        self.dialog = CustomerFilterDialog({
            "controller": self.controller
        })
        self.dialog.open()
