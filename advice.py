
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
    tempday = daily['daytemp'] 
    tempeve = daily['evetemp'] 
    tempnight = daily['nighttemp'] 


    #Class for giving advice to the user
    class Advice():
        
        """ Gives advice of what to wear to the user 
         Attributes: 
            jacket: string repersenting the type of jacket to wear
            unbrella: string repersenting rather or not to bring an unbrealla 
            gloves: string repersenting rather or not to wear gloves 
            hat: repersenting rather or not to wear a hat 
        """

        jacket = ""
        unbrella = ""
        gloves = ""
        hat = ""

        def __init__(self,daytemp,evetemp,nighttemp,rain):

           """ Initializes a Advice object.

            Args:
               daytemp(int): int value containg morning tempeture 
               evetemp(int): int value containg evening tempeture 
               nighttemp(int): int value containg nighttime tempeture 
               rain(float): float value containg the probaility of rain

            Raises:
               TypeError: all parameters must be int values
    
            """  

           self.daytemp = daytemp
           self.evetemp = evetemp
           self.nighttemp = nighttemp
           self.rain = rain
    
        def isitrain (self):
            """ Figures out if its going to rain.


            SideEffect:
                Sets isitrain to True or False
            Returns:
                isitrain(Boolean): repersenting rather or not its raining
    
            """      
            if self.rain > 0:
                isitrain = True
            else:
                isitrain = False
            return isitrain

        def day_advice(self):
            """ Figures out what advise to give the user for daytime weather.


            SideEffect:
                Modifies jacket,unbrella,gloves,and hat atrributes to the correct advice
    
            """    

            if self.daytemp >= 85 and self.isitrain() == False:
            
                self.jacket = "No need for a jacket"
                self.unbrella = False
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 85 and self.isitrain() == True:
                
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True
                self.gloves = False    
                self.hat = False        
            if self.daytemp >= 70 and self.isitrain() == False and self.daytemp < 85:
                self.jacket = "No need for a jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  

            if self.daytemp >= 70 and self.isitrain() == True and self.daytemp < 85:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 60 and self.isitrain() == False and self.daytemp < 70:
                self.jacket = "For colder indivisuals may advice a light jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 60 and self.isitrain() == True and self.daytemp < 70:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False 
            if self.daytemp >= 50 and self.isitrain() == False and self.daytemp < 60:
                self.jacket = "May advice a light to medium jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 50 and self.isitrain() == True and self.daytemp < 60:
                self.jacket = f"Would advice medium kacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False        
            if self.daytemp >= 40 and self.isitrain() == False and self.daytemp < 50:
                self.jacket = "May advice a medium to heavy jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 40 and self.isitrain() == True and self.daytemp < 50:
                self.jacket = f"Would advice heavy jacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.daytemp >= 30 and self.isitrain() == False and self.daytemp < 40:
                self.jacket = "Advice heavy jacket/coat"
                self.unbrella = False  
                self.gloves = False    
                self.hat = True  
            if self.daytemp >= 30 and self.isitrain() == True and self.daytemp < 40:
                self.jacket = f"Would Strongly advice heavy jacket/Coat with a hood, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True  
                self.gloves = True    
                self.hat = True   
            if self.daytemp < 29 and self.isitrain() == False:
                
                self.jacket = "Please bundle up"
                self.unbrella = False
                self.gloves = True    
                self.hat = True  
            if self.daytemp < 29 and self.isitrain() == True:
                
                self.jacket = f"Please bundle up and be cautious of potential harsh weather condiotions, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True
                self.gloves = True    
                self.hat = True      
        def eve_advice(self):
            """ Figures out what advise to give the user for evening weather.


            SideEffect:
                Modifies jacket,unbrella,gloves,and hat atrributes to the correct advice
    
            """          
            # code for suggested advice for evening weather 
            if self.evetemp >= 85 and self.isitrain() == False:
                
                self.jacket = "No need for a jacket"
                self.unbrella = False
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 85 and self.isitrain() == True:
                
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True
                self.gloves = False    
                self.hat = False        
            if self.evetemp >= 70 and self.isitrain() == False and self.evetemp < 85:
                self.jacket = "No need for a jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            
            if self.evetemp >= 70 and self.isitrain() == True and self.evetemp < 85:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 60 and self.isitrain() == False and self.evetemp < 70:
                self.jacket = "For colder indivisuals may advice a light jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 60 and self.isitrain() == True and self.evetemp < 70:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False 
            if self.evetemp >= 50 and self.isitrain() == False and self.evetemp < 60:
                self.jacket = "May advice a light to medium jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 50 and self.isitrain() == True and self.evetemp < 60:
                self.jacket = f"Would advice medium kacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False        
            if self.evetemp >= 40 and self.isitrain() == False and self.evetemp < 50:
                self.jacket = "May advice a medium to heavy jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 40 and self.isitrain() == True and self.evetemp < 50:
                self.jacket = f"Would advice heavy jacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.evetemp >= 30 and self.isitrain() == False and self.evetemp < 40:
                self.jacket = "Advice heavy jacket/coat"
                self.unbrella = False  
                self.gloves = False    
                self.hat = True  
            if self.evetemp >= 30 and self.isitrain() == True and self.evetemp < 40:
                self.jacket = f"Would Strongly advice heavy jacket/Coat with a hood, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True  
                self.gloves = True    
                self.hat = True   
            if self.evetemp < 29 and self.isitrain() == False:
                
                self.jacket = "Please bundle up"
                self.unbrella = False
                self.gloves = True    
                self.hat = True  
            if self.evetemp < 29 and self.isitrain() == True:
                
                self.jacket = f"Please bundle up and be cautious of potential harsh weather condiotions, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True
                self.gloves = True    
                self.hat = True
    

        def night_advice(self):
            """ Figures out what advise to give the user for night time weather.


            SideEffect:
                Modifies jacket,unbrella,gloves,and hat atrributes to the correct advice
    
            """  
         # code for suggested advice for night time weather 
            if self.nighttemp >= 85 and self.isitrain() == False:
            
                self.jacket = "No need for a jacket"
                self.unbrella = False
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 85 and self.isitrain() == True:
                
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True
                self.gloves = False    
                self.hat = False        
            if self.nighttemp >= 70 and self.isitrain() == False and self.nighttemp < 85:
                self.jacket = "No need for a jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
                
            if self.nighttemp >= 70 and self.isitrain() == True and self.nighttemp < 85:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 60 and self.isitrain() == False and self.nighttemp < 70:
                self.jacket = "For colder indivisuals may advice a light jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 60 and self.isitrain() == True and self.nighttemp < 70:
                self.jacket = f"Would advice light rain jacket, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False 
            if self.nighttemp >= 50 and self.isitrain() == False and self.nighttemp < 60:
                self.jacket = "May advice a light to medium jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 50 and self.isitrain() == True and self.nighttemp < 60:
                self.jacket = f"Would advice medium kacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = True  
                self.gloves = False    
                self.hat = False        
            if self.nighttemp >= 40 and self.isitrain() == False and self.nighttemp < 50:
                self.jacket = "May advice a medium jacket"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 40 and self.isitrain() == True and self.nighttemp < 50:
                self.jacket = f"Would advice heavy jacket with hood, there is a {rain_prob*100}% chance of rain"
                self.unbrella = False  
                self.gloves = False    
                self.hat = False  
            if self.nighttemp >= 30 and self.isitrain() == False and self.nighttemp < 40:
                self.jacket = "Advice heavy jacket/coat"
                self.unbrella = False  
                self.gloves = False    
                self.hat = True  
            if self.nighttemp >= 30 and self.isitrain() == True and self.nighttemp < 40:
                self.jacket = f"Would Strongly advice heavy jacket/Coat with a hood, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True  
                self.gloves = True    
                self.hat = True   
            if self.nighttemp < 29 and self.isitrain() == False:
                
                self.jacket = "Please bundle up"
                self.unbrella = False
                self.gloves = True    
                self.hat = True  
            if self.nighttemp < 29 and self.isitrain() == True:
                
                self.jacket = f"Please bundle up and be cautious of potential harsh weather condiotions, there is a {rain_prob*100}% chance of precipitation"
                self.unbrella = True
                self.gloves = True    
                self.hat = True
                
                
        def needunbrella(self):
            """ gives appropiate response for unbrella


            SideEffect:
                a string contaning the response
    
            """  
            
            if self.unbrella == True:
                return "Would advice unbrella"
            elif self.daytemp and self.evetemp and self.nighttemp < 45 and self.unbrella == False:
                return "Cold, but atleast its not raning "
            else:
                return ""
    
    
        def needhat(self):
            """ gives  appropiate response for hat


            Returns:
                a string contaning the response
    
            """  
            if self.hat == True:
                return "Dont forget your hat"
            else:
                return ""
                    
        
        def needgloves(self):
            """ gives  appropiate response for gloves


            SideEffect:
                 a string contaning the response
    
            """  
            if self.gloves == True:
                return "Its cold make sure you wear gloves"
            else:
                return ""       

except Exception:
    pass