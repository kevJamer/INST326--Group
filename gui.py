from tkinter import *
from api import API
from weather import Weather

root = Tk()
openweathermap = API()
weathermap = openweathermap.get_current_weather()
city_name = weathermap['city']
city_temp = weathermap['temp']   
weather_program = Weather((city_temp,city_temp),city_name,.5,(5,6))
weather = weather_program.make_description()


   
class GUI():
   
    root.geometry("300x300")
    root.title(f"{city_name} Weather")
   
    def display_name(city):
        city_label = Label(root, text=f"{city_name}")
        city_label.config(font =("Consolas",28))
        city_label.pack(side='top')
    
    def display_stats(temp):
        temp = Label(root, text=f"{city_temp} f")
        temp.config(font =("Consolas",22))
        temp.pack(side='top')
    def display_program(description):
        program = Label(root, text = f"{weather}",wraplength=300, justify="center")
        program.config(font =("Consolas",15))
        program.pack(side='top')

gui = GUI()
dis_name = gui.display_name()
dis_stats = gui.display_stats()
dis_program = gui.display_program()

mainloop()