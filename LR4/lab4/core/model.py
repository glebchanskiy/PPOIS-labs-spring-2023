import os

from lab4.core.state import State
from lab4.core.exceptions import NoCardException, NoPincodeException, WrongPincodeException, WrongCardException, InsufficientFoundsException

from lab4.core.repositories.card_repository import CardRepository
from lab4.core.repositories.card_account_repository import CardAccountRepository
from lab4.core.repositories.transfer_repository import TransferRepository
from lab4.core.dto.dto import TransferDTO

class Model:
    def __init__(self) -> None:
        self.__state = State()
        self.__card_repository = CardRepository()
        self.__card_account_repository = CardAccountRepository()
        self.__transfer_repository = TransferRepository()

    def get_account_info(self):
        if not self.__state.card_number:
            raise NoCardException
        elif not self.__state.pincode:
            raise NoPincodeException

        card = self.__card_repository.get_by_number(self.__state.card_number)
        account = self.__card_account_repository.get_by_id(card.account_id)

        return {
            "number": account.number,
            "currency": account.currency,
            "balance": account.balance
        }

    def terminate(self):
        self.__state.card_number = None
        self.__state.pincode = None
        self.__state.dump()
        return {
            "message": "termination"
        }

    def set_pincode(self, pincode):
        if not self.__state.card_number:
            raise NoCardException

        card = self.__card_repository.get_by_number(self.__state.card_number)

        if card.pincode == pincode:
            self.__state.pincode = pincode
            return {
                "message": "pincode accepted"
            }
        else:
            raise WrongPincodeException("Пинкод неверный!")

    def set_card(self, card_number):
        self.__state.pincode = None

        card = self.__card_repository.get_by_number(card_number)

        if not card:
            raise WrongCardException(
                f"Карта с номером {card_number} - не найдена")
        else:
            self.__state.card_number = card_number
            return {
                "message": "card accepted"
            }

    def payment_phone(self, money, phone):
        if not self.__state.card_number:
            raise NoCardException
        elif not self.__state.pincode:
            raise NoPincodeException

        card = self.__card_repository.get_by_number(self.__state.card_number)
        account = self.__card_account_repository.get_by_id(card.account_id)

        if (account.balance - money) < 0:
            raise InsufficientFoundsException

        account.balance -= money

        self.__card_account_repository.update(account)
        self.__transfer_repository.save(
            TransferDTO(
                account_id=account.id,
                operation_type="withdraw",
                operation_name="phone payment (ATM)",
                amount=money
            )
        )

        return {
            "message": f"phone [{phone}] paid successfully [{money}]"
        }

    def get_transfers_info(self):
        if not self.__state.card_number:
            raise NoCardException
        elif not self.__state.pincode:
            raise NoPincodeException

        card = self.__card_repository.get_by_number(self.__state.card_number)
        transfers = self.__transfer_repository.get_all_by_account_id(
            card.account_id)

        if not transfers:
            return {
                "transfers": []
            }
        else:
            return {
                "transfers": [
                    (
                        t.completed_at,
                        t.operation_name,
                        t.operation_type, t.amount
                    )
                    for t in transfers
                ]
            }

    def withdrawal(self, money):
        if not self.__state.card_number:
            raise NoCardException
        elif not self.__state.pincode:
            raise NoPincodeException

        if (self.__state.monies - money) < 0:
            raise InsufficientFoundsException

        card = self.__card_repository.get_by_number(self.__state.card_number)
        account = self.__card_account_repository.get_by_id(card.account_id)

        if (account.balance - money) < 0:
            raise InsufficientFoundsException

        account.balance -= money

        self.__card_account_repository.update(account)
        self.__transfer_repository.save(
            TransferDTO(
                account_id=account.id,
                operation_type="withdraw",
                operation_name="cash withdrawal (ATM)",
                amount=money
            )
        )

        self.__state.monies -= money
        self.__state.dump()
        return {
            "message": f"{money} cash withdrawn"
        }
