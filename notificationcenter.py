from tkinter import *
from datetime import date
from struct import pack
from turtle import bgcolor, width
from matplotlib.pyplot import fill
from api import *
from weather import Weather
import os
import sys
try:
    from bgimage import Picture
    from advice import Advice
except Exception:
    pass
import re
import threading
import time
import schedule
from email.message import EmailMessage
import smtplib


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


try:
    root = tk.Tk()
    root.title("Notification Center")
    root.geometry("600x600")
    root.config(bg="black")



    class NotificationCenter():
        '''allows user input and notifies the indivisual on suggestions
        
        '''
        def __init__(self,main):
        
            """ initializes NotificationCenter object

            Args:
            main: tk.TK()
            

            
            SideEffect:
                Creates a tkinter Frame with information
    
            """
            
            myframe = tk.Frame(main)
            myframe.pack()
            
            Welcome = tk.Label(main,text = f"Welcome To The Notification Center For \n {city_name}", width = 200, font=("Verdana", 24) )
            Welcome.pack(pady=50)
            
            inst = tk.Label(main,text= "If you want to get email updates everyday on what you should wear",width=200,font=("Verdana", 15),bg='black')
            inst.pack()
            
            
            self.lab_text = tk.StringVar(main)
            lab = tk.Label(main,text = "some text",textvariable=self.lab_text,bg="black")
            lab.pack()
        
        
            self.entry_text = tk.StringVar(main)
            entry = tk.Entry(main,textvariable=self.entry_text)
            entry.pack()
            note = tk.Label(main,text= "Please enter complete email",width=200,font=("Verdana", 10),bg='black')
            note.pack()
            user_email = tk.Button(main, text="submit", command=self.press_button,fg='black',bg='black')
            user_email.pack(pady=10)


            
            warning = tk.Label(main,text= "Warning: You cannot exit this program if you want contious updates",width=200,font=("Verdana", 10),bg='black')
            warning.pack(pady=50)

        
        
        
        
        def press_button(self):
            
            """ determines what happen after hitting button

            
            SideEffect:
                Emails user updates everyday on suggestions aslong as the window is open
                
            Rasies:
                TypeError: if str value is not inputed 
                ValueError: if non valid email is inputed
            """
            text = self.entry_text.get()
            self.entry_text.set("")
            # The def run_continously is directly from Daniel Bader https://schedule.readthedocs.io/en/stable/
            def run_continuously(interval=1):
            
                cease_continuous_run = threading.Event()

                class ScheduleThread(threading.Thread):
                    @classmethod
                    def run(cls):
                        while not cease_continuous_run.is_set():
                            schedule.run_pending()
                            time.sleep(interval)

                continuous_thread = ScheduleThread()
                continuous_thread.start()
                return cease_continuous_run
                    
                    
            
            
            def email(text):
            
            
            #This email structure we copied from a tutorial on youtube by Jake https://www.youtube.com/watch?v=B1IsCbXp0uE
            #the contents we wrote ourselves 
                msg = EmailMessage()
                msg.set_content(f"{Body().BodyOne()}\n{Body().BodyTwo()}\n{Body().BodyThree()}")
                msg['subject'] = f"Clothing Advice"
                msg['to']=text
                    
                user = "weatherapp326@gmail.com"
                msg['from'] = user
                password = "pwefmtpvuftyumon"
                
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(user,password)
        
                server.send_message(msg)

                server.quit()
                
            #aniel Bader https://schedule.readthedocs.io/en/stable/
            schedule.every().day.do(email,text=f'{text}')

            # Start the background thread
            stop_run_continuously = run_continuously()

            time.sleep(1)

except Exception:
    pass           
        

        


try:
    class Body():
        ''' contains body of email
        '''
        def __init__(self):
            """ initializes a Body object 

            
            SideEffect:
            Runs 
                    adv.day_advice()
                    adv.eve_advice()
                    adv.night_advice
            which modifies advice atributes
        
                
            Return:
                Retrun string values contaning the body of the email.
        """

            self.morning = adv.day_advice()
            self.eve =  adv.eve_advice()
            self.night =  adv.night_advice
        
        def needunbrella(self):
            if adv.unbrella == True:
                return "May need unbrella"
            else:
                return ""
            
        def needhat(self):
            if adv.hat == True:
                return "May need to bring a hat"
            else:
                return ""
            
        def needgloves(self):
            if adv.gloves == True:
                return "May need to wear gloves"
            else:
                return ""
        
        def BodyOne(self):
            self.morning
            return str(f"Hello, The Current tempeture is: {city_temp}° with an high of {city_temp_max}°"
                        f" and a low of {city_temp_min}°\nMorning suugestions: {adv.jacket}\n{self.needunbrella()}\n{self.needhat()}\n{self.needgloves()}\n")
        def BodyTwo(self):
            self.eve
            return f"Evening Suggestions: {adv.jacket}\n{self.needunbrella()}\n{self.needhat()}\n{self.needgloves()}\n"
        def BodyThree(self):
            self.night
            return f"Night Suggestions: {adv.jacket}\n{self.needunbrella()}\n{self.needhat()}\n{self.needgloves()}\n"
        




    e = NotificationCenter(root)

except Exception:
    pass

