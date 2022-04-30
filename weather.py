from datetime import datetime
import sys
from argparse import ArgumentParser

class Day():
    ''' holds the days of the week
    Attributes:
        Date: a integer value holding the day 
        Month: a intger vaule holding the month
        Year: a intger vaule holding the year
        Weather: 
        
    '''
    def __init__(self, Date=0, Month=0, Year=0):
        """ Initializes a Day object.

        Args:
            Date: a integer value holding the day 
            Month: a intger vaule holding the month
            Year: a intger vaule holding the year
            Weather:
            
        RaiseVaule:
           
        """
        self.date = Date
        self.month = Month
        self.year = Year
        #self.Weather = Weather((32,60),"Partilaly Cloudy",.25,('NW',5))
    
class Weather():
    ''' Holds data varibles for the weather '''
    # precip = inches/hr if rain and incches after snow for snow    

    def __init__(self, temperature=tuple, cloud_cover=str, precipitation=float, wind=tuple):
        """ Initializes a Weather object.

        Args:
            temperature: a integer value holding the temperature in degrees Farenhight 
            cloud_cover: sting value that holds cloud cover information
            precipitation: a intger vaule holding the amount of precipitation as a percentage.
            wind: a tuple containg the dircetion of the wind as a str and the speed in mph as a int
            
        RaiseVaule:
           
        """        
        self.temperature = temperature
        self.cloud_cover = cloud_cover
        self.precipitation = precipitation
        self.wind = wind
        
        
    def make_description(self):
        """ creates 

        Args:
            Self:
            
        Return: 
             description: 
           
        """   
        description = ""
        description += "High: " + str(self.temperature[1]) + " Farenheit, Low: " + str(self.temperature[0]) + " Farenheit, "
        description += str(self.cloud_cover) + ", "

        if (self.temperature[1] + self.temperature[0]) / 2 > 32:
            if self.precipitation == 0:
                description += "No Rain, "
            if self.precipitation < 0.098:
                desription += "Light Rain, "
            elif self.precipitation > 0.098 and self.precipitation < .39:
                description += "Moderate Rain, "
            elif self.precipitation > .39 and self.precipitation < 2.0:
                description += "Heavy Rain, "
            elif self.precipitation > 2.0:
                description += "Violent Rain, "
        elif (self.temperature[1] + self.temperature[0]) / 2 < 33:
            if self.precipitation == 0:
                description += "No Snow, "
            if self.precipitation > 0 or self.precipitation < 1: 
                description += "Flurries of snow, "
            else:
                description += str(self.precipitation) + " inches of snow, "
            
        description += str(self.wind[1]) + " " + str(self.wind[0]) + " winds."

        print(description)
        return description

    
def advice(description):
    """ gives the advice on what the user should do 

        Args:
            
            
        Return: 
             advice_user: returns the advice needed to be given by the user as a str.
           
        """   
    print()

def main():
    """ Main statment

        Args:
            
            
        sideeffect: 
             print: prints out the results of make_description.
           
        """   
    day = Day(1, 1 , 2000, Weather)
    print(day.Weather.make_description)

if __name__ == "__main__":
    main()
    
    

