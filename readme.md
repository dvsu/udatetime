### Description  
  
Simple `datetime` module written in MicroPython for Pycom board
  
<br>

### Usage  
  
- Put `udatetime.py` file in `lib` folder.  
- Import it from `main.py` as shown in the example below.
  
<br>

### Example  
  
```python
from udatetime import udatetime

# establish wireless connection
# ...
# ...

datetime = udatetime()
print(datetime.utc_seconds()) # print Unix epoch time in seconds

# get utc time
print(datetime.utcnow())

# utc time as string
print(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
```
  
<br>
  
### Dependencies  
  
- Pycom RTC module <https://docs.pycom.io/firmwareapi/pycom/machine/rtc/>
  
<br>
  
### Limitation  
- Require internet connection
  
<br>
  
### Tested On
  
- Pycom WiPy3.0 mounted on Pycom Expansion Board 3.0
  
<br>

### Logs  
  
05/04/2021 
- Add basic function to get Unix epoch time in seconds

07/05/2021 
- Change datetime logic based on Pycom RTC module and NTP sync 