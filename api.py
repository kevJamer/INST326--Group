
from tkinter import *
import requests



class API():
    
    api_key = f"f2a3f0a69be836e5147d815b9ff939ba"  
    
    def __init__(self):
         
         self.zip_code = zip_code
         self.api_key = self.api_key


    def get_current_weather(self):
    
   
        geo = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code}&appid={self.api_key}"
        geocoder = requests.get(geo).json()
        lat = geocoder['lat']
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
    
    
zip_code = "20742"
api = API()
weather = api.get_current_weather()


