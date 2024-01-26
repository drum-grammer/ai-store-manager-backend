from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def list(cls):
        return list(cls)

    @classmethod
    def name_list(cls):
        return [item.name for item in cls]
