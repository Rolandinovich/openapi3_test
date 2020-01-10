from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def get_choices(cls):
        return [(item.name, item.value) for item in cls]

    @classmethod
    def get_value(cls, name):
        value = [item.value for item in cls if item.name == name][0]
        return value

    @classmethod
    def get_name(cls, value):
        name = [item.name for item in cls if item.value == value][0]
        return name
