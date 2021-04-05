import ujson
import utime
import urequests as requests


class UDatetime:

    def __init__(self, debug=False):
        self.debug = debug
        self.__response = None
        self.__utc_time = 0


    def utc_time(self):
        self.__response = requests.get("http://api.open-notify.org/iss-now.json")
        self.__utc_time = ujson.loads(self.__response.content.decode('utf-8'))["timestamp"]

        if self.debug:
            year, month, mday, hour, minute, second, *args = utime.gmtime(self.__utc_time)
            print("Current UTC time [ {}-{:02}-{:02}T{:02}:{:02}:{:02}Z ]".format(year, month, mday, hour, minute, second))

        return self.__utc_time
