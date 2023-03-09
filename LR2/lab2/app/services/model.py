from typing import List
from random import randint

from lab2.app.services.orm_models import Customer
from lab2.app.services.customers_repository import CustomersRepository
from lab2.app.db.connect import DbConnect

from lab2.app.services.template_data import countries, cities, first_names, last_names

class Model:
    customers: List[Customer] = None
    customers_repository: CustomersRepository = None

    def __init__(self) -> None:
        self.customers_repository = CustomersRepository(DbConnect())
        self.customers = list()
        # self.fill_customers()
        self.update_customers()

    #
    #  DATA Setters and Getters below
    #

    def get_customers(self):
        return self.customers

    def update_customers(self):
        self.customers = self.customers_repository.get_all()

    def add_customer(self, customer):
        self.customers_repository.save(customer)
        self.update_customers()

    def delete_customers(self, customers: List):
        self.customers_repository.delete_customers(customers)
        self.update_customers()

    def filtere_customers(self, filter_options):
        self.customers = self.customers_repository.get_filtered(filter_options)

    def fill_customers(self):
        for i in range(1, 100):
            fullname = f"{first_names[randint(0, len(first_names)-1)]} {last_names[randint(0, len(last_names)-1)]}"
            address = f"{countries[randint(0, len(countries)-1)]}, {cities[randint(0, len(cities)-1)]}"
            mobile = f"+{randint(300, 399)}-{randint(10, 99)}-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}"
            landline = f"{randint(1, 9)}-{randint(100, 999)}-{randint(1000000, 9999999)}"
            customer = Customer(
                fullname=fullname,
                account_number=str(randint(1000000000000, 9999999999999)),
                address=address,
                mobile=mobile,
                landline=landline,
            )
            self.customers_repository.save(customer)
