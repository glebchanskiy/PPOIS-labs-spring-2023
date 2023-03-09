from tabulate import tabulate

from lab4.core.controller import Controller
from lab4.cli.exceptions import ParsingEexception


def account_info(controller: Controller, value: str) -> None:
    account_info = controller.get_account_info()
    print('\nACCOUNT INFO')
    print(tabulate([[account_info['number'], account_info['currency'], account_info['balance']]], headers=[
        'number', 'currency', 'balance'], tablefmt='simple_grid'))
    


def insert_card(controller: Controller, value: str) -> None:
    response = controller.set_card(value)
    print(response['message'])


def input_pincode(controller: Controller, value: str) -> None:
    response = controller.set_pincode(value)
    print(response['message'])


def phone_payment_operation(controller: Controller, value: str) -> None:
    try:
        phone, money = value.split('=')
    except (ValueError, IndexError):
        raise ParsingEexception(str(value))
    
    response = controller.payment_phone(money=money, phone=phone)
    print(response['message'])


def transfers_info(controller: Controller, value: str) -> None:
    response = controller.get_transfers_info()
    
    print('\nTRANSFERS')
    print(tabulate(response['transfers'], headers=[
              'datetime', 'operation', 'type', 'amount'], tablefmt='simple_grid'))


def withdrawal_operation(controller: Controller, value: str) -> None:
    response = controller.withdrawal(value)
    print(response['message'])


def get_card(controller: Controller, value: str) -> None:
    response = controller.terminate()
    print(response['message'])
