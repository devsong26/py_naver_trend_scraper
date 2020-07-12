import unittest

from src.utility.time import TimeUtil


class MyTestCase(unittest.TestCase):
    def test_get_kst_date_one_month_ago(self):
        expected_one_month_ago = "2020-06-11"
        rtn_one_month_ago = TimeUtil.get_kst_date_one_month_ago()

        self.assertEqual(rtn_one_month_ago, expected_one_month_ago)


if __name__ == '__main__':
    unittest.main()
