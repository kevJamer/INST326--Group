from datetime import date
from struct import pack
import tkinter as tk
from turtle import bgcolor
from matplotlib.pyplot import fill
from api import *
from weather import Weather
from PIL import ImageTk, Image
import os
import sys
from bgimage import Picture
from advice import Advice



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
fivedayforcast= [daily['one_max_forcast'],daily['two_max_forcast'],daily['three_max_forcast'],daily['four_max_forcast'],daily['five_max_forcast']] 

adv = Advice(tempday,tempeve,tempnight,rain_prob)

dayadvice = adv.day_advice()
eveadvice = adv.eve_advice()
nightadvice = adv.night_advice()
unbrellaadvice = adv.needunbrella()
hatadvice = adv.needhat()
gloveadvice = adv.needgloves()

weather_program = Weather((city_temp_min,city_temp_max),dcloud_cover,rain_prob,(int(dwindspeed),dwind_dir))
weather = weather_program.make_description()[0]
bgpicture = Picture(dcloud_cover,current_rain).choose_image()

LARGE_FONT= ("Verdana", 18)
class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title(f"{city_name}")
        self.geometry("600x670")
        self.maxsize(600,710)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=2)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        
        frame.tkraise()
    
   
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
       

        
        
        
        bg = Image.open(bgpicture)
        newsize = (600, 300) 
        bg = bg.resize(newsize)
        
        bg = ImageTk.PhotoImage(bg)

        my_canvas = tk.Canvas(self,width=100,height=100)
        my_canvas.image = bg
        my_canvas.pack(fill="both",expand=True)
        my_canvas.create_image(0,0,image=bg,anchor ="nw")
        
        
        
        
        #sun_back = tk.Label(self,image=bg)
        #sun_back.image = bg
        #sun_back.place(x=0,y=0,relwidth=1,relheight=1)
        
    
        label = tk.Label(self, text=f"{city_name}", font=LARGE_FONT)
        label.config(font =("Consolas",50))
        label.pack(pady=10,padx=10)
        temp = tk.Label(self, text=f"{city_temp} f")
        temp.config(font =("Consolas",22))
        temp.pack(side='top')
        program = tk.Label(self, text = f"{weather}",wraplength=300, justify="center")
        program.config(font =("Consolas",15))
        program.pack(side='top')
        
        self.lab_text = tk.StringVar(self)
        lab = tk.Label(self,text = "some text",textvariable=self.lab_text)
        lab.pack()
        
        
        self.entry_text = tk.StringVar(self)
        entry = tk.Entry(self,textvariable=self.entry_text)
        entry.pack()
        
       
        tell_date = tk.Label(self, text = f'Date: {todays_date}')
        tell_date.pack()
        
        
        #tell_zone = tk.Label(self, text = f'Date: {timezone}')
        #tell_zone.pack()
        
       
        user_zip = tk.Button(self, text="submit", command=self.press_button,fg='blue')
        user_zip.pack()
        
        space_label = tk.Label(self,text="")
        space_label.pack()
        
        button3 = tk.Button(self, text="Night Advie",
                            command=lambda: controller.show_frame(PageThree,fill="White"))
        button3.pack(side="bottom")
        button2 = tk.Button(self, text="Evenig Advice",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side='bottom')
        button = tk.Button(self, text="Morning Advice",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(side='bottom')
        
        forcastcanvas = tk.Canvas(self,width=150,height=400)
        forcastcanvas.place(x=-3,y=266,anchor="nw")
        text = forcastcanvas.create_text(3, 0, width =150, text=f"5-day forcast", font="Verdana, 20", fill="black",anchor='nw')
    
    
    
    def press_button(self):
        text = self.entry_text.get()
        self.lab_text.set(text)
        f= open("zip_code_update.txt", "w")
        f.write(f"{text}")
        f.close()
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)   
  
        
       

        
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Morning Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        adv.day_advice()
        my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
        my_advice.pack(side="top")
    
       
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="bottom")
        button2 = tk.Button(self, text="Evening Advice",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side="bottom")
        button3 = tk.Button(self, text="Night Advice",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side="bottom")       
        
        

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Evening Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        adv.eve_advice()
        my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
        my_advice.pack(side="top")
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Night Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        adv.night_advice()
        my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
        my_advice.pack(side="top")
    
       
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()        

app = Main()
app.mainloop()