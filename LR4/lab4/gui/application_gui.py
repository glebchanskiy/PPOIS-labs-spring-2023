from kivymd.app import MDApp

from lab4.core.controller import Controller
from lab4.gui.view import View
from lab4.gui.components.authorization import Authorization
from lab4.gui.components.operations import Operations
from lab4.gui.components.account_info import AccountInfo
from lab4.gui.components.withdrawal import Withdrawal
from lab4.gui.components.phone_payment import PhonePayment
from lab4.gui.components.transfers_info import TransfersInfo

import os

class ApplicationGUI(MDApp):
    def __init__(self, controller: Controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    
    def terminate_app(self):
        self.stop()

    def build(self):
        self.title = 'Kono Dio da'
        self.icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "asserts/icon.tiff")
        self.theme_cls.primary_palette = "Teal"
        
        self.view = View(self.terminate_app, controller=self.controller, )
        self.view.add_widget(Authorization(self.view))
        self.view.add_widget(Operations(self.view))
        self.view.add_widget(AccountInfo(self.view))
        self.view.add_widget(Withdrawal(self.view))
        self.view.add_widget(PhonePayment(self.view))
        self.view.add_widget(TransfersInfo(self.view))
        self.view.current = "authorization"
        
        return self.view
