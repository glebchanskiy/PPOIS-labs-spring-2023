from lab2.app.services.model import Model
from lab2.app.view.view import View
from lab2.app.view.erroro_view import ErrorView
from lab2.app.services.orm_models import Customer
from collections import namedtuple
from sqlalchemy.exc import SQLAlchemyError
import re

class Controller:
    def __init__(self) -> None:
        self.dialog = None
        try:
            self.model = Model()
            self.view = View(controller=self)
        except SQLAlchemyError as err:
            self.view = ErrorView()

    def get_view(self):
        return self.view.root

    def dispatch(self, action):
        print(action.type, action.content)
        if action.type == 'REMOVE':
            print(self.view.table.children[0].get_row_checks())
            self.model.delete_customers(
                list(map(lambda el: el[1], self.view.table.children[0].get_row_checks())))
            self.view.update()
        if action.type == 'FILTER':
            form = self.view.dialog.content_cls.ids

            CustomerFilter = namedtuple(
                'Customer', ['fullname', 'account_number', 'address', 'phone'])
            customer_filter = CustomerFilter(
                fullname=form.fullname.text,
                account_number=form.account_number.text,
                address=form.address.text,
                phone=form.phone.text,
            )
            self.model.filtere_customers(customer_filter)
            self.view.close_dialog()
            self.view.update()

        if action.type == 'OPEN_FILTER_DIALOG':
            self.view.open_customer_filter_dialog()
        if action.type == 'CLOSE_DIALOG':
            self.view.close_dialog()
        if action.type == 'OPEN_ADDING_DIALOG':
            self.view.open_customer_adding_dialog()
        if action.type == 'ADD_CUSTOMER':
            form = self.view.dialog.content_cls.ids
            customer = Customer(
                fullname=form.fullname.text,
                account_number=form.account_number.text,
                address=form.address.text,
                mobile=form.mobile.text,
                landline=form.landline.text,
            )

            validated: bool = True
            # Вынести в класс валидатор
            if not customer.fullname or len(customer.fullname) < 4:
                form.fullname.error = True
                validated = False
            if not customer.account_number or len(customer.account_number) != 8:
                form.account_number.error = True
                validated = False
            if not customer.address or len(customer.fullname) < 4:
                form.address.error = True
                validated = False
            if not customer.mobile or not re.match(r"\+\b[\d]{3}-[\d]{2}-[\d]{3}-[\d]{2}-[\d]{2}\b", customer.mobile):
                form.mobile.error = True
                validated = False
            if not customer.landline or not re.match(r"[\d]{1}-[\d]{3}-[\d]{7}\b", customer.landline):
                form.landline.error = True
                validated = False

            if (validated):
                self.model.add_customer(customer)
                self.view.close_dialog()
                self.view.update()

    def get_customers(self):
        return self.model.get_customers()

    def get_filtered_customers(self):
        return
