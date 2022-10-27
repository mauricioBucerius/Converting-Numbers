# Converting-Numbers

Repository in which you can find scripts for converting numbers or other stuff

## 📐 How-To
When you want to convert numbers with a large scale to a human-readable format, 
you can use "zahl2prefix.py".
This script converts a number to a string and adds a matching Prefix for a less sacrifing reading.

### Converting Numbers in Strings with Prefix
For Converting of a large number, doesn't matter if positive or negative, you can use the function
*zahl2prefix*:
-`zahl2prefix(1000) -> 1 k`
- `zahl2prefix(-52400) -> 52.4 k`
- `zahl2prefix(0.000003452) -> 3.5 u`

Furthermore if you want to round the output value, you can add the number of decimal place as an 2nd
Argument. The default value amounts to one:
- `zahl2prefix(-36.2265990, 0) -> -36`
- `zahl2prefix(-36.22658904607586, 5) -> -36.22659`

### Converting Strings with Prefix in floating value 
The function *prefix2zahl* converts a string with an optional prefix at the end to a floating value
- `prefix2zahl("2.34 k") -> 2340.0`
- `prefix2zahl("-0.1 m") -> -0.0001`
- `prefix2zahl("345.67 u") -> 0.00034567`

### Converting Time
With the function *time2prefix* you can convert a floating value in seconds into a human-readable. The 
formating represents minutes, hours and prefix below seconds for example milli and micro. 
- `time2prefix(7198.5) -> 01:00:59.975 h`
- `time2prefix(125.5) -> 02:05.120500 min`
