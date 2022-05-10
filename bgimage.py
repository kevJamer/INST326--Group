
from api import API



openweathermap = API()
weathermap = openweathermap.get_current_weather()
city_name = weathermap['city']
city_temp = weathermap['temp']   
daily = openweathermap.get_daily_weather(city_name)
city_temp_max = daily['max']
city_temp_min = daily['min']
todays_date = daily["date"]
dwind_dir = daily['dwind_dir']
dwindspeed = daily['dwindspeed']
rain_prob = daily['probability']
dcloud_cover = daily['dcloud_cover']
timezone = daily['timezone']
current_rain=daily['isitrain']



class Picture():
    
    rainbg = "rain_bg.jpeg"
    snowbg= "snow"
    cloudybg = "cloudy_bg.jpeg"
    sunnybg = "sunny_bg.jpeg"
    partly_cloddybg = "partly_bg.jpeg"
    night_timebg = "night_clear.jpeg"
    
    def __init__(self,cloud,rain):
        self.cloud = cloud
        self.rain = rain
       
       
    def isitnight():
        pass
    
    
    def isitrain (self):
        if self.rain > 0:
            isitrain = True
        else:
            isitrain = False
        return isitrain
    
     
    def choose_image(self):
            
        if self.cloud == "Clear" and self.isitrain() == False:
            return self.sunnybg
        elif self.cloud == "Mostly Sunny":
            return self.cloudybg   
        elif self.cloud == "partly cloudy":
            return self.partly_cloddybg
        elif self.cloud == "Mostly Cloudy":
            return self.partly_cloddybg
        elif self.cloud == "Cloudy":
            return self.cloudybg   

   
   
bg = Picture(dcloud_cover,current_rain).choose_image()
print(bg)