# weather-averager
This is a python project that collects weather data from the 4 following sources: 

OpenWeather API, MetOffice Weather API, BBC Weather website, yrno website,

(as well as the moon phase from timeanddate.com)

The variables are collected and put into numpy arrays and then at the end they are averaged.

The output is either an average of the weather variables, if available, or a singular element from one of the sources

-> (e.g. temperature comes from all 4 sources and then averaged, rain chance comes from 2 sources and then averaged,
but gust speed is only present on the MetOffice API so it is not an average)

You will require your own API key for OpenWeather, as well as your own API 'id' and 'secret' for MetOffice

main.py uses the other .py files to create the variables and give the output

MetOffice weather uses the 'significantweathercodes.json' and 'uv index codes.json'


There will be errors when you run the code as I have taken out my API codes and left other variables needing to be assigned a value before the code is operational:

In main.py:

line 20 asks the user for their name as an input and then functions.py uses this input to assign the latitude, longitude, BBC weather url, and the yrno url

line 38 requires your OpenWeather API key

line 125 is where the url for the moon phase is located, by default it is 'london', but this can be changed to other cities (e.g. 'https://www.timeanddate.com/moon/phases/france/paris')

In functions.py:

line 14-18 is where you must configure your name, latitude, longitude, BBC weather url for the location you want, and the yrno url for the location you want. This will be then be used by main.py


In MetOffice.py:

line 16 and 17 is where you enter your MetOffice id and secret
