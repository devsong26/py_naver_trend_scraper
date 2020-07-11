import os


class PropertyUtil:
    @classmethod
    def get_value_from_os(cls, key):
        return os.environ[key]
