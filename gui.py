import tkinter as tk
from api import *
from weather import Weather
from PIL import ImageTk, Image
import os
import sys


openweathermap = API()
weathermap = openweathermap.get_current_weather()
city_name = weathermap['city']
city_temp = weathermap['temp']   
daily = openweathermap.get_daily_weather(city_name)

weather_program = Weather((city_temp,city_temp),city_name,.5,(5,6))
weather = weather_program.make_description()



LARGE_FONT= ("Verdana", 18)
class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(f"{city_name}")
        self.geometry("500x400")
        self.maxsize(1000,800)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
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
        label = tk.Label(self, text=f"{city_name}", font=LARGE_FONT)
        label.config(font =("Consolas",100))
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
       
        user_zip = tk.Button(self, text="submit", command=self.press_button)
        user_zip.pack()
        
        
        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack(side="bottom")
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageTwo))
        button.pack(side="bottom")
        
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
        label = tk.Label(self, text="CAT!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("weather.jpeg")
        newsize = (400, 400) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CAT!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        img = Image.open("weather.jpeg")
        newsize = (400, 200) 
        img = img.resize(newsize) 
        img = ImageTk.PhotoImage(img)
        picture = tk.Label(self, image = img)
        picture.image = img
        picture.pack()
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        

app = Main()
app.mainloop()