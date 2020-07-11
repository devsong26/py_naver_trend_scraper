import unittest

from src.utility.property import PropertyUtil
from src.utility.file_util import FileUtil


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.os_key_json = FileUtil.get_os_property_key_json()

    def test_get_value_from_os(self):
        db_key_json = self.os_key_json["db"]
        db_username = PropertyUtil.get_value_from_os(db_key_json["username"])
        db_password = PropertyUtil.get_value_from_os(db_key_json["password"])
        print(db_username)
        print(db_password)


if __name__ == '__main__':
    unittest.main()
