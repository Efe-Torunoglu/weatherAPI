# Original Code :https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# Imports
import requests, json

def requestFromFile():
    
    # Open File and Use getWeatherData
    with open("city_request.txt") as f:
        city = f.read()
        getWeatherData(city)
        
def getWeatherData(city_name):
    
    # Api Key
    api_key = "c76db9ba1f61d57b88d8a19ecb97b283"

    # Base url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
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
        
        # Dump JSON
        with open("weather_information.json",'w') as file:
            json.dump(x,file)
    
    else:
        print(" City Not Found ")

if __name__ == "__main__":
    
    while True:
        
        
        # Open Text,
        try:
            f = open('city_request.txt', 'r')
            city = f.read().strip('\n')
            if city != "":
                getWeatherData(city)
        except FileNotFoundError:
            pass