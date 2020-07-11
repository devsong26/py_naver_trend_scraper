from src.utility.file_util import FileUtil


class NaverTrendScraper:
    def __init__(self):
        pass

    def scrape(self):
        word_json = FileUtil.get_json_from_file()
        print(word_json)

        
        # TODO 라인 별로 워드를 네이버 api 호출한다.
        pass
