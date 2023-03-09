from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition import MDSlideTransition

from lab4.core.controller import Controller
from lab4.gui.components.dialog import Dialog
from lab4.core.exceptions import *



class View(MDScreenManager):
    def __init__(self, terminate_app, controller: Controller, **kw):
        super().__init__(**kw)
        self.transition = MDSlideTransition()
        self.terminate_app = terminate_app
        self.controller = controller
        self.dialog = None
        

    def submit_authorization(self, event):
        auth_screen = self.get_screen("authorization")
        try:
            self.controller.set_card(auth_screen.ids.auth_form.ids.card_number_input.text)
            self.controller.set_pincode(auth_screen.ids.auth_form.ids.pin_code_input.text)

            self.current = "operations"
        except WrongCardException as err:
            auth_screen.ids.auth_form.ids.card_number_input.error = True
            self.dialog = Dialog(self, str(err))
            self.dialog.open()
        except WrongPincodeException as err:
            auth_screen.ids.auth_form.ids.pin_code_input.error = True
            self.dialog = Dialog(self, str(err))
            self.dialog.open()

        

    def submit_withdrawal(self, event):
        withdrawal_screen = self.get_screen("withdrawal")
        try:
            withdrawal_amount = withdrawal_screen.ids.withdrawal_form.ids.withdrawal_input_text.text
            self.controller.withdrawal(withdrawal_amount)
            self.current = "operations"
        except InputFormatException as err:
            withdrawal_screen.ids.withdrawal_form.ids.withdrawal_input_text.error = True
            self.dialog = Dialog(self, str(err))
            self.dialog.open()
            

    def submit_phone_payment(self, event):
        phone_payment = self.get_screen("phone_payment")
        try:
            phone_number = phone_payment.ids.phone_pay_form.ids.phone_number.text
            money_amount = self.get_screen("phone_payment").ids.phone_pay_form.ids.money_amount.text
            self.controller.payment_phone(money=money_amount, phone=phone_number)
            self.current = "operations"
        except PhoneFormatException as err:
            phone_payment.ids.phone_pay_form.ids.phone_number.error = True
            self.dialog = Dialog(self, str(err))
            self.dialog.open()
        except InputFormatException as err:
            phone_payment.ids.phone_pay_form.ids.money_amount.error = True
            self.dialog = Dialog(self, str(err))
            self.dialog.open()
        


    def to_account_info(self, event):
        self.update_account_info()
        self.current = "account_info"

    def to_operations(self, event):
        self.current = "operations"
    
    def to_withdrawal(self, event):
        self.current = "withdrawal"

    def to_phone_payment(self, event):
        self.current = "phone_payment"
        
    def to_transfers(self, event):
        self.update_transfers_info()
        self.current = "transfers_info"

    def terminate(self, evevnt):
        self.controller.terminate()
        self.terminate_app()

    def update_account_info(self):
         screen = self.get_screen("account_info")
         data = self.controller.get_account_info()

         screen.ids.info_form.ids.card_number_label.font_size = '28sp'
         screen.ids.info_form.ids.card_number.font_size = '28sp'

         screen.ids.info_form.ids.currency_label.font_size = '28sp'
         screen.ids.info_form.ids.currency.font_size = '28sp'

         screen.ids.info_form.ids.balance_label.font_size = '28sp'
         screen.ids.info_form.ids.balance.font_size = '28sp'

         screen.ids.info_form.ids.card_number.text = data['number']
         screen.ids.info_form.ids.currency.text = data['currency']
         screen.ids.info_form.ids.balance.text = str(data['balance'])

    def update_transfers_info(self):
         screen: MDScreen = self.get_screen("transfers_info")
         data = self.controller.get_transfers_info()
         screen.children[1].row_data = data["transfers"]
         
         

    def close_dialog(self, event):
        self.dialog.dismiss(force=True)

    # def open_customer_adding_dialog(self):
    #     self.dialog = CustomerAddingDialog({
    #         "controller": self.controller
    #     })
    #     self.dialog.open()
