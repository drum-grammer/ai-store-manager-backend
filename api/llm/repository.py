import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import GoogleConfig


def _get_gspread():
    cred_text = GoogleConfig.instance().GOOGLE_CREDENTIAL
    cred_json = json.loads(cred_text)
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(cred_json, scope)
    client = gspread.authorize(credentials)
    return client


def get_sync_table():
    sheet_key = "1CNc_eobkgeklG1LhaAa3GLbKfVoPupZ4WMsRttWiBF4"
    client = _get_gspread()
    try:
        gsheet = client.open_by_key(sheet_key)
        data = gsheet.worksheet('user')
        return data.get_all_records(default_blank=None, numericise_ignore=['all'])
    except Exception as e:
        print(e)
        return None
