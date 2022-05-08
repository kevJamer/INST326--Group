from datetime import datetime
import tkinter as tk
import requests

class API():
    
    api_key = f"de24ba549fe9b21406f59888864dfaf2"  
    
    def __init__(self):
         
         self.zip_code = zip_code
         self.api_key = self.api_key


    def get_current_weather(self):
    
   
        geo = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code}&appid={self.api_key}"
        geocoder = requests.get(geo).json()
        lat = geocoder["lat"]
        lon = geocoder['lon']
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url).json() 
        temperature = response['main']['temp']
        city_name = response['name']
        temperature = int((temperature * 1.8) - 459.67)
        
        return {
            'temp' : temperature,
            'city' : city_name
        }
    def get_daily_weather(self,city_name):
        
        geo = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code}&appid={self.api_key}"
        geocoder = requests.get(geo).json()
        lat = geocoder['lat']
        lon = geocoder['lon']
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=&appid={self.api_key}"
        response = requests.get(url).json() 
        city = city_name
        temp_min = response["daily"]
        temp_min = temp_min[0]["temp"]["min"]
        temp_max= response['daily'][0]["temp"]["max"]
        temp_min = int((temp_min * 1.8) - 459.67)
        temp_max = int((temp_max * 1.8) - 459.67)
        date = response["daily"][1]["dt"]
        offset = response["timezone_offset"]
        date = date-offset
        date = datetime.fromtimestamp(date) 
        return {
            "date" : str(date),
             "min" : temp_min,
             "max" : temp_max
        }


f = open("zip_code_update.txt", "r")
user_zip = f.read()
zip_code = user_zip
api = API()
current_weather = api.get_current_weather()
city = current_weather["city"]
day_weather = api.get_daily_weather(city)
print(day_weather)