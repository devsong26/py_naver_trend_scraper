import unittest

from src.utility.file_util import FileUtil


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_file_path(self):
        expected_file_path = \
            'C:\\Users\\yhnkw\\Documents\\git\\github\\py_naver_trend_scraper\\resources\\word.json'
        rtn_file_path = FileUtil.get_file_path()
        self.assertEqual(expected_file_path, rtn_file_path)
        pass

    def test_get_json_from_file(self):
        json_data = FileUtil.get_json_from_file()
        print(json_data)
        self.assertEqual(False, not json_data)

    def test_get_os_property_key_json(self):
        json_data = FileUtil.get_os_property_key_json()
        db_json = json_data['db']
        self.assertEqual(db_json["username"], "MYSQL_DB_USERNAME")
        self.assertEqual(db_json["password"], "MYSQL_DB_PASSWORD")


if __name__ == '__main__':
    unittest.main()
