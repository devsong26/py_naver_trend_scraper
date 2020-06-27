from datetime import datetime
from pytz import timezone


class TimeUtil:
    @staticmethod
    def get_kst_now_date():
        kst = timezone('Asia/Seoul')
        now = datetime.now().astimezone(kst).strftime('%Y-%m-%d')
        return now

    @staticmethod
    def convert_datetime_to_str(date):
        converted_date_str = date.strftime("%Y-%m-%d")[0:10]
        return converted_date_str
