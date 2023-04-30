import constants
import functions

# 4. Yr.no

def getweather(url, request, soup):

    #Temperature
    YRNO_current_temp = soup.find("span", {"class": "temperature temperature--warm"}).get_text()
    YRNO_current_temp = YRNO_current_temp[-3:]

    #Feels like
    YRNO_feels_like = soup.find("div", {"class": "feels-like-text"}).get_text()
    YRNO_feels_like = YRNO_feels_like[-3:]

    #Wind speed
    YRNO_wind_speed = soup.find("span", {"class": "wind__value now-hero__next-hour-wind-value"}).get_text()
    YRNO_wind_speed = float(YRNO_wind_speed)
    YRNO_wind_speed_kn = YRNO_wind_speed * constants.MS_TO_KN
    YRNO_wind_speed_kn = round(YRNO_wind_speed_kn, 1)

    #Rainfall
    YRNO_rainfall_amount = soup.find("span", {"class": "now-hero__next-hour-precipitation-value"}).get_text()

    #Clean up scraped text
    YRNO_current_temp = functions.format_variable(YRNO_current_temp)
    YRNO_feels_like = functions.format_variable(YRNO_feels_like)
    YRNO_wind_speed_kn = functions.format_variable(YRNO_wind_speed_kn)
    YRNO_rainfall_amount = functions.format_variable(YRNO_rainfall_amount)

    yrno_dict = {
        "temp" : YRNO_current_temp,
        "feels like" : YRNO_feels_like,
        "wind speed kn" : YRNO_wind_speed_kn,
        "rainfall amount" : YRNO_rainfall_amount
    }

    return yrno_dict
