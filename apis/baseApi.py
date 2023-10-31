import sys
import datetime as date

class BaseApi(object):

    @property
    def headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': self.token
        }
    
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
        
    def __init__(self):
        try:
            self.host = sys.argv[3] # "https://api.meetime.com.br"
            self.stage = sys.argv[4] # "/v2"
            self.token = sys.argv[5] # "<TOKEN_AUTHORIZATION>"
            self.date_format = sys.argv[6] # "%Y-%m-%d"
            self.items_by_request = sys.argv[7] # 100
            self.show_deleted = sys.argv[8] # "false"
        except Exception as err:
            raise SystemExit("Exception: Any those sys.argv[]=[host, stage, token, date_format, items_by_request, show_deleted] is required.")

        try:
            self.show_deleted = sys.argv[8] # "false"
        except Exception as err:
            raise SystemExit("Exception: sys.argv[8]=<show_deleted> is required. Message: " + str(err.args[0]))

        self.dtToday = date.datetime.today().strftime(self.date_format)
        self.dtTodayD1 = (date.datetime.today() - date.timedelta(days=1)).strftime(self.date_format)