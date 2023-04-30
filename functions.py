from math import ceil, floor

def locationpicker(input):

    #Format input
    input = str(input)
    input = input.lower()

    #Check that input is valid
    if not input.isalpha():
        print("Error: Input invalid")
        exit()

    if input == [enter your name here]:
        LATITUDE = [enter your latitude here]
        LONGITUDE = [enter your longitude here]
        BBCWeatherURL = [enter bbc weather url for your location here] #https://www.bbc.co.uk/weather
        YRNO_URL = [enter yrno weather url for your location here] #https://www.yr.no/en

    else:
        print("Error: Name not found")
        exit()

    return LATITUDE, LONGITUDE, BBCWeatherURL, YRNO_URL


def format_variable(variable):

    #Covert variable to string
    variable = str(variable)

    #Remove any degree symbols, percentage signs, or spaces
    variable = variable.strip("°% ")

    #Conver to a float
    variable = float(variable)

    #If the float is a whole number, convert it to a integer
    if variable % 1 == 0:
        variable = int(variable)

    return variable
