import urllib.request
from urllib.error import HTTPError
from src.utility.property import PropertyUtil
from src.utility.file_util import FileUtil


class NaverAPI:
    API_URL = "https://openapi.naver.com/v1/datalab/search"

    @classmethod
    def __set_up(cls):
        if hasattr(cls, "CLIENT_ID") and hasattr(cls, "CLIENT_SECRET"):
            return

        os_key_json = FileUtil.get_os_property_key_json()
        naver_key_json = os_key_json["naver"]
        cls.CLIENT_ID = PropertyUtil.get_value_from_os(naver_key_json["CLIENT_ID"])
        cls.CLIENT_SECRET = \
            PropertyUtil.get_value_from_os(naver_key_json["CLIENT_SECRET"])

    @classmethod
    def call_api(cls, request_body):
        # keywordGroups의 아이템이 5개 이상이면 안 된다.

        cls.__set_up()
        request = urllib.request.Request(cls.API_URL)
        request.add_header("X-Naver-Client-Id", cls.CLIENT_ID)
        request.add_header("X-Naver-Client-Secret", cls.CLIENT_SECRET)
        request.add_header("Content-Type", "application/json")

        try:
            response = urllib.request.urlopen(request, data=request_body.encode("utf-8"))
        except HTTPError as err:
            return err.code, None

        res_code = response.getcode()
        response_body = None

        if res_code == 200:
            response_body = response.read()
            response_body = response_body.decode('utf-8')

        return res_code, response_body
