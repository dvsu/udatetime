import ujson
import utime
import urequests as requests


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
        
        # The latest UTC time can be extracted from returned JSON data of ISS API call.
        # At the same time, the internal counter of the device will be started once the device is ON,
        # and can be extracted from utime.time(). The number obtained from this method will be stored
        # as current offset.

        # Every API call will introduce some time delay and its impact can be minimized by estimating
        # latest UTC time obtained from last API call, then added by latest counter and substracted by
        # recorded offset.
        #       estimated UTC time = UTC time from API call + utime.time() - offset

        self.sync_time()
        self.__seconds = 0
        self.__datetime = Datetime()
        self.__sync_period = 3600 # sync time every 1 hour
        self.__sync_tracker = 0

    # Time tracking for time sync to ensure the timestamp is accurate
    def time_tracker(self) -> None:
        
        if self.__sync_tracker < self.__sync_period:
            self.__sync_tracker = utime.time() - self.__offset
        else:
            self.sync_time()
            self.__sync_tracker = 0

    def utc_seconds(self) -> int:
        try:
            self.time_tracker()

            self.__seconds = self.__base_utc + utime.time() - self.__offset
            return self.__seconds

        except Exception as e:
            print("Failed to get UTC seconds")
            print(e)

    def utcnow(self) -> udatetime:

        self.fromtimestamp(self.utc_seconds())
        return self

    def fromtimestamp(self, seconds:int) -> udatetime:

        self.__datetime.year, self.__datetime.month, self.__datetime.day, self.__datetime.hour, self.__datetime.minute, self.__datetime.second, *args = utime.gmtime(seconds)
        return self

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

    def sync_time(self) -> None:
        try:
            response = requests.get("http://api.open-notify.org/iss-now.json")
            self.__base_utc = ujson.loads(response.content.decode('utf-8'))["timestamp"]
            self.__offset = utime.time()

        except Exception as e:
            print("Not connected to network. Failed to sync time.\n{}".format(e))

    def __str__(self) -> str:
        return "{:4}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(self.__datetime.year, self.__datetime.month, self.__datetime.day, self.__datetime.hour, self.__datetime.minute, self.__datetime.second)
        
