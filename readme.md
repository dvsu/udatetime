### Usage  
  
- Put `udatetime.py` file in `lib` folder.  
- Import it from `main.py` as shown in the example below.
  
<br>

### Example  
  
    from udatetime import UDatetime


    t = UDatetime()
    print(t.utc_time()) # print Unix epoch time in seconds
  
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

