import unittest

from src.scraper.naver_trend import NaverTrendScraper


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.naver_trend_scraper = NaverTrendScraper()

    def test_scrape(self):
        self.naver_trend_scraper.scrape()


if __name__ == '__main__':
    unittest.main()
