import pywhatkit as kit
from Body.listen import micExecution
import datetime
from Body.speak import speak
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
import datetime


def sendMessage():
    name_id={"Method":"+919873527717",
                      "shreya":"+919871631633",
                      "ashish":"+918351984261",
                      "younger brother":"+917840880604"
                      }
    
    name=micExecution().lower()
    
    if len(name)<3:
        speak("Boss you didn't give me a name..")   
        sendMessage()
        
    elif name in name_id.keys():
        num=str(name_id.values())        
        speak("Boss what message you want to send")
        msg=micExecution().lower()       
        hour=int(datetime.datetime.now().strftime("%H"))
        min=int((datetime.datetime.now()+timedelta(minutes = 2)).strftime("%M"))
        speak("sending the message")
        kit.sendwhatmsg(num,msg,hour,min)        
            
    else:
        speak("Boss I coundn't find the contact")
        sendMessage()
     
    
    
          
    
            
