import os

from lab4.core.db_engine import DbEngine
from lab4.core.state import State
from lab4.core.orm_models import CardAccount, Card, Transfer, OperationType
from lab4.core.exceptions import NoCardException, NoPincodeException, WrongPincodeException, WrongCardException, InsufficientFoundsException

class Model:
    def __init__(self) -> None:
        self._db_engine = DbEngine()
        self._state = State()

    def get_account_info(self):
        if not self._state.card_number:
            raise NoCardException
        elif not self._state.pincode:
            raise NoPincodeException

        s = self._db_engine.get_session()
        account_data = s.query(CardAccount.number, CardAccount.currency, CardAccount.balance).join(
            Card, Card.account_id == CardAccount.id).filter(Card.number == self._state.card_number).first()
        s.close()
        return {
            "number": account_data[0],
            "currency": account_data[1],
            "balance": account_data[2]
        }

    def terminate(self):
        self._state.card_number = None
        self._state.pincode = None
        self._state.dump()
        return {
            "message": "termination"
        }

    def set_pincode(self, pincode):
        if not self._state.card_number:
            raise NoCardException

        s = self._db_engine.get_session()
        card = s.query(Card).filter(Card.number == self._state.card_number).filter(
            Card.pincode == pincode).first()
        s.close()

        if not card:
            raise WrongPincodeException("Пинкод неверный!")
        else:
            self._state.pincode = pincode
            return {
                "message": "pincode accepted"
            }

    def set_card(self, card_number):
        self._state.pincode = None

        s = self._db_engine.get_session()
        card = s.query(Card).filter_by(number=card_number).first()
        s.close()

        if not card:
            raise WrongCardException(f"Карта с номером {card_number} - не найдена")
        else:
            self._state.card_number = card_number
            return {
                "message": "card accepted"
            }

    def payment_phone(self, money, phone):
        if not self._state.card_number:
            raise NoCardException
        elif not self._state.pincode:
            raise NoPincodeException

        s = self._db_engine.get_session()
        (account_id,) = s.query(Card.account_id).filter(
            Card.number == self._state.card_number).first()

        (balance,) = s.query(CardAccount.balance).join(
            Card, Card.account_id == CardAccount.id
        ).filter(Card.number == self._state.card_number).filter(Card.pincode == self._state.pincode).first()

        if (balance - money) < 0:
            s.close()
            raise InsufficientFoundsException

        s.query(CardAccount).filter(CardAccount.id == account_id).update(
            {CardAccount.balance: CardAccount.balance - money})
        s.add(Transfer(
            account_id=account_id,
            operation_type=OperationType.withdrawal,
            operation_name=f"phone payment [{phone}]",
            amount=money
        ))
        s.commit()
        s.close()

        return {
            "message": f"phone [{phone}] paid successfully [{money}]"
        }

    def get_transfers_info(self):
        if not self._state.card_number:
            raise NoCardException
        elif not self._state.pincode:
            raise NoPincodeException

        s = self._db_engine.get_session()
        transfers = s.query(
            Transfer.completed_at,
            Transfer.operation_name,
            Transfer.operation_type,
            Transfer.amount
        ).join(
            CardAccount, CardAccount.id == Transfer.account_id
        ).join(
            Card, Card.account_id == CardAccount.id
        ).filter(Card.number == self._state.card_number).all()
        s.close()

        if not transfers:
            return {
                "transfers": []
            }
        else:
            return {
                "transfers": transfers
            }

    def withdrawal(self, money):
        if not self._state.card_number:
            raise NoCardException
        elif not self._state.pincode:
            raise NoPincodeException


        s = self._db_engine.get_session()
        (account_id,) = s.query(Card.account_id).filter(
            Card.number == self._state.card_number).first()
        (balance,) = s.query(CardAccount.balance).join(
            Card, Card.account_id == CardAccount.id
        ).filter(Card.number == self._state.card_number).filter(Card.pincode == self._state.pincode).first()

        if (balance - money) < 0:
            s.close()
            raise InsufficientFoundsException
            
        elif (self._state.monies - money) < 0:
            s.close()
            raise InsufficientFoundsException

        s.query(CardAccount).filter(CardAccount.id == account_id).update(
            {CardAccount.balance: CardAccount.balance - money})

        s.add(Transfer(
            account_id=account_id,
            operation_type=OperationType.withdrawal,
            operation_name="Withdrawal of money from the account",
            amount=money
        ))
        s.commit()
        s.close()

        self._state.monies -= money
        self._state.dump()
        return { 
            "message": f"{money} cash withdrawn"
        }
