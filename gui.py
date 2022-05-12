
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
try:
    from bgimage import Picture
    from advice import Advice
except Exception:
    pass
import re


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
    
except Exception:
    pass


LARGE_FONT= ("Verdana", 18)
class Main(tk.Tk):
    """ Creates the foundation of gui
     args
        tk.Tk:
    """
    
    
    def __init__(self, *args, **kwargs):
        """ initializes main object

        Args:
           args: (tuple)
           kwargs: dictionary

           
        SideEffect:
            Creates and initialize a tkinter frame, and then formats it
  
        """
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        try:
            self.title(f"{city_name}")
        except Exception:
            self.geometry("600x450")
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
        
        else:
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
        """ shows the page i selceted 

        Args:
           cont: repersenting the page im on

           
        SideEffect:
            shows the frame you have chosen
  
        """
        
        frame = self.frames[cont]
        
        frame.tkraise()
    
   
class StartPage(tk.Frame):
    """ Creates startpage
     args
        tk.Frame:
    """
    
    def __init__(self, parent, controller):
       
       
        """ initializes Starpage object

        Args:
           paremt: 
           controller: 

           
        SideEffect:
            creats a user input
            initalizes 3 buttons
  
        """
        
        tk.Frame.__init__(self,parent)
        
       

        
        
        
        try:
            bg = Image.open(bgpicture)
            newsize = (600, 300) 
            bg = bg.resize(newsize)

            bg = ImageTk.PhotoImage(bg)

            my_canvas = tk.Canvas(self,width=100,height=100)
            my_canvas.image = bg
            my_canvas.pack(fill="both",expand=True)
            my_canvas.create_image(0,0,image=bg,anchor ="nw")
        
        
        
    
        
    
            label = tk.Label(self, text=f"{city_name}", font=LARGE_FONT)
            label.config(font =("Consolas",50))
            label.pack(pady=10,padx=10)
            temp = tk.Label(self, text=f"{city_temp} f")
            temp.config(font =("Consolas",22))
            temp.pack(side='top')
            program = tk.Label(self, text = f"{weather}",wraplength=300, justify="center")
            program.config(font =("Consolas",15))
            program.pack(side='top')
        except Exception:
            bg = Image.open("space.jpeg")
            newsize = (600, 300) 
            bg = bg.resize(newsize)

            bg = ImageTk.PhotoImage(bg)

            error_can = tk.Canvas(self,width=600,height=250)
            error_can.image = bg
            error_can.pack(fill="both",expand=True)
            error_can.create_image(0,0,image=bg,anchor ="nw")
            error = error_can.create_text(90, 0, width =600, text=f"Sorry, your location cannot be found", font="Verdana, 30", fill="White",anchor='nw')
            error2 = error_can.create_text(200, 250, width =600, text=f"Please try again!", font="Verdana, 30", fill="White",anchor='nw')
            

            
            self.lab_text = tk.StringVar(self)
            lab = tk.Label(self,text = "some text",textvariable=self.lab_text)
            lab.pack()
        
        
            self.entry_text = tk.StringVar(self)
            entry = tk.Entry(self,textvariable=self.entry_text)
            error_can.create_window(200, 330, window=entry ,anchor='nw')
        else:
            

            self.lab_text = tk.StringVar(self)
            lab = tk.Label(self,text = "some text",textvariable=self.lab_text)
            lab.pack()
        
        
            self.entry_text = tk.StringVar(self)
            entry = tk.Entry(self,textvariable=self.entry_text)
            entry.pack()
        
       
        
        try:
            tell_date = tk.Label(self, text = f'Date: {todays_date}')
            tell_date.pack()
        except Exception:
            user_zip = tk.Button(self, text="submit", command=self.press_button,fg='blue')
            user_zip.pack(side="top")
            error_can.create_window(258, 365, window=user_zip, anchor='nw')
        else:

        
       
            user_zip = tk.Button(self, text="submit", command=self.press_button,fg='blue')
            user_zip.pack()
        
            space_label = tk.Label(self,text="")
            space_label.pack()
            
            button3 = tk.Button(self, text="Night Advie",
                                command=lambda: controller.show_frame(PageThree))
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
           
        """ determines what happen after hitting button

           
        SideEffect:
            opens up and writes to a text document based on users input
            restarts the entire program with new zip
            
        Rasies:
            TypeError: if int value is not inputed 
            ValueError: if correct zipcode is not instered.
        """
        
        text = self.entry_text.get()
        self.lab_text.set(text)
        f= open("zip_code_update.txt", "w")
        f.write(f"{text}")
        f.close()
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
  
  
  
        
       

        
        
class PageOne(tk.Frame):
    """ Page one of tkinter frame

        Args:
           tk.frame
  
        """
    def __init__(self, parent, controller):
        """ initializes PageOne object

        Args:
           paremt: 
           controller: 

           
        SideEffect:
            runs day_advice method
  
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Morning Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        try:
            adv.day_advice()
            my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
            my_advice.pack(side="top")
        except Exception:   
            pass
 


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
    """ Page two of tkinter

        Args:
           tk.frame
  
        """
    def __init__(self, parent, controller):
        """ initializes PageTwo object

        Args:
           paremt: 
           controller: 

           
        SideEffect:
            runs eve_advice() method
  
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Evening Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        try:
            adv.eve_advice()
            my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
            my_advice.pack(side="top")
        except Exception:
            pass

        button1 = tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                                command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(tk.Frame):
    """ Page Three of tkinter

        Args:
           tk.frame
  
        """
    def __init__(self, parent, controller):
        """ initializes PageThree object

        Args:
           paremt: 
           controller: 

           
        SideEffect:
            runs night_advice() method
  
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Night Advice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        try:
            adv.night_advice()
            my_advice = tk.Label(self,text=f"{adv.jacket}{unbrellaadvice}")
            my_advice.pack(side="top")
        except Exception:
            pass

        button1 = tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                                command=lambda: controller.show_frame(PageTwo))
        button2.pack()        

        


if __name__ == "__main__":
    app = Main()
    app.mainloop()