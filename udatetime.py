import utime
from time import sleep
from machine import RTC


class Datetime:

    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.minute = None
        self.second = None


class udatetime:

    def __init__(self):
        self.__datetime = Datetime()
        self.__timetuple = ()
        self.__seconds = 0
        self.__rtc = RTC()
        self.__rtc.ntp_sync("pool.ntp.org") # sync to UTC time
        while not self.__rtc.synced():
            sleep(1)
    
    # get_current_time() will be the core method to be called to get latest datetime 
    # and update the values of corresponding attributes
    def get_current_time(self):
        self.__timetuple = self.__rtc.now()
        self.__datetime.year, self.__datetime.month, self.__datetime.day, self.__datetime.hour, self.__datetime.minute, self.__datetime.second, *args = self.__timetuple

    def utcnow(self) -> udatetime:
        self.get_current_time()
        return self

    def utc_seconds(self) -> int:
        self.get_current_time()
        self.__seconds = utime.mktime(self.__timetuple)
        return self.__seconds

    def year(self) -> int:
        return self.__datetime.year

    def month(self) -> int:
        return self.__datetime.month

    def day(self) -> int:
        return self.__datetime.day

    def hour(self) -> int:
        return self.__datetime.hour

    def minute(self) -> int:
        return self.__datetime.minute

    def second(self) -> int:
        return self.__datetime.second

    def strftime(self, dt_format:str) -> str:

        dt_map = {
            "%Y": "{:4}".format(self.__datetime.year),
            "%m": "{:02}".format(self.__datetime.month),
            "%d": "{:02}".format(self.__datetime.day),
            "%H": "{:02}".format(self.__datetime.hour),
            "%M": "{:02}".format(self.__datetime.minute),
            "%S": "{:02}".format(self.__datetime.second)
        }

        for key, value in dt_map.items():
            if key in dt_format:
                dt_format = dt_format.replace(key, value)

        return dt_format

    def __str__(self) -> str:
        return "{:4}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(self.__datetime.year, self.__datetime.month, self.__datetime.day, self.__datetime.hour, self.__datetime.minute, self.__datetime.second)
     