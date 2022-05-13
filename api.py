from datetime import datetime
import tkinter as tk
import requests

class API():
    
    """ Calls the upon openweatherapp api to find weather data
     
     Attributes: 
        Api_key: Holds the key to access the Api
    """
    
    api_key = f"de24ba549fe9b21406f59888864dfaf2"  
    
    def __init__(self):
         """ Initializes an Api object.

        SideEffect:
           calls upon find_zip() function.
  
        """
         self.zip_code = self.find_zip()
         self.api_key = self.api_key
     
    def find_zip(self):
        """ reads zip cod from zip_code_update.txt

        Raises:
           ValueError: must be a valid zipcode
           
        Returns:
            int value repersenting the zipcode
  
        """
        f = open("zip_code_update.txt", "r")
        zip_code = f.read()
        return zip_code 
    
   
    def dayornight(self,date,offset):
        """ creates the right timezone

        Args:
           date(int): int value containg date in unix timestamp
           offest(int): int value containg offset data based on the timezone 

        Raises:
           TypeError: all parameters must be int values
           
        Retuns:
            string varible contaning formated date
  
        """
        #calculate the date based on users timezone using the unix value + the unix offest besed on there timezone
        time= date+offset
        return time
    
    def tell_date(self,date,offset):
        """ Converts the unix time stamp

        Args:
           date(int): int value containg date in unix timestamp
           offest(int): int value containg offset data based on the timezone 

        Raises:
           TypeError: all parameters must be int values
           
        Retuns:
            string varible contaning formated date
  
        """
        #calculate the date based on users timezone using the unix value + the unix offest besed on there timezone
        todays_date = date+offset
        # convert the unix time stamp into a readable format
        todays_date = datetime.utcfromtimestamp(todays_date) 
        #format the data
        todays_date = todays_date.strftime("%b %d %Y %H:%M")
        return todays_date
    
    def temp_conversion(self,temp):
        """ Converts the tempeture from kelvin to fahrenheit

        Args:
           temp(int): int value containg passed in temp

        Raises:
           TypeError: must be int varible
        
        Returns: 
            int temp in fahrenheit
  
        """
        #conversion
        converted_temp=int((temp * 1.8) - 459.67)
        return converted_temp
        
   
    def wind_direction(self,wind):
        """ Converts meteorological degrees into compas directions.

        Args:
           wind(int): int value containg passed in wind varibile 

        Raises:
           TypeError: must be int varible
        
        Returns: 
            str varible contaning the computed wind direction
  
        """      
      
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
        """ Converts cloud cover precentage into descriptive terms

        Args:
           cloud(int): int value containg passed in cloud varibile 

        Raises:
           TypeError: must be int varible
           ValueErros must be between 0-100
        
        Returns: 
            str varible contaning the descriptive term
  
        """ 
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
        """ calls upon the api to retrieve weather information

        Raises:
           ValueError: must import correct api key and zipcode(int)
        
        SideEffects:
            Calls upon the openweatherapp Api
            Stores dictonary values into local varibles 
        
        Returns: 
            dictionary varible contaning current temp and city name
  
        """ 
        try:
            geo = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code}&appid={self.api_key}"
            geocoder = requests.get(geo).json()
            lat = geocoder["lat"]
            lon = geocoder['lon']
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
            response = requests.get(url).json() 
            temperature = response['main']['temp']
            city_name = response['name']
            temperature = int((temperature * 1.8) - 459.67)
        except Exception:
            return "error"
        
        return {
            'temp' : temperature,
            'city' : city_name
        }
    def get_daily_weather(self,city_name):
        """ calls upon the api to retrieve weather information

        Raises:
           ValueError: must import correct api key and zipcode(int)
           
        SideEffects:
            Calls upon the openweatherapp Api
            Stores dictonary values into local varibles 
        
        Returns: 
            dictionary varible contaning necessary weather information 
  
        """ 
        try:
            geo = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code}&appid={self.api_key}"
            geocoder = requests.get(geo).json()
            lat = geocoder['lat']
            lon = geocoder['lon']
            url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=&appid={self.api_key}"
            response = requests.get(url).json() 
            city = city_name
        except Exception:
            return "error"
            

           
        #DATE
        timezone = response['timezone']
        date = response["minutely"][0]["dt"]
        offset = response["timezone_offset"]
        con_date = self.tell_date(date,offset)
        current_hour = response['minutely'][0]['dt']
        current_hour = self.dayornight(current_hour,offset)
        
        #Day and Night
        sunset = response['daily'][0]['sunset']
        sunset = self.dayornight(sunset,offset)
        sunrise = response['daily'][0]['sunrise']
        sunrise = self.dayornight(sunrise,offset)
        
        #Rain
        daily_pop = response['daily'][0]["pop"]
        current_rain = response['minutely'][0]["precipitation"]

        
        #Tempeture (morning,evening,night)
        daytemp = self.temp_conversion(response['daily'][0]['feels_like']['morn'])
        evetemp = self.temp_conversion(response['daily'][0]['feels_like']['eve'])
        nighttemp = self.temp_conversion(response['daily'][0]['feels_like']['night'])
       
        #Temp min and max
        temp_min = self.temp_conversion(response['daily'][0]["temp"]["min"])
        temp_max= self.temp_conversion(response['daily'][0]["temp"]["max"])
        
         #Wind
        dwind_dir = self.wind_direction(response['daily'][0]['wind_deg'])
        cwind_dir = self.wind_direction(response['current']['wind_deg'])
        current_wind_speed = response["current"]["wind_speed"]
        daily_wind_speed = response['daily'][0]['wind_speed']
       
        #Clouds
        desc_day_clouds = self.cloudy(response['daily'][0]['clouds'])
        desc_cur_clouds = self.cloudy(response['current']['clouds'])
       
       # Five day forcast
        one_day_forcast = response['daily'][0]['temp']['max']
        two_day_forcast = response['daily'][1]['temp']['max']
        three_day_forcast = response['daily'][2]['temp']['max']
        four_day_forcast = response['daily'][3]['temp']['max']
        five_day_forcast = response['daily'][4]['temp']['max']              
        
        return {
            "date" : str(con_date),
             "min" : temp_min,
             "max" : temp_max,
             "probability" : daily_pop,
             "isitrain":current_rain,
             'dwindspeed': daily_wind_speed,
             'cwindspeed': current_wind_speed,
             'dwind_dir': dwind_dir,
             'cwind_dir': cwind_dir,
             'dcloud_cover':desc_day_clouds,
             'ccloud_cover':desc_cur_clouds,
             'timezone':timezone,
             'daytemp':daytemp,
             'evetemp':evetemp,
             'nighttemp':nighttemp,
             'one_max_forcast':one_day_forcast,
             'two_max_forcast':two_day_forcast,
             'three_max_forcast':three_day_forcast,
             'four_max_forcast':four_day_forcast,
             'five_max_forcast':five_day_forcast,
             'sunset': sunset,
             'sunrise': sunrise,
             'current_hour':current_hour
        }




api = API()
current_weather = api.get_current_weather()
city = current_weather["city"]
day_weather = api.get_daily_weather(city)
print(day_weather)
