import json
import pickle
from abc import ABCMeta, abstractmethod
from pathlib import Path


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, obj: object, file_name: str) -> None:
        pass

    @abstractmethod
    def deserialize(self, file_name: str) -> object:
        pass


class JsonSerialization(SerializationInterface):
    def serialize(self, obj: object, file_name: str) -> None:
        with open(file_name, "w") as f:
            json.dump(obj, f, ensure_ascii=False)

    def deserialize(self, file_name: str) -> object:
        path = Path(file_name)
        if not path.exists():
            return None

        with open(file_name, "r") as f:
            restored_data = json.load(f)
        return restored_data


class BinSerialization(SerializationInterface):
    def serialize(self, obj: object, file_name: str) -> None:
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    def deserialize(self, file_name: str) -> object:
        path = Path(file_name)
        if not path.exists():
            return None

        with open(file_name, "rb") as f:
            restored_data = pickle.load(f)
        return restored_data


if __name__ == '__main__':
    data = {"taskseriliazation": 567}

    json_serialization = JsonSerialization()
    json_serialization.serialize(data, 'data.json')
    print(json_serialization.deserialize('data.json'))

    bin_serialization = BinSerialization()
    bin_serialization.serialize(data, 'data.bin')
    print(bin_serialization.deserialize('data.bin'))
