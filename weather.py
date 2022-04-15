from datetime import date
import sys
from argparse import ArgumentParser

class Day():
    def __init__(self, Date, Month, Year, Weather):
        self.date = Date
        self.Month = Month
        self.Year = Year
        self.Weather = Weather((32,60),"Partilaly Cloudy",.25,('NW',5))
    
class Weather():
    # precip = inches/hr if rain and incches after snow for snow

    def __init__(self, temperature, cloud_cover, precipitation, wind):
        self.temperature = temperature
        self.cloud_cover = cloud_cover
        self.precipitation = precipitation
        self.wind = wind


    def make_description(self):
        description = ""
        description += "High: " + str(self.temperature[1]) + " Fearhenheit, Low: " + str(self.temperature[0]) + ", "
        description += str(self.cloud_cover) + ", "

        if (self.temperature[1] + self.temperature[0]) / 2 > 32:
            if self.precipitation == 0:
                desc += "No Rain, "
            if self.precipitation < 0.098:
                desc += "Light Rain, "
            elif self.precipitation > 0.098 and self.precipitation < .39:
                dec += "Moderate Rain, "
            elif self.precipitation > .39 and self.precipitation < 2.0:
                desc += "Heavy Rain, "
            elif self.precipitation > 2.0:
                desc += "Violent Rain, "
        elif (self.temperature[1] + self.temperature[0]) / 2 < 33:
            if self.precipitation == 0:
                desc += "No Snow, "
            if self.precipitation > 0 or self.precipitation < 1: 
                desc += "Flurries of snow, "
            else:
                desc += str(self.precipitation) + " inches of snow, "
            
        desc += str(self.wind[1]) + " " + str(self.wind[0]) + " winds."

        return description
    
def advice(Day):
    print()

def main():
    print()
    
if __name__ == "__main__":
    main()