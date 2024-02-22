# Original Code :https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# Imports
import requests, json

def getWeatherData(city_name): 
    # Api Key
    api_key = "c76db9ba1f61d57b88d8a19ecb97b283"

    # Base url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = input("Enter city name : ")
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z
        weather_description = z[0]["description"]

        print(x)
        return x 

        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
    else:
        print(" City Not Found ")

if __name__ == "__main__":
    getWeatherData('Null')