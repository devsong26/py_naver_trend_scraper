import urllib.request
from urllib.error import HTTPError


class NaverAPI:
    def __init__(self):
        pass

    @staticmethod
    def call_api(api_url, client_id, client_secret, request_body):
        request = urllib.request.Request(api_url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
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
