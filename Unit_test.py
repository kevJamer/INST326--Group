import time
from weather import *
from bgimage import *
from advice import *


#UNIT TEST

pic = Picture



print(f"Tesing bgimage().chooseimage().....")
time.sleep(2)
try:
        def bgimage_test():
            # this test rather or not our if staments where correct in determing the correct image to use
            #(we used a unit test because we were unable to find enough places with different weather condiotions)
            test1 =  pic("partly cloudy",0,"500","200","600").choose_image()
            test2 =  pic("cloudy",.5,'500',"600",'800').choose_image()
            test3 =  pic("mostly cloudy",.1,"400","100","700").choose_image()

            
            assert test1 == "partly_bg.jpeg"
            assert test2 == "rain_bg.jpeg"
            assert test3 == "day_rainbg.jpg"
            
        
        bgimage_test()
    
except AssertionError:
    print(AssertionError)

else:
    print("passed")
    time.sleep(2)
    print("Testing Advice()...")

try:
    
    def advise_test(): 

        adv = Advice        
        test1 = adv(20,70,10,70)
        test1.day_advice()
        test2 = adv(50,90,105,0)
        test2.night_advice()
        
        
        
        assert test1.unbrella == True
        assert test2.hat == False
        assert test1.gloves == True
        
    advise_test()
    time.sleep(2)
    
except AssertionError:
    print(AssertionError)
    
else:
    print("passed")
    time.sleep(3)
    print("Testing....")

    