import locale
from datetime import datetime

from common.constant.time_zone import seoul_timezone


def get_today_string():
    locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')
    return datetime.now(seoul_timezone).strftime('%Y.%m.%d (%a)')
