# weather-averager
This is a python project that collects weather data from the 4 following sources: OpenWeather API, MetOffice Weather API, BBC Weather website, yrno website, as well as the mooon from timeanddate.com

The output is an average of the weather variables/more explanatory weather output due to unique elements from each API/website

You will require your own API key for OpenWeather, as well as your own API 'id' and 'secret' for MetOffice

main.py uses the other .py files to create the variables and give the output

MetOffice weather uses the 'significantweathercodes.json' and 'uv index codes.json'

There will be errors when you run the code as I have taken out my API codes and left other variables needing to be assigned a value before the code is operational:

In main.py:
line 20 asks the user for their name as an input and then functions.py uses this input to assign the latitude, longitude, BBC weather url, and the yrno url
line 38 requires your OpenWeather API key

In functions.py:
line 14-18 is where you must configure your name, latitude, longitude, bbc weather url for the location you want, and the yrno url for the location you want. This will be then be used by main.py

In MetOffice.py:
line 16 and 17 is where you enter your MetOffice id and secret
