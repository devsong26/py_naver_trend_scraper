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


if __name__ == '__main__':
    unittest.main()
