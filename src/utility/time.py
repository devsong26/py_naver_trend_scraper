from pytz import timezone
from datetime import datetime
from datetime import timedelta


class TimeUtil:
    @classmethod
    def get_kst_now_date(cls):
        kst = timezone('Asia/Seoul')
        now = datetime.now().astimezone(kst).strftime('%Y-%m-%d')
        return now

    @classmethod
    def convert_datetime_to_str(cls, date):
        converted_date_str = date.strftime("%Y-%m-%d")[0:10]
        return converted_date_str

    @classmethod
    def get_kst_date_one_month_ago(cls):
        kst = timezone('Asia/Seoul')
        now = datetime.now().astimezone(kst)
        one_month_ago = now - timedelta(days=31)
        return one_month_ago.strftime('%Y-%m-%d')
