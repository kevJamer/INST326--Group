
from api import API


    #Creating varibles that contains dictionary vaules from imported APi() class
try:
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
        """ Displays correct picture
        
        Attributes: 
            rainbg: holds name of image file 
            snowbg: holds name of image file  
            cloudybg: holds name of image file 
            sunnybg: holds name of image file 
            partly_cloudybg: holds name of image file 
            night_timebg: holds name of image file 
        """
        
        
        rainbg = "rain_bg.jpeg"
        snowbg= "snow"
        cloudybg = "cloudy_bg.jpeg"
        sunnybg = "sunny_bg.jpeg"
        partly_cloddybg = "partly_bg.jpeg"
        night_timebg = "night_clear.jpeg"
        
        def __init__(self,cloud,rain):
            """ Initializes a Picture object.

            Raises:
            ValueError: cloud must be a string contating the correct descriptions
            TypeErros: rain must be an int varible
    
            """
            self.cloud = cloud
            self.rain = rain
        
        
        def isitnight(self):
            """ Determines rather or not its night



            Raises:
            
            
            Retuns:
                bolean rather or not its night
    
            """
            pass
        
        
        def isitrain (self):
            """ determine if it is currently raning 

            Args:
            date(int): int value containg date in unix timestamp
            offest(int): int value containg offset data based on the timezone 

            Raises:
            TypeError: rain must be int value
            
            Retuns:
                boolean determinng if its raning
    
            """
            if self.rain > 0:
                isitrain = True
            else:
                isitrain = False
            return isitrain
        
        
        def choose_image(self):
            """ chooses the image displayed on the gui
            
            Retuns:
                returns attribute containg the correct filename
    
            """
                
            if self.cloud == "Clear" and self.isitrain() == False:
                return self.sunnybg
            elif self.cloud == "Mostly Sunny":
                return self.sunnybg   
            elif self.cloud == "partly cloudy":
                return self.partly_cloddybg
            elif self.cloud == "Mostly Cloudy":
                return self.partly_cloddybg
            elif self.cloud == "Cloudy" and self.isitrain() == False:
                return self.cloudybg
            elif self.cloud == "Cloudy" and self.isitrain() == True:
                return self.rainbg 

    
    if __name__ == "__main__"   :
        bg = Picture(dcloud_cover,current_rain).choose_image()
        print(bg)
except Exception:
    pass