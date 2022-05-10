from datetime import datetime
import tkinter as tk
import requests

class API():
    
    api_key = f"de24ba549fe9b21406f59888864dfaf2"  
    
    def __init__(self):
         
         self.zip_code = zip_code
         self.api_key = self.api_key
         
    def wind_direction(self,wind):
        if wind >= 0 and wind <22.5:
            return "N"
        elif wind >= 22.5 and wind < 67.5:
            return "NE"
        elif wind >= 67.5 and wind < 112.5:
            return "E"
        elif wind >= 112.5 and wind < 157.5:
            return "SE"
        elif wind >= 157.5 and wind <202.5:
            return "S"
        elif wind >= 202.5 and wind < 247.5:
            return "SW"
        elif wind >= 247.5 and wind <292.5:
            return "W"
        elif wind >= 292.5 and wind <337.5:
            return "NW"
        else:
            return "N"
    def cloudy(self,cloud):
        print(cloud)
        if cloud >= 0 and cloud <10:
            return "Clear"
        elif cloud >= 10 and cloud <30: 
            return "Mostly Sunny"
        elif cloud >= 30 and cloud <70:
            return "partly cloudy"
        elif cloud >= 70 and cloud <90:
            return "Mostly Cloudy"
        elif cloud >= 90 and cloud <=100:
            return "Cloudy"


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
        date = response["minutely"][0]["dt"]
        print(date)
        offset = response["timezone_offset"]
        date = date+offset
        date = datetime.utcfromtimestamp(date) 
        date = date.strftime("%b %d %Y %H:%M")
        timezone = response['timezone']
        daily_pop = response['daily'][0]["pop"]
        current_rain = response['minutely'][0]["precipitation"]
        daily_wind_speed = response['daily'][0]['wind_speed']
        current_wind_speed = response["current"]["wind_speed"]
        daily_wind_dir = response['daily'][0]['wind_deg']
        current_wind_dir = response['current']['wind_deg']
        daily_cloud_cover = response['daily'][0]['clouds']
        current_cloud_cover = response['current']['clouds']
        day_temp = response['daily'][0]['feels_like']['morn']
        eve_temp = response['daily'][0]['feels_like']['eve']
        night_temp = response['daily'][0]['feels_like']['night']
        daytemp = int((day_temp * 1.8) - 459.67)
        evetemp = int((eve_temp * 1.8) - 459.67)
        nighttemp = int((night_temp * 1.8) - 459.67)
        dwind_dir = self.wind_direction(daily_wind_dir)
        cwind_dir = self.wind_direction(current_wind_dir)
        des_day_clouds = self.cloudy(daily_cloud_cover)
        des_cur_clouds = self.cloudy(current_cloud_cover)
        one_day_forcast = response['daily'][0]['temp']['max']
        two_day_forcast = response['daily'][1]['temp']['max']
        three_day_forcast = response['daily'][2]['temp']['max']
        four_day_forcast = response['daily'][3]['temp']['max']
        five_day_forcast = response['daily'][4]['temp']['max']              
        return {
            "date" : str(date),
             "min" : temp_min,
             "max" : temp_max,
             "probability" : daily_pop,
             "isitrain":current_rain,
             'dwindspeed': daily_wind_speed,
             'cwindspeed': current_wind_speed,
             'dwind_dir': dwind_dir,
             'cwind_dir': cwind_dir,
             'dcloud_cover':des_day_clouds,
             'ccloud_cover':des_cur_clouds,
             'timezone':timezone,
             'daytemp':daytemp,
             'evetemp':evetemp,
             'nighttemp':nighttemp,
             'one_max_forcast':one_day_forcast,
             'two_max_forcast':two_day_forcast,
             'three_max_forcast':three_day_forcast,
             'four_max_forcast':four_day_forcast,
             'five_max_forcast':five_day_forcast,
        }


f = open("zip_code_update.txt", "r")
user_zip = f.read()
zip_code = user_zip
api = API()
current_weather = api.get_current_weather()
city = current_weather["city"]
day_weather = api.get_daily_weather(city)
print(day_weather)