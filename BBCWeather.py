import constants
import functions

# 3. BBC Weather

def getweather(url, request, soup):

    check_day = False
    tonight_check = soup.find("span", {"class": "wr-date"}).get_text()

    # Condition
    if tonight_check == "Tonight":
        check_day = False
    else:
        check_day = True

    # Whole Day:
    if check_day is True:
        high_temperature = soup.find("span", {"class": "wr-value--temperature--c"}).get_text()
        low_temperature = soup.find("span", {"class": "wr-day-temperature__low-value"}).get_text()[0:3]

        # Format
        BBCWeather_high_temperature = functions.format_variable(high_temperature)
        BBCWeather_low_temperature = functions.format_variable(low_temperature)

        # Average between high and low
        BBCWeather_average_day_temp = (BBCWeather_high_temperature + BBCWeather_low_temperature) // 2

        # View output:
        # print("Average day temp: ", BBCWeather_average_day_temp)
        #
        # print("High temperature:", high_temperature)
        # print("Today's low temperature is:", low_temperature)

    # Get weather information for the current hour:

    # Temperature:
    BBCWeather_current_temp = soup.find("span",
                                              {"class": "wr-value--temperature wr-temperature--time-slot"}).get_text()

    BBCWeather_current_temp = BBCWeather_current_temp[0:2]

    # Feels like:
    BBCWeather_feelslike = soup.find("span", {
        "class": "wr-time-slot-secondary__feels-like-temperature-value gel-long-primer-bold wr-value--temperature--c"}).get_text()

    # Wind speed and wind description:
    BBCWeather_wind_speed = soup.find("span", {"class": "wr-value--windspeed wr-value--windspeed--mph"}).get_text()

    BBCWeather_wind_speed = float(BBCWeather_wind_speed[0:2])
    BBCWeather_wind_speed_kn = round(BBCWeather_wind_speed * constants.MPH_TO_KN, 1)

    BBCWeather_wind_desc = soup.find("div", {
        "class": "wr-time-slot-secondary__wind-direction wr-time-slot-secondary__bottom-section gel-long-primer"}).get_text()

    # Rainfall:
    BBCWeather_rainchance = soup.find("div", {"class": "wr-u-font-weight-500"}).get_text()
    BBCWeather_rainchance = BBCWeather_rainchance[0:2]

    ## Sunrise / Sunset:
    BBCWeather_sunrise = soup.find("span", {"class": "wr-c-astro-data__sunrise gel-pica-bold gs-u-pl-"}).get_text()
    BBCWeather_sunset = soup.find("span", {"class": "wr-c-astro-data__sunset gel-pica gs-u-pl-"}).get_text()

    # Format variables:
    BBCWeather_current_temp = functions.format_variable(BBCWeather_current_temp)
    BBCWeather_feelslike = functions.format_variable(BBCWeather_feelslike)
    BBCWeather_wind_speed_kn = functions.format_variable(BBCWeather_wind_speed)
    BBCWeather_rainchance = functions.format_variable(BBCWeather_rainchance)

    bbcweather_dict = {
        "temp" : BBCWeather_current_temp,
        "feels like" : BBCWeather_feelslike,
        "wind speed kn": BBCWeather_wind_speed_kn,
        "wind description" : BBCWeather_wind_desc,
        "rain chance" : BBCWeather_rainchance,
        "sunrise" : BBCWeather_sunrise,
        "sunset" : BBCWeather_sunset
    }

    return bbcweather_dict