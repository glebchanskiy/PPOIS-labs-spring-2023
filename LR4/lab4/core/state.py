import os

from lab4.core.serializers import JsonEngine
from lab4.core.serializers import YamlEngine
class State:
    serialize_engin: YamlEngine = None
    card_number: str = None
    pincode: str = None
    monies: int = None

    def __init__(self) -> None:
        path_json = os.path.realpath(os.path.dirname(__file__)) + '/state.yaml'
        self.serialize_engin = YamlEngine(path_json)

        data = self.serialize_engin.deserialize()
        self.card_number = data['card_number']
        self.pincode = data['pincode']
        self.monies = data['monies']

    def dump(self) -> None:
        self.serialize_engin.serialize(
            {
                'card_number': self.card_number,
                'pincode': self.pincode,
                'monies': self.monies
            }
        )

    def __del__(self) -> None:
        self.dump()
