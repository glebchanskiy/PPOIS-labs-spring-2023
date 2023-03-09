from lab2.app.db.connect import DbConnect
from sqlalchemy import delete, or_
from lab2.app.services.orm_models import Customer
from typing import List


class CustomersRepository:
    def __init__(self, db_connect: DbConnect) -> None:
        self.db_connect = db_connect
        self.sessionmaker = db_connect.get_sessionmaker()

    def get_all(self):
        s = self.sessionmaker()
        customers = s.query(Customer.fullname, Customer.account_number,
                            Customer.address, Customer.landline, Customer.mobile).all()
        s.close()
        return customers

    def get_filtered(self, options):
        s = self.sessionmaker()
        customers = s.query(
            Customer.fullname,
            Customer.account_number,
            Customer.address,
            Customer.landline,
            Customer.mobile
        ).filter(
            Customer.fullname.contains(options.fullname),
            Customer.account_number.contains(options.account_number),
            Customer.address.contains(options.address),
            or_(Customer.mobile.contains(options.phone),
                Customer.landline.contains(options.phone))
        ).all()
        s.close()
        return customers

    def save(self, customer: Customer):
        s = self.sessionmaker()
        s.add(customer)
        s.commit()
        s.close()

    def delete_customers(self, to_delete: List):
        s = self.sessionmaker()
        print(to_delete)
        sql1 = delete(Customer).where(Customer.account_number.in_(to_delete))
        s.execute(sql1)
        s.commit()
        s.close()
