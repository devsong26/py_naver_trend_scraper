import json

from src.utility.file_util import FileUtil
from src.api.naver_api import NaverAPI
from src.utility.time import TimeUtil


class NaverTrendScraper:
    def __init__(self):
        pass

    def scrape(self):
        word_json = FileUtil.get_json_from_file()

        request_json = {
            'startDate': TimeUtil.get_kst_date_one_month_ago(),
            'endDate': TimeUtil.get_kst_now_date(),
            'timeUnit': 'date',
            'keywordGroups': []
        }

        for attribute, value in word_json.items():
            request_json['keywordGroups'] = []
            request_json['keywordGroups'].append({
                'groupName': value,
                'keywords': [value]
            })
            request_json_str = json.dumps(request_json, ensure_ascii=False)
            response = NaverAPI.call_api(request_json_str)
            print(attribute, response)
