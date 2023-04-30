import requests
import json
from datetime import datetime
import os
import constants
import functions

# 2. Met Office

def getweather(baseUrl, timesteps, latitude, longitude, excludeMetadata, includeLocation):

    url = baseUrl + timesteps

    headers = {
        'accept': "application/json",
        "x-ibm-client-id": [enter your metoffice weather id here in quotes],
        "x-ibm-client-secret": [enter your metoffice weather secret here in quotes]
    }

    params = {
        'excludeParameterMetadata': excludeMetadata,
        'includeLocationName': includeLocation,
        'latitude': latitude,
        'longitude': longitude,
    }

    req = requests.get(url, headers=headers, params=params)

    met_json = json.loads(req.text)

    current_time = str(datetime.date(datetime.now())) + str('T') + str(datetime.time(datetime.now()))[0:3] + str('00Z')
    json_key = req.json()['features'][0]['properties']['timeSeries']

    print(json_key)

    # Check for current date and time in data
    for i in range(25):
        if json_key[i]['time'] == current_time:

            # Significant weather code
            with open(os.path.join("significantweathercodes.json"), 'r+') as MetOffice_Significant_Weather_Codes_File:
                MetOffice_Significant_Weather_Codes = json.load(MetOffice_Significant_Weather_Codes_File)

            weather_code = json_key[i]['significantWeatherCode']
            weather_code = str(weather_code)
            weather_code = MetOffice_Significant_Weather_Codes[weather_code]

            # Raw temp
            raw_temp = json_key[i]['screenTemperature']
            raw_temp = round(raw_temp, 1)

            # Feels like temp
            feels_like = json_key[i]['feelsLikeTemperature']
            feels_like = round(feels_like, 1)

            # Wind direction
            #wind_direction = json_key[i]['windDirectionFrom10m']

            # Wind speed
            wind_speed = json_key[i]['windSpeed10m']
            wind_speed_kn = float(wind_speed)
            wind_speed_kn = round(wind_speed_kn, 1)

            # Gust speed
            gust_speed = json_key[i]['windGustSpeed10m']
            gust_speed_kn = round(gust_speed, 1)
            gust_speed_mph = round(gust_speed_kn * constants.KN_TO_MPH, 1)

            # Chance of rain (rounded to nearest 10%)
            rain_chance = json_key[i]['probOfPrecipitation']
            rain_chance = float(rain_chance)
            #rain_chance = int(round(float(rain_chance) / 100, 1) * 100)

            # Chance of snow (if amount > 0)
            snow_amount = json_key[i]['totalSnowAmount']
            snow_condition = False

            if snow_amount > 0:
                snow_condition = True

            # UV index
            with open(os.path.join("uv index codes.json"),'r+') as MetOffice_UV_Index_Codes_File:
                MetOffice_UV_Index_Codes = json.load(MetOffice_UV_Index_Codes_File)

            uv_index_number = json_key[i]['uvIndex']

            # If UV Index > 11 display the highest warning
            if int(uv_index_number) > 11:
                uv_index_desc = "Extreme. Avoid being outside during midday hours. Shirt, sunscreen and hat essential."
            # Otherwise display the corresponding description for the index number
            else:
                uv_index_desc = str(uv_index_number)
                uv_index_desc = MetOffice_UV_Index_Codes[uv_index_desc]

            gust_speed_kn = round(gust_speed_kn, 1)

            # Convert variables into integers if they are round e.g. 8.0 -> 8
            raw_temp = functions.format_variable(raw_temp)
            feels_like = functions.format_variable(feels_like)
            wind_speed_kn = functions.format_variable(wind_speed_kn)
            gust_speed_kn = functions.format_variable(gust_speed_kn)
            gust_speed_mph = functions.format_variable(gust_speed_mph)

            # Put all variables in a global dictionary to be accessed later for the output
            met_dict = {
                'description' : weather_code,
                'temp' : raw_temp,
                'feels like' : feels_like,
                'wind speed kn' : wind_speed_kn,
                'gust speed kn' : gust_speed_kn,
                'gust speed mph' : gust_speed_mph,
                'rain chance' : rain_chance,
                'snow condition' : snow_condition,
                'snow amount' : snow_amount,
                'uv index number' : uv_index_number,
                'uv index description' : uv_index_desc
            }

            return met_dict
