class NoCardException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoPincodeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class WrongPincodeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class WrongCardException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class InsufficientFoundsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PhonePaymentException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PhoneFormatException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InputFormatException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

