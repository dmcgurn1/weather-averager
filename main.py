# Import packages
import requests
from datetime import datetime
import numpy as np
from bs4 import BeautifulSoup

# Import modules
import constants
import functions
import OpenWeather
import MetOffice
import BBCWeather
import YrNo

# Choose where to look for the weather using 'locationpicker' function from 'functions.py'

USER_INPUT = input("Enter name: ")

LATITUDE, LONGITUDE = functions.locationpicker(USER_INPUT)[0:2]
BBCWeatherURL = functions.locationpicker(USER_INPUT)[2]
YrNo_url = functions.locationpicker(USER_INPUT)[3]

print("Running...\n")

#
# print(f"Coordinates for '{USER_INPUT}':",
#       f"({LATITUDE}, {LONGITUDE})"
#       ,"\n")

#-----------------------------------------------------------------------------------------------------------------------
#1
# Open Weather API Parameters

OpenWeather_API_KEY = [enter your openweather api key here in quotes]

OpenWeather_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

OpenWeather_REQUEST_URL = f"{OpenWeather_BASE_URL}?lat={LATITUDE}&lon={LONGITUDE}&&APPID={OpenWeather_API_KEY}"

OpenWeather_response = requests.get(OpenWeather_REQUEST_URL)

# print("Open Weather API:\n",
#       OpenWeather.getweather(OpenWeather_response)
#       ,"\n")

#Open Weather variables
OpenWeather_temp = OpenWeather.getweather(OpenWeather_response)['temp']
OpenWeather_feelslike = OpenWeather.getweather(OpenWeather_response)['feelslike']
OpenWeather_wind_speed_kn = OpenWeather.getweather(OpenWeather_response)['wind speed kn']

#-----------------------------------------------------------------------------------------------------------------------
#2
# Met Office API Parameters

MetOffice_BASE_URL = "https://api-metoffice.apiconnect.ibmcloud.com/v0/forecasts/point/"

MetOffice_Timesteps = 'hourly'

excludeMetadata = False
includeLocation = True

# print("Met Office API:\n",
#       MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)
#       ,"\n")

#Met Office variables
MetOffice_weather_desc = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['description']
MetOffice_temp = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['temp']
MetOffice_feelslike = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['feels like']
MetOffice_wind_speed_kn = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['wind speed kn']
MetOffice_gust_speed_kn = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['gust speed kn']
MetOffice_gust_speed_mph = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['gust speed mph']
MetOffice_rain_chance = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['rain chance']
MetOffice_snow_condition = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['snow condition']
MetOffice_snow_amount = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['snow amount']
MetOffice_uv_index_number = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['uv index number']
MetOffice_uv_index_desc = MetOffice.getweather(MetOffice_BASE_URL, MetOffice_Timesteps, LATITUDE, LONGITUDE, excludeMetadata, includeLocation)['uv index description']

#-----------------------------------------------------------------------------------------------------------------------
#3
# BBC Weather Web-scrape parameters

BBCWeatherURL = BBCWeatherURL

response = requests.get(BBCWeatherURL)

soup = BeautifulSoup(response.content, "html.parser")

# print("BBC Weather (Web scrape):\n",
#       BBCWeather.getweather(BBCWeatherURL, response, soup)
#       ,"\n")

#BBC Weather variables
BBCWeather_temp = BBCWeather.getweather(BBCWeatherURL, response, soup)['temp']
BBCWeather_feelslike = BBCWeather.getweather(BBCWeatherURL, response, soup)['feels like']
BBCWeather_wind_speed_kn = BBCWeather.getweather(BBCWeatherURL, response, soup)['wind speed kn']
BBCWeather_wind_desc = BBCWeather.getweather(BBCWeatherURL, response, soup)['wind description']
BBCWeather_rain_chance = BBCWeather.getweather(BBCWeatherURL, response, soup)['rain chance']
BBCWeather_sunrise = BBCWeather.getweather(BBCWeatherURL, response, soup)['sunrise']
BBCWeather_sunset = BBCWeather.getweather(BBCWeatherURL, response, soup)['sunset']

#-----------------------------------------------------------------------------------------------------------------------
#4
#Yr.no Web-scrape parameters

YrNo_url = YrNo_url

YrNo_request = requests.get(YrNo_url)

YrNo_soup = BeautifulSoup(YrNo_request.content, "html.parser")

# print("Yr.no (Web scrape):\n",
#       YrNo.getweather(YrNo_url, YrNo_request, YrNo_soup)
#       ,"\n")

#YrNo Variables
YrNo_temp = YrNo.getweather(YrNo_url, YrNo_request, YrNo_soup)['temp']
YrNo_feelslike = YrNo.getweather(YrNo_url, YrNo_request, YrNo_soup)['feels like']
YrNo_wind_speed_kn = YrNo.getweather(YrNo_url, YrNo_request, YrNo_soup)['wind speed kn']
YrNo_rainfall_amount = YrNo.getweather(YrNo_url, YrNo_request, YrNo_soup)['rainfall amount']

#-----------------------------------------------------------------------------------------------------------------------
# Moon

moon_url = 'https://www.timeanddate.com/moon/phases/uk/london'
moon_request = requests.get(moon_url)
moon_soup = BeautifulSoup(moon_request.content, 'html.parser')

moon_phase = moon_soup.find_all("td")[1].get_text()

#-----------------------------------------------------------------------------------------------------------------------

# Arrays

# Make empty lists to put variables inside and average
all_temperatures_array = np.array([])
all_feelslike_array = np.array([])
all_wind_speeds_array = np.array([])
all_rain_chance_array = np.array([])

# Adding variables to arrays
all_temperatures_array = np.append(all_temperatures_array,
                                   (OpenWeather_temp, MetOffice_temp, BBCWeather_temp, YrNo_temp))
all_feelslike_array = np.append(all_feelslike_array,
                                (OpenWeather_feelslike, MetOffice_feelslike, BBCWeather_feelslike, YrNo_feelslike))
all_wind_speeds_array = np.append(all_wind_speeds_array,
                                  (OpenWeather_wind_speed_kn, MetOffice_wind_speed_kn, BBCWeather_wind_speed_kn, YrNo_wind_speed_kn))
all_rain_chance_array = np.append(all_rain_chance_array,
                                  (MetOffice_rain_chance, BBCWeather_rain_chance))

#Averages (rounded)
average_temp = round(np.average(all_temperatures_array), 1)
average_feelslike = round(np.average(all_feelslike_array), 1)
average_wind_speed_kn = round(np.average(all_wind_speeds_array), 1)
average_wind_speed_mph = round(average_wind_speed_kn * constants.KN_TO_MPH, 1)
average_rain_chance = round(np.average(all_rain_chance_array), 1)

#Formatted averages
average_temp = functions.format_variable(average_temp)
average_feelslike = functions.format_variable(average_feelslike)
average_wind_speed_kn = functions.format_variable(average_wind_speed_kn)
average_wind_speed_mph = functions.format_variable(average_wind_speed_mph)
average_rain_chance = functions.format_variable(average_rain_chance)

# Output
print("                 Dylan's Weather Program:\n")
print(f"Date: {str(datetime.now())[8:10]}/{str(datetime.now())[5:7]}/{str(datetime.now())[0:4]}, "
       f"Time: {str(datetime.now())[11:16]}")
print("\n Weather:")
print("----------")
print(f"Temperature: {average_temp}°C (Feels like: {average_feelslike}°C)")
print(f"Description: {MetOffice_weather_desc}")
print("\n Wind:")
print("-------")
print(f"Wind description: {BBCWeather_wind_desc}")
print(f"Wind speed: {average_wind_speed_kn}kn ({average_wind_speed_mph}mph)")
print(f"Gust speed: {MetOffice_gust_speed_kn}kn ({MetOffice_gust_speed_mph}mph)")
print("\n Precipitation:")
print("----------------")
print(f"Chance of rain: {average_rain_chance}%")
print(f"Rain amount: {YrNo_rainfall_amount}mm")
if MetOffice_snow_condition is True:
      print(f"Snow amount: {MetOffice_snow_amount}")
print("\n UV:")
print("-----")
print(f"UV Index Code: {MetOffice_uv_index_number} - {MetOffice_uv_index_desc}")
print("\n Sun/Moon:")
print("-----------")
print(f"Sunrise: {BBCWeather_sunrise[-5:]}")
print(f"Sunset: {BBCWeather_sunset[-5:]}")
print(f"Moon: {moon_phase}")