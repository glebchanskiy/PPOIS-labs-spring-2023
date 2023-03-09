import os
import json

from lab4.core.serializers.engine import Engine

class JsonEngine(Engine):
    def __init__(self, path) -> None:
        super().__init__(path)

    def deserialize(self) -> dict:
        with open(self._path, "r") as file:
            data = json.load(file)

        return data

    def serialize(self, data: dict) -> None:
        with open(self._path, "w") as file:
            json.dump(data, file, indent=4)
