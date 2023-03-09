import re

from lab4.core.model import Model
from lab4.core.exceptions import PhoneFormatException, InputFormatException

class Controller:
    
    def __init__(self) -> None:
        self._model = Model()
    
    def get_account_info(self):
        return self._model.get_account_info()
    
    def terminate(self):
        return self._model.terminate()
    
    def set_pincode(self, pincode):
        return self._model.set_pincode(pincode=pincode)
    
    def set_card(self, card):
        return self._model.set_card(card_number=card)
    
    def payment_phone(self, money, phone):
        try:
 
            money = int(money)
            phone_number = re.compile(r"\+\b[\d]{3}-[\d]{2}-[\d]{3}-[\d]{2}-[\d]{2}\b").match(phone)

            if phone_number is None:
                raise PhoneFormatException("Неправильный формат телефона [+xxx-xx-xxx-xx-xx]")
            if (money <= 0):
                raise ValueError
           

            phone_number = phone_number.group(0)

        except PhoneFormatException as err:
            raise err
        except ValueError:
            raise InputFormatException(f"Неправильный формат ввода: {str(money) if money else '[empty]'}")

        return self._model.payment_phone(money=money, phone=phone)
    
    def get_transfers_info(self):
        return self._model.get_transfers_info()
    
    def withdrawal(self, money):
        try:
            money = int(money)
        except ValueError:
            raise InputFormatException(f"Неправильный формат ввода: {str(money) if money else '[empty]'}")
        
        return self._model.withdrawal(money=money)