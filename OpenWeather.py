import constants
import functions

# 1. OpenWeather

def getweather(request):
    if request.status_code == 200:

        data = request.json()

        weather_key = data['weather'][0]

        #Temperature
        raw_temp = data['main']['temp']
        raw_temp = float(raw_temp) - constants.KELVIN_OFFSET
        raw_temp = round(raw_temp, 1)

        #Feels like
        feelslike = data['main']['feels_like']
        feelslike = float(feelslike) - constants.KELVIN_OFFSET
        feelslike = round(feelslike, 1)

        #Wind speed (knots)
        wind_speed = data['wind']['speed']
        wind_speed = float (wind_speed)
        wind_speed_kn = wind_speed * constants.MS_TO_KN
        wind_speed_kn = round(wind_speed_kn, 1)

    else:
        print("OpenWeather API request unsuccessful")
        exit()

    #Format variables
    raw_temp = functions.format_variable(raw_temp)
    feelslike = functions.format_variable(feelslike)
    wind_speed_kn = functions.format_variable(wind_speed_kn)

    openweather_dict = {
        "temp" : raw_temp,
        "feelslike" : feelslike,
        "wind speed kn" : wind_speed_kn,
    }

    return openweather_dict