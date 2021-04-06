### Description  
  
Most controllers that support MicroPython do not have built-in RTC. 
For time-sensitive application, e.g. remote and complex logic control,
real datetime could improve the precision of event logging and monitoring. 
This simple datetime module utilizes `urequests` module to make an API call to 
**Open Notify** <http://open-notify.org/>. Current Unix timestamp is based on latest 
valid location of the International Space Station (ISS).
  
<br>

### Usage  
  
- Put `udatetime.py` file in `lib` folder.  
- Import it from `main.py` as shown in the example below.
  
<br>

### Example  
  
```python
from udatetime import UDatetime


t = UDatetime()
print(t.utc_time()) # print Unix epoch time in seconds
```
  
<br>
  
### Dependencies  
  
- urequests <https://github.com/micropython/micropython-lib/tree/master/urequests>
  
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

