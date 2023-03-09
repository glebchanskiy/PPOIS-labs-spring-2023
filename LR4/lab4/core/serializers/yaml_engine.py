import yaml
from yaml import CLoader as Loader, CDumper as Dumper
import os

from lab4.core.serializers.engine import Engine

class YamlEngine(Engine):
    def __init__(self, path) -> None:
        super().__init__(path)

    def deserialize(self) -> dict:
        with open(self._path, "r") as file:
            data = yaml.load(file, Loader=Loader)

        return data

    def serialize(self, data: dict) -> None:
        with open(self._path, "w") as file:
            yaml.dump(data, file, indent=4)
